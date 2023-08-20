import os
import requests
import pandas as pd
import numpy as np
from datetime import datetime
import asyncio
import aiohttp

async def fetch_data(symbol=None, stock_market_index=None, start_date=None, end_date=None, frequency='1d', observation='last', calculate_return=False, log_return=True, drop_na=True, save_to_excel=False, excel_file_name=None, language='en', exchange='TL'):

    column_labels = {
        'tr': {
            'date': 'Tarih'
        },
        'en': {
            'date': 'Date'
        }
    }

    error_messages = {
        'tr': {
            'symbol_smi': "'symbol' veya 'stock_market_index' parametrelerinden biri girilmelidir.",
            'start_date': "Başlangıç tarihi girilmedi. 'start_date' parametresi zorunludur.",
            'start_end_date': "Bitiş tarihi başlangıç tarihinden büyük veya başlangıç tarihine eşit olmalıdır.",
            'date_format': "Tarih formatı GG-AA-YYYY olmalıdır.",
            'exchange': "Geçersiz para birimi. Sadece 'TL' veya 'USD' girilmelidir.",
            'check_bool': "Bool değeri olarak girilmelidir.",
            'frequency' : "'frequency' parametresi '1d', '1w', '1m' veya '1y' olmalıdır.",
            'observation': "'observation' parametresi 'last' veya 'mean' olmalıdır.",
            'data': "Herhangi bir sembol için veri bulunamadı.",
            'response': "HTTP Hatası"
        },
        'en': {
            'symbol_smi': "One of the parameters 'symbol' or 'stock_market_index' must be entered.",
            'start_date': "Start period not provided. The 'start_date' parameter is mandatory.",
            'start_end_date': "End date must be greater than or equal to the start date.",
            'date_format': "Date format must be DD-MM-YYYY.",
            'exchange': "Invalid exchange. Only 'TL' or 'USD' must be entered.",
            'check_bool': "It must be entered as a bool value.",
            'frequency' : "The 'frequency' parameter must be '1d', '1w', '1m' or '1y'.",
            'observation': "The 'observation' parameter must be 'last' or 'mean'.",
            'data': "No data found for any symbol.",
            'response': "HTTP Error"
        }
    }

    if symbol is None and stock_market_index is None:
        raise KeyError(error_messages[language]['symbol_smi'])

    if symbol is not None:
        if not isinstance(symbol, list):
            symbol = [symbol]

    if stock_market_index is not None:
        if not isinstance(stock_market_index, list):
            stock_market_index = [stock_market_index]

    if start_date is None:
        raise KeyError(error_messages[language]['start_date'])

    if end_date is None:
        end_date = datetime.now().strftime('%d-%m-%Y')

    try:
        datetime.strptime(start_date, "%d-%m-%Y")
        datetime.strptime(end_date, "%d-%m-%Y")
    except ValueError:
        raise ValueError(error_messages[language]['date_format'])

    start_date_ = datetime.strptime(start_date, "%d-%m-%Y")
    end_date_ = datetime.strptime(end_date, "%d-%m-%Y")
    if end_date_ < start_date_:
        raise ValueError(error_messages[language]['start_end_date'])

    if not all(isinstance(var, bool) for var in [calculate_return, log_return, drop_na, save_to_excel]):
        raise ValueError(error_messages[language]['check_bool'])

    valid_frequencies = ["1d", "1w", "1m", "1y"]
    if frequency.lower() not in valid_frequencies:
        raise KeyError(error_messages[language]['frequency'])

    valid_observations = ["last", "mean"]
    if observation.lower() not in valid_observations:
        raise KeyError(error_messages[language]['observation'])

    if exchange.upper() == "TL":
        closing_column = 'HGDG_KAPANIS'
    elif exchange.upper() == "USD":
        closing_column = 'DOLAR_BAZLI_FIYAT'
    else:
        raise ValueError(error_messages[language]['exchange'])

    if language.lower() != "tr" and language.lower() != "en":
        raise KeyError("Geçersiz dil seçeneği. Sadece 'tr' veya 'en' girilmelidir./Invalid language. Only 'tr' or 'en' must be entered.")

    async def fetch_url(session, url):
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                raise ConnectionError(f"{error_messages[language]['response']}: {response.status}")

    if symbol is not None:

        symbol = symbol[:400]

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit_per_host=5)) as session:
            tasks = []
            for index, s in enumerate(symbol):
                url = f"https://www.isyatirim.com.tr/_layouts/15/Isyatirim.Website/Common/Data.aspx/HisseTekil?" \
                      f"hisse={s}&startdate={start_date}&enddate={end_date}.json"
                tasks.append(fetch_url(session, url))

            chunk_size = 5
            chunked_tasks = [tasks[i:i + chunk_size] for i in range(0, len(tasks), chunk_size)]
            results = []
            for chunk_tasks in chunked_tasks:
                chunk_results = await asyncio.gather(*chunk_tasks, return_exceptions=True)
                results.extend(chunk_results)

            symbol_data_list = []

            for index, result in enumerate(results):
                if isinstance(result, Exception):
                    continue
                if result and result['value']:
                    historical = (
                        pd.DataFrame(result['value'])
                        .loc[:, ['HGDG_TARIH', closing_column]]
                        .rename(columns={'HGDG_TARIH': column_labels[language]['date'], closing_column: f'{symbol[index]}'})
                    )
                    symbol_data_list.append(historical)

            if not symbol_data_list:
                raise ValueError(error_messages[language]['data'])

            df_symbol_final = symbol_data_list[0]
            for i in range(1, len(symbol_data_list)):
                df_symbol_final = pd.merge(df_symbol_final, symbol_data_list[i], on=column_labels[language]['date'], how='outer')
            df_symbol_final[column_labels[language]['date']] = pd.to_datetime(df_symbol_final[column_labels[language]['date']], format='%d-%m-%Y').dt.strftime('%Y-%m-%d')
            df_symbol_final = df_symbol_final.sort_values(by=column_labels[language]['date'])

    if stock_market_index is not None:
        smi_data_dict = {smi: [] for smi in stock_market_index}
        usdtry_historical = []

        smi_start_date = datetime.strptime(start_date, "%d-%m-%Y")
        smi_end_date = datetime.strptime(end_date, "%d-%m-%Y")

        current_year = smi_start_date.year
        end_year = smi_end_date.year

        while current_year <= end_year:
            year_start = datetime(current_year, 1, 1)
            year_end = datetime(current_year, 12, 31)

            formatted_start_date = year_start.strftime('%Y%m%d')
            formatted_end_date = year_end.strftime('%Y%m%d')

            if exchange == 'USD' and stock_market_index is not None:
                url = f"https://www.isyatirim.com.tr/_Layouts/15/IsYatirim.Website/Common/ChartData.aspx/IndexHistoricalAll?period=1440"
                url += f"&from={formatted_start_date}000000&to={formatted_end_date}235959&endeks={'USD/TRL'}"
                res = requests.get(url)
                if not res.status_code == 200:
                    raise ConnectionError(error_messages[language]['response'])
                result = res.json()
                if result['data']:
                    historical = (
                        pd.DataFrame(result['data'])
                        .rename(columns={0: column_labels[language]['date'], 1: 'USDTRY'})
                    )
                    historical[column_labels[language]['date']] = pd.to_datetime(historical[column_labels[language]['date']] / 1000, unit='s') + pd.to_timedelta(3, unit='h')
                    historical[column_labels[language]['date']] = historical[column_labels[language]['date']].dt.strftime('%Y-%m-%d')
                    usdtry_historical.append(historical)

            for smi in stock_market_index:
                url = f"https://www.isyatirim.com.tr/_Layouts/15/IsYatirim.Website/Common/ChartData.aspx/IndexHistoricalAll?period=1440"
                url += f"&from={formatted_start_date}000000&to={formatted_end_date}235959&endeks={smi}.I.BIST"
                res = requests.get(url)
                if not res.status_code == 200:
                    raise ConnectionError(error_messages[language]['response'])
                result = res.json()
                if result['data']:
                    historical = (
                        pd.DataFrame(result['data'])
                        .rename(columns={0: column_labels[language]['date'], 1: f'{smi}'})
                    )
                    historical[column_labels[language]['date']] = pd.to_datetime(historical[column_labels[language]['date']] / 1000, unit='s') + pd.to_timedelta(3, unit='h')
                    historical[column_labels[language]['date']] = historical[column_labels[language]['date']].dt.strftime('%Y-%m-%d')
                    smi_data_dict[smi].append(historical)

            current_year += 1

        if not all(data_list for data_list in smi_data_dict.values()):
            raise ValueError(error_messages[language]['data'])

        combined_data = []
        for smi, data_list in smi_data_dict.items():
            for data_frame in data_list:
                combined_data.append(data_frame)

        df_smi_final = pd.DataFrame()
        for df in combined_data:
            stock_index = df.columns[1]
            df['Stock_Index'] = stock_index
            df.rename(columns={df.columns[1]: 'Value'}, inplace=True)
            df_smi_final = pd.concat([df_smi_final, df], ignore_index=True)
        df_smi_final = df_smi_final.pivot_table(index=column_labels[language]['date'], columns='Stock_Index', values='Value')
        df_smi_final.columns.name = None
        df_smi_final = df_smi_final.reset_index()

    if exchange == 'USD' and stock_market_index is not None:
        df_usdtry_historical = pd.DataFrame()
        for usdtry_hist in usdtry_historical:
            df_usdtry_historical = pd.concat([df_usdtry_historical, usdtry_hist], ignore_index=True)
        df_smi_final = pd.merge(df_smi_final, df_usdtry_historical, on=column_labels[language]['date'], how='left')
        date_column = df_smi_final[column_labels[language]['date']]
        df_smi_final = df_smi_final.drop(column_labels[language]['date'], axis=1)
        usdtry_column = df_smi_final['USDTRY']
        df_smi_final = df_smi_final.drop(columns=['USDTRY'], axis=1)
        df_smi_final = df_smi_final.divide(usdtry_column, axis=0)
        df_smi_final.insert(0, column_labels[language]['date'], date_column)

    if symbol is not None and stock_market_index is None:
        df_final = df_symbol_final
        df_final[column_labels[language]['date']] = pd.to_datetime(df_final[column_labels[language]['date']])
        df_final= df_symbol_final.set_index(column_labels[language]['date'])
    elif symbol is None and stock_market_index is not None:
        df_final = df_smi_final
        df_final[column_labels[language]['date']] = pd.to_datetime(df_final[column_labels[language]['date']])
        df_final= df_smi_final.set_index(column_labels[language]['date'])
    else:
        df_final = pd.merge(df_symbol_final, df_smi_final, on=column_labels[language]['date'], how='outer')
        df_final[column_labels[language]['date']] = pd.to_datetime(df_final[column_labels[language]['date']])
        df_final= df_final.set_index(column_labels[language]['date'])

    df_final = df_final[(df_final.index <= pd.to_datetime(end_date, format='%d-%m-%Y')) & (df_final.index >= pd.to_datetime(start_date, format='%d-%m-%Y'))].sort_index()

    if frequency.lower() == '1w':
        df_final = df_final.resample('W').last() if observation == 'last' else df_final.resample('W').mean()
    elif frequency.lower() == '1m':
        df_final = df_final.resample('M').last() if observation == 'last' else df_final.resample('M').mean()
    elif frequency.lower() == '1y':
        df_final = df_final.resample('Y').last() if observation == 'last' else df_final.resample('Y').mean()

    if calculate_return:
        if log_return:
            df_final = df_final.apply(lambda x: np.log(x / x.shift(1)))
        else:
            df_final = df_final.apply(lambda x: x / x.shift(1) - 1)

    if drop_na:
        df_final = df_final.dropna()

    df_final = df_final.reset_index()

    if save_to_excel:
        if not excel_file_name or excel_file_name is None:
            excel_end_date = datetime.now().strftime('%Y%m%d')
            excel_file_name = f'data_{excel_end_date}.xlsx'
        else:
            file_name, file_extension = os.path.splitext(excel_file_name)
            if not file_extension:
                excel_file_name += '.xlsx'
            i = 1
            while os.path.exists(excel_file_name):
                excel_file_name = f'{file_name}_{i}{file_extension}'
                i += 1

        df_final.to_excel(excel_file_name, index=False)

    return df_final

