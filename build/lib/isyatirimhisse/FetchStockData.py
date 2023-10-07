import requests
import pandas as pd
import numpy as np
from datetime import datetime

class StockData:
    BASE_URL = "https://www.isyatirim.com.tr/_layouts/15/Isyatirim.Website/Common/Data.aspx/HisseTekil"
    COLUMN_MAPPING = {
        'HGDG_HS_KODU':'CODE',
        'HGDG_TARIH':'DATE',
        'HGDG_KAPANIS':'CLOSING_TL',
        'HGDG_MIN':'LOW_TL',
        'HGDG_MAX':'HIGH_TL',
        'HGDG_HACIM':'VOLUME_TL',
        'DOLAR_BAZLI_FIYAT':'CLOSING_USD',
        'DOLAR_BAZLI_MIN':'LOW_USD',
        'DOLAR_BAZLI_MAX':'HIGH_USD',
        'DOLAR_HACIM':'VOLUME_USD',
        'END_DEGER':'XU100_TL',
    }
    SELECTED_COLUMNS = [
        'HGDG_HS_KODU',
        'HGDG_TARIH',
        'HGDG_KAPANIS',
        'HGDG_MIN',
        'HGDG_MAX',
        'HGDG_HACIM',
        'DOLAR_BAZLI_FIYAT',
        'DOLAR_BAZLI_MIN',
        'DOLAR_BAZLI_MAX',
        'DOLAR_HACIM',
        'END_DEGER',
    ]

    def __init__(self):
        pass

    def get_data(
            self,
            symbols: list = None,
            start_date: str = None,
            end_date: str = None,
            exchange: str = '2',
            frequency: str = '1d',
            observation: str = 'last',
            return_type: str = '0',
            save_to_excel: bool = False
    ) -> pd.DataFrame:

        """
        Get stock data from the IS Investment.

        :param symbols: List of stock symbols.
        :param start_date: Start date in 'dd-mm-yyyy' format.
        :param end_date: End date in 'dd-mm-yyyy' format.
        :param exchange: Exchange type ('0' for TL columns, '1' for USD columns, '2' for both TL and USD columns).
        :param frequency: Data frequency ('1d', '1w', '1mo', '3mo', '1y').
        :param observation: Data observation type ('last', 'mean').
        :param return_type: Return type ('0' for no transformation, '1' for log returns, '2' for simple returns).
        :param save_to_excel: Whether to save data to an Excel file.

        :return: Pandas DataFrame containing stock data.
        """

        if not symbols or symbols is None:
            raise ValueError("Please ensure you have provided at least one symbol.")

        if not isinstance(symbols, list):
            symbols = [symbols]

        if not start_date or start_date is None:
            raise ValueError("Please ensure you have provided a start date in the 'dd-mm-yyyy' format.")

        if not end_date or end_date is None:
            end_date = datetime.now().strftime("%d-%m-%Y")

        if exchange not in ['0', '1', '2']:
            raise ValueError("Invalid exchange value. The options are '0' for TL columns, '1' for USD columns, or '2' for both TL and USD columns.")

        if frequency not in ['1d', '1w', '1mo', '3mo', '1y']:
            raise ValueError("Invalid frequency value. The options are '1d', '1w', '1mo', '3mo', or '1y'.")

        if observation not in ['last', 'mean']:
            raise ValueError("Invalid observation value. The options are 'last' or 'mean'.")

        if return_type not in ['0', '1', '2']:
            raise ValueError("Invalid return type value. The options are '0' for no transformation, '1' for log returns, or '2' for simple returns.")

        if not isinstance(save_to_excel, bool):
            raise ValueError("The save_to_excel parameter must have a boolean value.")

        data_frames = []

        for symbol in symbols:
            url = f"{self.BASE_URL}?hisse={symbol}&startdate={start_date}&enddate={end_date}.json"

            response = requests.get(url)
            if response.status_code == 200:
                data = pd.DataFrame(response.json()['value'])
                if not data.empty:
                    data = data[self.SELECTED_COLUMNS]
                    data = data.rename(columns=self.COLUMN_MAPPING)
                    data['XU100_USD'] = data['XU100_TL'] / (data['CLOSING_TL'] / data['CLOSING_USD'])

                    if exchange == '0':
                        selected_columns = ['CODE', 'DATE'] + [col for col in data.columns if "_TL" in col]
                    elif exchange == '1':
                        selected_columns = ['CODE', 'DATE'] + [col for col in data.columns if "_USD" in col]
                    else:
                        selected_columns = list(self.COLUMN_MAPPING.values())
                        selected_columns.append('XU100_USD')

                    data = data[selected_columns]
                    data['DATE'] = pd.to_datetime(data['DATE'], format='%d-%m-%Y')

                    data = data.set_index('DATE')
                    data = data.drop(columns='CODE')

                    if frequency == '1d':
                        data_observed = data
                    elif frequency == '1w':
                        data_observed = data.resample('W').last() if observation == 'last' else data.resample('W').mean()
                    elif frequency == '1mo':
                        data_observed = data.resample('M').last() if observation == 'last' else data.resample('M').mean()
                    elif frequency == '3mo':
                        data_observed = data.resample('3M').last() if observation == 'last' else data.resample('3M').mean()
                    elif frequency == '1y':
                        data_observed = data.resample('Y').last() if observation == 'last' else data.resample('Y').mean()

                    data_observed = data_observed.reset_index()
                    data_observed['CODE'] = symbol

                    if return_type == '1':
                        returns_data = data_observed.copy()
                        columns_to_exclude = ['DATE', 'CODE']
                        for column in data_observed.columns:
                            if column not in columns_to_exclude:
                                returns_data[column] = np.log(data_observed[column] / data_observed[column].shift(1))
                        data_observed = returns_data.dropna()
                    elif return_type == '2':
                        returns_data = data_observed.copy()
                        columns_to_exclude = ['DATE', 'CODE']
                        for column in data_observed.columns:
                            if column not in columns_to_exclude:
                                returns_data[column] = (data_observed[column] - data_observed[column].shift(1)) / data_observed[column].shift(1)
                        data_observed = returns_data.dropna()

                    data_frames.append(data_observed)
            else:
                raise ValueError(f"HTTP Status Code: {response.status_code}")

        if data_frames:
            combined_data = pd.concat(data_frames, ignore_index=True)
            combined_data['DATE'] = combined_data['DATE'].dt.date

            if save_to_excel:
                current_datetime = datetime.now().strftime("%Y%m%d")
                excel_file_name = f"stockdata_{current_datetime}.xlsx"
                combined_data.to_excel(excel_file_name, index=False)
                print(f"Data saved to {excel_file_name}")

            return combined_data
        else:
            return None