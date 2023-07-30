import sys
import os
import pandas as pd

tests_directory = os.path.dirname(os.path.abspath(__file__))
isyatirimanaliz_directory = os.path.abspath(os.path.join(tests_directory, '..'))
if os.path.exists(isyatirimanaliz_directory):
    sys.path.insert(0, isyatirimanaliz_directory)
    print(sys.path)
else:
    print(f"The directory '{isyatirimanaliz_directory}' does not exist.")

from isyatirimhisse import veri_cek

def test_veri_cek():
    # Test senaryosu 1: Tek hisse, günlük frekans ve logaritmik getiri
    sembol = 'AKBNK'
    baslangic_tarih = '03-01-2023'
    bitis_tarih = '21-07-2023'
    frekans = '1g'
    gozlem = 'son'
    getiri_hesapla = True
    logaritmik_getiri = True
    na_kaldir = True
    excel_kaydet = True

    veriler = veri_cek(
        sembol=sembol,
        baslangic_tarih=baslangic_tarih,
        bitis_tarih=bitis_tarih,
        frekans=frekans,
        gozlem=gozlem,
        getiri_hesapla=getiri_hesapla,
        logaritmik_getiri=logaritmik_getiri,
        na_kaldir=na_kaldir,
        excel_kaydet=excel_kaydet
    )

    assert isinstance(veriler, pd.DataFrame), "Veri çekme fonksiyonu DataFrame dönmeli."
    assert len(veriler) > 0, "Veri çekme fonksiyonu boş DataFrame döndü."

    # Test senaryosu 2: Bitiş tarihi yok

    sembol = 'AKBNK'
    baslangic_tarih = '03-01-2023'
    frekans = '1g'
    gozlem = 'son'
    getiri_hesapla = True
    logaritmik_getiri = True
    na_kaldir = True
    excel_kaydet = True
    excel_dosya_ismi = 'test_veri.xlsx'

    veriler = veri_cek(
        sembol=sembol,
        baslangic_tarih=baslangic_tarih,
        frekans=frekans,
        gozlem=gozlem,
        getiri_hesapla=getiri_hesapla,
        logaritmik_getiri=logaritmik_getiri,
        na_kaldir=na_kaldir,
        excel_kaydet=excel_kaydet,
        excel_dosya_ismi=excel_dosya_ismi
    )

    assert isinstance(veriler, pd.DataFrame), "Veri çekme fonksiyonu DataFrame dönmeli."
    assert len(veriler) > 0, "Veri çekme fonksiyonu boş DataFrame döndü."
    assert os.path.exists(excel_dosya_ismi), "Excel dosyası kaydedilmedi."

    # Test senaryosu 3: Birden fazla hisse, haftalık frekans, basit getiri ve NA kaldır
    sembol = ['AKBNK', 'EUPWR']
    baslangic_tarih = '03-01-2023'
    bitis_tarih = '21-07-2023'
    frekans = '1h'
    gozlem = 'son'
    getiri_hesapla = True
    logaritmik_getiri = False
    na_kaldir = True
    excel_kaydet = True
    excel_dosya_ismi = 'test_veri.xlsx'

    veriler = veri_cek(
        sembol=sembol,
        baslangic_tarih=baslangic_tarih,
        bitis_tarih=bitis_tarih,
        frekans=frekans,
        gozlem=gozlem,
        getiri_hesapla=getiri_hesapla,
        logaritmik_getiri=logaritmik_getiri,
        na_kaldir=na_kaldir,
        excel_kaydet=excel_kaydet,
        excel_dosya_ismi=excel_dosya_ismi
    )

    assert isinstance(veriler, pd.DataFrame), "Veri çekme fonksiyonu DataFrame dönmeli."
    assert len(veriler) > 0, "Veri çekme fonksiyonu boş DataFrame döndü."
    assert os.path.exists(excel_dosya_ismi), "Excel dosyası kaydedilmedi."

    # Test senaryosu 4: Birden fazla hisse, aylık frekans, kapanış fiyatı ve NA bırak
    sembol = ['AKBNK', 'EUPWR']
    baslangic_tarih = '03-01-2023'
    bitis_tarih = '21-07-2023'
    frekans = '1a'
    gozlem = 'son'
    getiri_hesapla = False
    logaritmik_getiri = True
    na_kaldir = False
    excel_kaydet = True
    excel_dosya_ismi = 'test_veri.xlsx'

    veriler = veri_cek(
        sembol=sembol,
        baslangic_tarih=baslangic_tarih,
        bitis_tarih=bitis_tarih,
        frekans=frekans,
        gozlem=gozlem,
        getiri_hesapla=getiri_hesapla,
        logaritmik_getiri=logaritmik_getiri,
        na_kaldir=na_kaldir,
        excel_kaydet=excel_kaydet,
        excel_dosya_ismi=excel_dosya_ismi
    )

    assert isinstance(veriler, pd.DataFrame), "Veri çekme fonksiyonu DataFrame dönmeli."
    assert len(veriler) > 0, "Veri çekme fonksiyonu boş DataFrame döndü."
    assert os.path.exists(excel_dosya_ismi), "Excel dosyası kaydedilmedi."

    # Test senaryosu 5: Birden fazla hisse, yıllık frekans, kapanış fiyatları, ortalama fiyatlar ve NA kaldır
    sembol = ['AKBNK', 'EUPWR']
    baslangic_tarih = '03-01-2023'
    bitis_tarih = '21-07-2023'
    frekans = '1y'
    gozlem = 'ortalama'
    getiri_hesapla = False
    logaritmik_getiri = True
    na_kaldir = True

    veriler = veri_cek(
        sembol=sembol,
        baslangic_tarih=baslangic_tarih,
        bitis_tarih=bitis_tarih,
        frekans=frekans,
        gozlem=gozlem,
        getiri_hesapla=getiri_hesapla,
        logaritmik_getiri=logaritmik_getiri,
        na_kaldir=na_kaldir
    )

    assert isinstance(veriler, pd.DataFrame), "Veri çekme fonksiyonu DataFrame dönmeli."
    assert len(veriler) > 0, "Veri çekme fonksiyonu boş DataFrame döndü."

test_veri_cek()