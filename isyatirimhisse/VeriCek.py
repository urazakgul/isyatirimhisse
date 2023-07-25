import requests
import json
import pandas as pd
import numpy as np
from datetime import datetime

def veri_cek(sembol=None, baslangic_tarih=None, bitis_tarih=None, frekans='1g', gozlem='son', getiri_hesapla=True, logaritmik_getiri=True, na_kaldir=True):
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

    Dönen değer:
        pandas.DataFrame: İstenilen tarih aralığındaki hisse senedi verileri ve gerekirse getiri değerleri içeren DataFrame.
    """

    if sembol is None:
        raise KeyError("Hisse senedi sembolü girilmedi. 'sembol' parametresi zorunludur.")

    if baslangic_tarih is None:
        raise KeyError("Başlangıç tarihi girilmedi. 'baslangic_tarih' parametresi zorunludur.")

    if bitis_tarih is None:
        bitis_tarih = datetime.now().strftime('%d-%m-%Y')

    if not isinstance(sembol, list):
        sembol = [sembol]

    liste = []

    for s in sembol:
        url = f"https://www.isyatirim.com.tr/_layouts/15/Isyatirim.Website/Common/Data.aspx/HisseTekil?"
        url += f"hisse={s}&startdate={baslangic_tarih}&enddate={bitis_tarih}&frequency={frekans}.json"
        result = json.loads(requests.get(url).text)
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

    return df_final