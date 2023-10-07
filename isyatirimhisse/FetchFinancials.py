import pandas as pd
import requests
from datetime import datetime

class Financials:
    BASE_URL = "https://www.isyatirim.com.tr/_layouts/15/IsYatirim.Website/Common/Data.aspx/MaliTablo"

    def __init__(self):
        pass

    def get_data(
            self,
            symbols: list = None,
            start_year: str = None,
            end_year: str = None,
            exchange: str = 'TRY',
            financial_group: str = '1',
            save_to_excel: bool = False
    ) -> dict:
        """
        Get financials from the IS Investment.

        :param symbols: List of stock symbols.
        :param start_year: Start year for the data.
        :param end_year: End year for the data.
        :param exchange: Currency exchange type ('TRY' or 'USD').
        :param financial_group: Financial group identifier ('1', '2', or '3').
        :param save_to_excel: Whether to save data to an Excel file.

        :return: Dictionary containing financial statements for each symbol.
        """
        if not symbols or symbols is None:
            raise ValueError("The 'symbols' parameter is required.")

        if not isinstance(symbols, list):
            symbols = [symbols]

        if not start_year or start_year is None:
            start_year = datetime.now().year - 2
        else:
            start_year = int(start_year)

        if not end_year or end_year is None:
            end_year = datetime.now().year
        else:
            end_year = int(end_year)

        if end_year < start_year:
            raise ValueError("The end_year must be greater than or equal to the start_year.")

        if exchange.upper() not in ['TRY', 'USD']:
            raise ValueError("Invalid currency exchange. Exchange currency must be either 'TRY' (Turkish Lira) or 'USD' (US Dollar) only.")

        if financial_group not in ['1', '2', '3']:
            raise ValueError("Invalid financial group. The 'financial_group' parameter must be '1' for XI_29, '2' for UFRS, or '3' for UFRS_K.")

        if financial_group == '1':
            financial_group = 'XI_29'
        elif financial_group == '2':
            financial_group = 'UFRS'
        elif financial_group == '3':
            financial_group = 'UFRS_K'

        periods = [3, 6, 9, 12]
        data_dict = {}

        for symbol in symbols:
            urls = []
            for year in range(start_year, end_year + 1):
                parameters = {
                    "companyCode": symbol,
                    "exchange": exchange,
                    "financialGroup": f'{financial_group}',
                    "year1": year,
                    "period1": periods[0],
                    "year2": year,
                    "period2": periods[1],
                    "year3": year,
                    "period3": periods[2],
                    "year4": year,
                    "period4": periods[3]
                }
                url = f"{self.BASE_URL}?{'&'.join(f'{key}={value}' for key, value in parameters.items())}"
                urls.append(url)

            data_list = []
            quarters = [f"{year}/{month}" for year in range(start_year, end_year + 1) for month in periods]

            for url in urls:
                res = requests.get(url)
                if res.status_code != 200:
                    raise ConnectionError(f"HTTP Status Code: {res.status_code}")
                result = res.json()
                if result.get('value'):
                    result_value = pd.DataFrame(result['value'])
                    result_value.columns = result_value.columns[:3].tolist() + quarters[:4]
                    quarters = quarters[4:]
                    data_list.append(result_value)
                else:
                    quarters = quarters[4:]

            if data_list:
                df_final = data_list[0]
                for i in range(1, len(data_list)):
                    df_final = pd.merge(
                        df_final, data_list[i],
                        on=['itemCode', 'itemDescTr', 'itemDescEng'],
                        how='outer', suffixes=('', f'_{i}')
                    )

                null_columns = df_final.columns[df_final.isnull().all()]
                df_final = df_final.drop(columns=null_columns)
                df_final[['itemCode', 'itemDescTr', 'itemDescEng']] = df_final[['itemCode', 'itemDescTr', 'itemDescEng']].apply(lambda x: x.str.strip())

                data_dict[symbol] = df_final

            else:
                print(f"No data found for {symbol}. You may need to change the financial_group parameter.")

        if save_to_excel:
            current_datetime = datetime.now().strftime("%Y%m%d")
            writer = pd.ExcelWriter(f"financials_{current_datetime}.xlsx", engine='openpyxl')
            for symbol, df in data_dict.items():
                df.to_excel(writer, sheet_name=symbol, index=False)
            writer.close()
            print(f"Data saved to financials_{current_datetime}")

        return data_dict if data_dict else {}