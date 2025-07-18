import pandas as pd
import requests
from datetime import datetime
from typing import List, Optional, Union

BASE_URL = "https://www.isyatirim.com.tr/_layouts/15/IsYatirim.Website/Common/Data.aspx/MaliTablo"

def fetch_financials(
    symbols: Union[List[str], str],
    start_year: Optional[Union[str, int]] = None,
    end_year: Optional[Union[str, int]] = None,
    exchange: str = 'TRY',
    financial_group: str = '1',
    save_to_excel: bool = False
) -> pd.DataFrame:
    """
    Fetch annual and quarterly financial statement data for one or more symbols from the IS Investment API.

    Parameters
    ----------
    symbols : str or list of str
        Stock symbol or list of stock symbols for which to fetch financials.
    start_year : str or int, optional
        Start year (inclusive). Defaults to two years prior to the current year.
    end_year : str or int, optional
        End year (inclusive). Defaults to the current year.
    exchange : str, default 'TRY'
        Currency ('TRY' or 'USD').
    financial_group : str, default '1'
        Financial group identifier: '1' for XI_29, '2' for UFRS, or '3' for UFRS_K.
    save_to_excel : bool, default False
        If True, saves the resulting statements to an Excel file.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing all financial statements for all requested symbols, stacked vertically, with a SYMBOL column.
    """
    if not symbols:
        raise ValueError("The 'symbols' parameter is required and cannot be empty.")
    if isinstance(symbols, str):
        symbols = [symbols]
    try:
        start_year = int(start_year) if start_year else datetime.now().year - 2
        end_year = int(end_year) if end_year else datetime.now().year
    except Exception:
        raise ValueError("'start_year' and 'end_year' must be convertible to integers.")

    if end_year < start_year:
        raise ValueError("'end_year' must be greater than or equal to 'start_year'.")

    if exchange.upper() not in ('TRY', 'USD'):
        raise ValueError("The 'exchange' parameter must be either 'TRY' or 'USD'.")

    if financial_group not in ('1', '2', '3'):
        raise ValueError("The 'financial_group' parameter must be '1' (XI_29), '2' (UFRS), or '3' (UFRS_K).")

    group_map = {'1': 'XI_29', '2': 'UFRS', '3': 'UFRS_K'}
    financial_group_label = group_map[financial_group]

    periods = [3, 6, 9, 12]
    data_frames = []

    for symbol in symbols:
        urls = []
        for year in range(start_year, end_year + 1):
            params = {
                "companyCode": symbol,
                "exchange": exchange.upper(),
                "financialGroup": financial_group_label,
                "year1": year, "period1": periods[0],
                "year2": year, "period2": periods[1],
                "year3": year, "period3": periods[2],
                "year4": year, "period4": periods[3]
            }
            param_str = '&'.join(f"{k}={v}" for k, v in params.items())
            urls.append(f"{BASE_URL}?{param_str}")

        data_list = []
        quarters = [f"{year}/{month}" for year in range(start_year, end_year + 1) for month in periods]

        for url in urls:
            try:
                res = requests.get(url, timeout=10)
                res.raise_for_status()
                result = res.json()
                if result.get('value'):
                    df = pd.DataFrame(result['value'])
                    if not df.empty:
                        base_cols = df.columns[:3].tolist()
                        quarter_cols = quarters[:4]
                        df.columns = base_cols + quarter_cols
                        quarters = quarters[4:]
                        data_list.append(df)
                    else:
                        quarters = quarters[4:]
                else:
                    quarters = quarters[4:]
            except Exception as e:
                print(f"[Warning] Could not fetch data for '{symbol}' in one period: {e}")
                quarters = quarters[4:]

        if data_list:
            df_final = data_list[0]
            for i in range(1, len(data_list)):
                df_final = pd.merge(
                    df_final, data_list[i],
                    on=['itemCode', 'itemDescTr', 'itemDescEng'],
                    how='outer', suffixes=('', f'_{i}')
                )
            null_cols = df_final.columns[df_final.isnull().all()]
            df_final = df_final.drop(columns=null_cols)
            for col in ['itemCode', 'itemDescTr', 'itemDescEng']:
                if col in df_final.columns:
                    df_final[col] = df_final[col].astype(str).str.strip()
            df_final["SYMBOL"] = symbol
            df_final = df_final.rename(columns={
                "itemCode": "FINANCIAL_ITEM_CODE",
                "itemDescTr": "FINANCIAL_ITEM_NAME_TR",
                "itemDescEng": "FINANCIAL_ITEM_NAME_EN"
            })
            data_frames.append(df_final)
        else:
            print(f"[Info] No financial data found for symbol '{symbol}'. You may need to adjust the financial_group or years.")

    if not data_frames:
        raise ValueError("No financial data was fetched for any symbol. Please check your parameters.")

    combined_data = pd.concat(data_frames, ignore_index=True)

    if save_to_excel:
        current_datetime = datetime.now().strftime("%Y%m%d")
        file_name = f"financials_{current_datetime}.xlsx"
        combined_data.to_excel(file_name, index=False)
        print(f"[Success] Data saved to '{file_name}'.")

    return combined_data