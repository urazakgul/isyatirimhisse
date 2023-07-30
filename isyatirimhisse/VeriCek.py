import requests
import pandas as pd
import numpy as np
from datetime import datetime
import os

def veri_cek(sembol=None, baslangic_tarih=None, bitis_tarih=None, frekans='1g', gozlem='son', getiri_hesapla=True, logaritmik_getiri=True, na_kaldir=True, excel_kaydet=False, excel_dosya_ismi=None):
    """
    Belirtilen tarih aralığında, belirtilen hisse senedi sembolleri için veri çeker. Çıktı özelleştirilebilir.

    Parametreler:
        sembol (str veya list, varsayılan None): Hisse senedi sembolü veya sembollerinin listesi.
        baslangic_tarih (str, 'GG-AA-YYYY', varsayılan None): Verilerin başlangıç tarihi (örn. '01-01-2023').
        bitis_tarih (str, 'GG-AA-YYYY', varsayılan None): Verilerin bitiş tarihi (örn. '25-07-2023').
            Eğer belirtilmezse, sistem tarihini (bugünkü tarihi) otomatik olarak kullanır.
        frekans (str, varsayılan '1g'): Veri frekansı (Günlük: '1g', Haftalık: '1h', Aylık: '1a', Yıllık: '1y').
        gozlem (str, varsayılan 'son'): Haftalık, aylık ve yıllık frekanslarda istenen gözlem ('son': Son, 'ortalama': Ortalama)
        getiri_hesapla (bool, varsayılan True): Getiri hesaplanacak mı?
        logaritmik_getiri (bool, varsayılan True): Logaritmik getiri mi hesaplanacak?
        na_kaldir (bool, varsayılan True): Eksik değerler kaldırılacak mı?
        excel_kaydet (bool, varsayılan False): pandas DataFrame Excel dosyasına kaydedilsin mi?
        excel_dosya_ismi (str, varsayılan None): Kaydedilecek Excel dosyasının ismi (örn. 'veriler.xlsx').
            Geçerli bir dosya adı belirtilmezse, varsayılan olarak 'veriler.xlsx' kullanılır.

    Dönen değer:
        pandas.DataFrame: İstenilen tarih aralığındaki hisse senedi verileri ve gerekirse getiri değerleri içeren DataFrame.
    """

    if not sembol or sembol is None:
        raise KeyError("Hisse senedi sembolü girilmedi. 'sembol' parametresi zorunludur.")

    if not baslangic_tarih or baslangic_tarih is None:
        raise KeyError("Başlangıç tarihi girilmedi. 'baslangic_tarih' parametresi zorunludur.")

    if not bitis_tarih or bitis_tarih is None:
        bitis_tarih = datetime.now().strftime('%d-%m-%Y')

    if not isinstance(sembol, list):
        sembol = [sembol]

    liste = []

    for s in sembol:
        url = f"https://www.isyatirim.com.tr/_layouts/15/Isyatirim.Website/Common/Data.aspx/HisseTekil?"
        url += f"hisse={s}&startdate={baslangic_tarih}&enddate={bitis_tarih}&frequency={frekans}.json"
        res = requests.get(url)
        if not res.status_code == 200:
            raise ConnectionError("Gönderdiğiniz istek İş Yatırım tarafından reddedildi.")
        result = res.json()
        historical = (
            pd.DataFrame(result['value'])
            .loc[:, ['HGDG_TARIH', 'HGDG_KAPANIS']]
            .rename(columns={'HGDG_TARIH': 'Tarih', 'HGDG_KAPANIS': f'{s}'})
        )
        liste.append(historical)

    df_final = liste[0]
    for i in range(1, len(liste)):
        df_final = pd.merge(df_final, liste[i], on='Tarih', how='outer')

    df_final['Tarih'] = pd.to_datetime(df_final['Tarih'], format='%d-%m-%Y').dt.strftime('%Y-%m-%d')
    df_final.dtypes
    df_final = df_final.set_index('Tarih')
    df_final.index = pd.to_datetime(df_final.index)

    if frekans == '1h':
        df_final = df_final.resample('W').last() if gozlem == 'son' else df_final.resample('W').mean()
    elif frekans == '1a':
        df_final = df_final.resample('M').last() if gozlem == 'son' else df_final.resample('M').mean()
    elif frekans == '1y':
        df_final = df_final.resample('Y').last() if gozlem == 'son' else df_final.resample('Y').mean()

    if getiri_hesapla:
        if logaritmik_getiri:
            df_final = df_final.apply(lambda x: np.log(x / x.shift(1)))
        else:
            df_final = df_final.apply(lambda x: x / x.shift(1) - 1)

    if na_kaldir:
        df_final = df_final.dropna()

    df_final = df_final.reset_index()

    if excel_kaydet:
        if not excel_dosya_ismi or excel_dosya_ismi is None:
            excel_bitis_tarih = datetime.now().strftime('%Y%m%d')
            excel_dosya_ismi = f'veriler_{excel_bitis_tarih}.xlsx'
        else:
            dosya_ismi, dosya_uzantisi = os.path.splitext(excel_dosya_ismi)
            if not dosya_uzantisi:
                excel_dosya_ismi += '.xlsx'
            i = 1
            while os.path.exists(excel_dosya_ismi):
                excel_dosya_ismi = f'{dosya_ismi}_{i}{dosya_uzantisi}'
                i += 1

        df_final.to_excel(excel_dosya_ismi, index=False)

    return df_final