def fetch_financials(symbol=None, start_year=None, end_year=None, exchange='TRY', financial_group='1', save_to_excel=False, excel_file_name=None, language='en'):

    file_names = {
        'tr': {
            'file_name': 'finansallar'
        },
        'en': {
            'file_name': 'financials'
        }
    }

    error_messages = {
        'tr': {
            'symbol': "Hisse senedi sembolü girilmedi. 'symbol' parametresi zorunludur.",
            'start_year': "Başlangıç yılı girilmedi. 'start_year' parametresi zorunludur.",
            'start_end_year': "Bitiş yılı başlangıç yılından büyük veya başlangıç yılına eşit olmalıdır.",
            'exchange': "Geçersiz para birimi. Sadece 'TL' veya 'USD' girilmelidir.",
            'financial_group': "Geçersiz finansal grup. 'financial_group' parametresi '1', '2' veya '3' girilmelidir.",
            'check_bool': "Bool değeri olarak girilmelidir.",
            'response': "Gönderdiğiniz istek İş Yatırım tarafından reddedildi.",
            'data': "Herhangi bir sembol için veri bulunamadı."
        },
        'en': {
            'symbol': "Stock symbol not provided. The 'symbol' parameter is mandatory.",
            'start_year': "Start year not provided. The 'start_year' parameter is mandatory.",
            'start_end_year': "End year must be greater than or equal to the start year.",
            'exchange': "Invalid exchange. Only 'TL' or 'USD' must be entered.",
            'financial_group': "Invalid financial group. The 'financial_group' parameter '1', '2' or '3' must be entered.",
            'check_bool': "It must be entered as a bool value.",
            'response': "The request you sent has been rejected by IS Investment.",
            'data': "No data found for any symbol."
        }
    }

    if not symbol or symbol is None:
        raise KeyError(error_messages[language]['symbol'])

    if not isinstance(symbol, list):
        symbol = [symbol]

    if not start_year or start_year is None:
        raise KeyError(error_messages[language]['start_year'])

    if not end_year or end_year is None:
        end_year = pd.Timestamp.now().year

    if not all(isinstance(var, bool) for var in [save_to_excel]):
        raise ValueError(error_messages[language]['check_bool'])

    if exchange.upper() != "TRY" and exchange.upper() != "USD":
        raise ValueError(error_messages[language]['exchange'])

    if language.lower() != "tr" and language.lower() != "en":
        raise KeyError("Geçersiz dil seçeneği. Sadece 'tr' veya 'en' girilmelidir./Invalid language. Only 'tr' or 'en' must be entered.")

    start_year = int(start_year)
    end_year = int(end_year)

    if end_year < start_year:
        raise ValueError(error_messages[language]['start_end_year'])

    if financial_group == '1':
        financial_group = 'XI_29'
    elif financial_group == '2':
        financial_group = 'UFRS'
    elif financial_group == '3':
        financial_group = 'UFRS_K'
    else:
        raise ValueError(error_messages[language]['financial_group'])

    base_url = "https://www.isyatirim.com.tr/_layouts/15/IsYatirim.Website/Common/Data.aspx/MaliTablo"

    periods = [3,6,9,12]

    data_dict = {}

    for sym in symbol:
        urls = []
        for year in range(start_year, end_year + 1):
            parameters = {
                "companyCode": sym,
                "exchange": exchange,
                "financialGroup": financial_group,
                "year1": year,
                "period1": periods[0],
                "year2": year,
                "period2": periods[1],
                "year3": year,
                "period3": periods[2],
                "year4": year,
                "period4": periods[3]
            }
            url = base_url + '?' + '&'.join(f"{key}={value}" for key, value in parameters.items())
            urls.append(url)

        data_list = []

        quarters = [f"{year}/{month}" for year in range(start_year, end_year + 1) for month in periods]

        for url in urls:
            res = requests.get(url)
            if not res.status_code == 200:
                raise ConnectionError(error_messages[language]['response'])
            result = res.json()
            if result['value']:
                result_value = pd.DataFrame(result['value'])
                itemDesc = 'itemDescEng' if language == 'tr' else 'itemDescTr'
                columns_to_drop = [col for col in result_value.columns if itemDesc in col]
                result_value = result_value.drop(columns=columns_to_drop)
                result_value.columns = result_value.columns[:2].tolist() + quarters[:4]
                quarters = quarters[4:]
                data_list.append(result_value)
            else:
                quarters = quarters[4:]

        if data_list:
            df_final = data_list[0]
            for i in range(1, len(data_list)):
                df_final = pd.merge(df_final, data_list[i], on=['itemCode'], how='outer', suffixes=('', f'_{i}'))

            item_columns = [col for col in df_final.columns if col.startswith('itemDesc')]
            header = 'itemDescEng_main' if language == 'en' else 'itemDescTr_main'
            df_final[header] = df_final[df_final.columns[df_final.columns.str.startswith('itemDesc')]].apply(lambda row: ''.join(set(row.dropna())), axis=1)
            df_final = df_final.drop(item_columns, axis=1)
            nulls_to_drop = df_final.columns[df_final.isnull().all()]
            df_final = df_final.drop(columns=nulls_to_drop)
            last_column = df_final.columns[-1]
            itemCode_index = df_final.columns.get_loc('itemCode')
            cols = list(df_final.columns)
            cols.pop(cols.index(last_column))
            cols.insert(itemCode_index + 1, last_column)
            df_final = df_final[cols]
            df_final.columns.values[0] = "Kod" if language == 'tr' else 'Code'
            df_final.columns.values[1] = sym
            df_final[sym] = df_final[sym].str.strip()

            data_dict[sym] = df_final

            if save_to_excel:
                if not excel_file_name or excel_file_name is None:
                    excel_end_date = datetime.now().strftime('%Y%m%d')
                    excel_file_name_ = f"{file_names[language]['file_name']}_{sym}_{excel_end_date}.xlsx"
                else:
                    file_name, file_extension = os.path.splitext(excel_file_name)
                    if not file_extension:
                        excel_file_name_ = excel_file_name + '.xlsx'
                    excel_file_name_ = f'{file_name}.{file_extension}'

                df_final.to_excel(excel_file_name_, index=False)

    if not data_dict:
        raise ValueError(error_messages[language]['data'])

    return data_dict