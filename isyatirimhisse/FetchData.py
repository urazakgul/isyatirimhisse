import os
import requests
import pandas as pd
import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def date_conversion_decorator(func):
    def wrapper(symbol=None, start_period=None, end_period=None, save_to_excel=False, language='en'):
        if start_period:
            start_date = datetime.strptime(start_period, '%Y/%m')
        else:
            start_date = None
        
        if end_period:
            end_date = datetime.strptime(end_period, '%Y/%m')
        else:
            end_date = None
        
        return func(symbol, start_date, end_date, save_to_excel, language)
    
    return wrapper


def fetch_data(symbol=None, start_date=None, end_date=None, frequency='1d', observation='last', calculate_return=False, log_return=True, drop_na=True, save_to_excel=False, excel_file_name=None, language='en', currency='TL'):

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
            'symbol': "Hisse senedi sembolü girilmedi. 'symbol' parametresi zorunludur.",
            'start_date': "Başlangıç tarihi girilmedi. 'start_date' parametresi zorunludur.",
            'response': "Gönderdiğiniz istek İş Yatırım tarafından reddedildi.",
            'currency': "Geçersiz para birimi. Sadece 'TL' veya 'USD' girilmelidir.",
            'check_bool': "'calculate_return', 'log_return', 'drop_na', 'save_to_excel' argümanları sadece bool türünde olmalıdır."
        },
        'en': {
            'symbol': "Stock symbol not provided. The 'symbol' parameter is mandatory.",
            'start_date': "Start period not provided. The 'start_date' parameter is mandatory.",
            'response': "The request you sent has been rejected by IS Investment.",
            'currency': "Invalid currency. Only 'TL' or 'USD' must be entered.",
            'check_bool': "The arguments 'calculate_return', 'log_return', 'drop_na', and 'save_to_excel' must be of boolean type."
        }
    }

    if not symbol or symbol is None:
        raise KeyError(error_messages[language]['symbol'])

    if not start_date or start_date is None:
        raise KeyError(error_messages[language]['start_date'])

    if not end_date or end_date is None:
        end_date = datetime.now().strftime('%d-%m-%Y')

    if not isinstance(symbol, list):
        symbol = [symbol]

    if not all(isinstance(var, bool) for var in [calculate_return, log_return, drop_na, save_to_excel]):
        raise ValueError(error_messages[language]['check_bool'])

    if currency.upper() == "TL":
        closing_column = 'HGDG_KAPANIS'
    elif currency.upper() == "USD":
        closing_column = 'DOLAR_BAZLI_FIYAT'
    else:
        raise ValueError(error_messages[language]['currency'])

    data_list = []

    for s in symbol:
        url = f"https://www.isyatirim.com.tr/_layouts/15/Isyatirim.Website/Common/Data.aspx/HisseTekil?"
        url += f"hisse={s}&startdate={start_date}&enddate={end_date}.json"
        res = requests.get(url)
        if not res.status_code == 200:
            raise ConnectionError(error_messages[language]['response'])
        result = res.json()
        if result['value']:
            historical = (
                pd.DataFrame(result['value'])
                .loc[:, ['HGDG_TARIH', closing_column]]
                .rename(columns={'HGDG_TARIH': column_labels[language]['date'], closing_column: f'{s}'})
            )
            data_list.append(historical)

    if not data_list:
        raise ValueError("No stock data found for any symbol.")

    df_final = data_list[0]
    for i in range(1, len(data_list)):
        df_final = pd.merge(df_final, data_list[i], on=column_labels[language]['date'], how='outer')

    df_final[column_labels[language]['date']] = pd.to_datetime(df_final[column_labels[language]['date']], format='%d-%m-%Y').dt.strftime('%Y-%m-%d')
    df_final.dtypes
    df_final = df_final.set_index(column_labels[language]['date'])
    df_final.index = pd.to_datetime(df_final.index)

    if frequency == '1w':
        df_final = df_final.resample('W').last() if observation == 'last' else df_final.resample('W').mean()
    elif frequency == '1m':
        df_final = df_final.resample('M').last() if observation == 'last' else df_final.resample('M').mean()
    elif frequency == '1y':
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

