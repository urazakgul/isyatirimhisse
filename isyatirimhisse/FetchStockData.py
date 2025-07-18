import requests
import pandas as pd
from datetime import datetime
from typing import List, Optional, Union

BASE_URL = "https://www.isyatirim.com.tr/_layouts/15/Isyatirim.Website/Common/Data.aspx/HisseTekil"

def fetch_stock_data(
    symbols: Union[List[str], str],
    start_date: str,
    end_date: Optional[str] = None,
    save_to_excel: bool = False
) -> pd.DataFrame:
    """
    Fetch raw daily stock data for one or multiple symbols from the IS Investment API.

    Parameters
    ----------
    symbols : str or list of str
        Stock symbol or list of stock symbols for which to fetch data.
    start_date : str
        Start date in 'dd-mm-yyyy' format.
    end_date : str, optional
        End date in 'dd-mm-yyyy' format. If not provided, defaults to today's date.
    save_to_excel : bool, default False
        If True, saves the resulting DataFrame as an Excel file in the current working directory.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing all columns returned by the IS Investment API, combined for all requested symbols.
    """
    if isinstance(symbols, str):
        symbols = [symbols]
    if not symbols:
        raise ValueError("At least one symbol must be provided.")
    if not start_date:
        raise ValueError("'start_date' is required in 'dd-mm-yyyy' format.")
    if end_date is None:
        end_date = datetime.now().strftime("%d-%m-%Y")

    data_frames = []
    for symbol in symbols:
        url = f"{BASE_URL}?hisse={symbol}&startdate={start_date}&enddate={end_date}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = pd.DataFrame(response.json().get("value", []))
        except Exception as e:
            print(f"[Warning] Could not fetch data for '{symbol}': {e}")
            continue
        if data.empty:
            print(f"[Info] No data found for symbol '{symbol}'.")
            continue

        data_frames.append(data)

    if not data_frames:
        raise ValueError("No data was fetched for any symbol. Please check the symbols and date ranges.")

    combined_data = pd.concat(data_frames, ignore_index=True)
    combined_data["HGDG_TARIH"] = pd.to_datetime(combined_data["HGDG_TARIH"], format="%d-%m-%Y").dt.strftime("%Y-%m-%d")
    combined_data["HGDG_TARIH"] = pd.to_datetime(combined_data["HGDG_TARIH"], format="%Y-%m-%d")
    combined_data = combined_data.sort_values(by=["HGDG_HS_KODU", "HGDG_TARIH"])
    combined_data = combined_data.reset_index(drop=True)

    if save_to_excel:
        file_name = f"stockdata_{datetime.now().strftime('%Y%m%d')}.xlsx"
        combined_data.to_excel(file_name, index=False)
        print(f"[Success] Data saved to '{file_name}'.")

    return combined_data