@date_conversion_decorator
def fetch_financials(symbol=None, start_period=None, end_period=None, save_to_excel=False, language='en'):

    translations_tr = {
        'Bilanço': 'Bilanço',
        'Gelir Tablosu': 'Gelir Tablosu',
        'Dipnot': 'Dipnot',
        'Nakit Akım Tablosu': 'Nakit Akım Tablosu',
        'MaliTabloTuru': 'MaliTabloTuru',
        'bilanco': 'Bilanco',
        'gelir_tablosu': 'GelirTablosu',
        'dipnot': 'Dipnot',
        'nakit_akim_tablosu': 'NakitAkimTablosu',
        'bilanco_dosya': 'bilanco',
        'gelir_tablosu_dosya': 'gelir_tablosu',
        'dipnot_dosya': 'dipnot',
        'nakit_akim_tablosu_dosya': 'nakit_akim_tablosu',
    }

    translations_en = {
        'Bilanço': 'Balance Sheet',
        'Gelir Tablosu': 'Income Statement',
        'Dipnot': 'Footnote',
        'Nakit Akım Tablosu': 'Cash Flow Statement',
        'MaliTabloTuru': 'FinancialStatementType',
        'bilanco': 'BalanceSheet',
        'gelir_tablosu': 'IncomeStatement',
        'dipnot': 'Footnote',
        'nakit_akim_tablosu': 'CashFlowStatement',
        'bilanco_dosya': 'balance_sheet',
        'gelir_tablosu_dosya': 'income_statement',
        'dipnot_dosya': 'footnote',
        'nakit_akim_tablosu_dosya': 'cash_flow_statement',
    }

    translations = translations_tr if language == 'tr' else translations_en

    error_messages = {
        'tr': {
            'symbol': "Hisse senedi sembolü girilmedi. 'symbol' parametresi zorunludur.",
            'start_period': "Başlangıç dönemi girilmedi. 'start_period' parametresi zorunludur.",
            'end_period': "Bitiş dönemi girilmedi. 'end_period' parametresi zorunludur.",
            'desired_date': "Mümkün olan son dönemden daha büyük bir dönem girilmemelidir.",
            'check_bool': "'save_to_excel' argümanı sadece bool türünde olmalıdır."
        },
        'en': {
            'symbol': "Stock symbol not provided. The 'symbol' parameter is mandatory.",
            'start_period': "Start period not provided. The 'start_period' parameter is mandatory.",
            'end_period': "End period not provided. The 'end_period' parameter is mandatory.",
            'desired_date': "No period larger than the last possible period must be entered.",
            'check_bool': "The argument 'save_to_excel' must be of boolean type."
        }
    }

    if not symbol or symbol is None:
        raise KeyError(error_messages[language]['symbol'])

    if not start_period or start_period is None:
        raise KeyError(error_messages[language]['start_period'])

    if not end_period or end_period is None:
        raise KeyError(error_messages[language]['end_period'])

    if not all(isinstance(var, bool) for var in [save_to_excel]):
        raise ValueError(error_messages[language]['check_bool'])

    chrome_options = Options()
    chrome_options.add_argument('--headless=new')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    if isinstance(symbol, str):
        symbol = [symbol]

    data_dict = {}

    for sym in symbol:
        url = f'https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={sym}'
        driver.get(url)
        financial_statements_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Mali Tablolar')]"))
        )
        financial_statements_tab.click()

        desired_dates = []
        while start_period <= end_period:
            quarter = (start_period.month - 1) // 3 + 1
            desired_dates.append(datetime(start_period.year, quarter * 3, 1).date())
            start_period += relativedelta(months=3)

        first_select_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@id='select2-ddlMaliTabloDonem1-container']"))
        )
        latest_period = first_select_box.get_attribute("title")
        latest_period_date = datetime.strptime(latest_period, "%Y/%m").date()
        desired_dates = [date_obj for date_obj in desired_dates if date_obj <= latest_period_date]
        desired_dates_str = [f"{date_obj.year}/{date_obj.month}" for date_obj in desired_dates]

        data_combined_dict = {}

        for date in desired_dates_str:
            select_box = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//span[@id='select2-ddlMaliTabloDonem1-container']"))
            )
            driver.execute_script("arguments[0].scrollIntoView();", select_box)
            select_box.click()
            select_box_item = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[contains(@id, 'select2-ddlMaliTabloDonem1') and .//text()='{date}']"))
            )
            select_box_item.click()

            page_source = driver.page_source

            soup = BeautifulSoup(page_source, 'html.parser')
            table = soup.select_one('table.excelexport[data-csvname="malitablo"]')

            if table:
                rows = table.find_all('tr')
                if len(rows) > 1:
                    data = []
                    for row in rows[1:]:
                        columns = row.find_all('td')
                        row_data = [column.text.strip() for column in columns]
                        data.append(row_data)
                    data_final = pd.DataFrame(data)

                    data_combined_temp = data_final.iloc[:, [0, 1]]
                    data_combined_temp.columns = ['Type', date]

                    for index, row in data_combined_temp.iterrows():
                        typ = row['Type']
                        if typ not in data_combined_dict:
                            data_combined_dict[typ] = {'Type': typ}
                        data_combined_dict[typ][date] = row[date]

        data_combined_list = list(data_combined_dict.values())
        data_combined = pd.DataFrame(data_combined_list)

        for col in data_combined.columns[1:]:
            data_combined[col] = data_combined[col].str.replace('.', '', regex=False)
            data_combined[col] = pd.to_numeric(data_combined[col])

        data_combined['FinancialStatementType'] = data_combined['Type'].apply(lambda x: translations.get(x, None))
        data_combined['FinancialStatementType'] = data_combined['FinancialStatementType'].fillna(method='ffill')

        balance_sheet = data_combined[data_combined['FinancialStatementType'] == translations['Bilanço']].drop(columns=['FinancialStatementType']).rename(columns={'Type': translations['bilanco']}).iloc[1:]
        income_statement = data_combined[data_combined['FinancialStatementType'] == translations['Gelir Tablosu']].drop(columns=['FinancialStatementType']).rename(columns={'Type': translations['gelir_tablosu']}).iloc[1:]
        footnote = data_combined[data_combined['FinancialStatementType'] == translations['Dipnot']].drop(columns=['FinancialStatementType']).rename(columns={'Type': translations['dipnot']}).iloc[1:]
        cash_flow_statement = data_combined[data_combined['FinancialStatementType'] == translations['Nakit Akım Tablosu']].drop(columns=['FinancialStatementType']).rename(columns={'Type': translations['nakit_akim_tablosu']}).iloc[1:]


        if save_to_excel:
            balance_sheet_filename = f'{translations["bilanco_dosya"]}_{{sym}}.xlsx'
            income_statement_filename = f'{translations["gelir_tablosu_dosya"]}_{{sym}}.xlsx'
            footnote_filename = f'{translations["dipnot_dosya"]}_{{sym}}.xlsx'
            cash_flow_statement_filename = f'{translations["nakit_akim_tablosu_dosya"]}_{{sym}}.xlsx'

            balance_sheet.to_excel(balance_sheet_filename.format(sym=sym), index=False)
            income_statement.to_excel(income_statement_filename.format(sym=sym), index=False)
            footnote.to_excel(footnote_filename.format(sym=sym), index=False)
            cash_flow_statement.to_excel(cash_flow_statement_filename.format(sym=sym), index=False)

        data_dict[sym] = {
            translations['bilanco_dosya']: balance_sheet,
            translations['gelir_tablosu_dosya']: income_statement,
            translations['dipnot_dosya']: footnote,
            translations['nakit_akim_tablosu_dosya']: cash_flow_statement
        }

    driver.quit()

    return data_dict
