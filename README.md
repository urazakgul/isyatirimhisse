# isyatirimhisse v0.2.0

## Aciklama

`isyatirimhisse`, Is Yatirim'in web sitesinden veri cekme islemlerini kolaylastirmak amaciyla gelistirilmis, istege gore ozellestirilebilir bir Python kutuphanesidir.

*** UYARI ***

`isyatirimhisse`, resmi Is Yatirim Menkul Degerler A.S. kutuphanesi degildir ve sirket tarafindan dogrulanmamistir. Kullanicilar, bu kutuphaneyi kullanmadan once ilgili tum verilere erisim icin Is Yatirim Menkul Degerler A.S. kullanim kosullarini ve haklarini incelemelidir. `isyatirimhisse` kutuphanesi, yalnizca kisisel kullanim amaclari icin tasarlanmistir.

## Kurulum

Kutuphaneyi kullanmak icin asagidaki adimlari izleyin:

1. Python'i sisteminize yukleyin: https://www.python.org/downloads/
2. Terminali acin ve paketi yuklemek icin asagidaki komutu calistirin:

```bash
pip install isyatirimhisse
```

Spesifik bir versiyona ait kurulum yapacaksaniz asagidaki ornekte oldugu gibi komutu calistirabilirsiniz.

```bash
pip install isyatirimhisse==0.2.0
```

## Kullanim

### Kutuphanenin Iceri Aktarilmasi

```python
from isyatirimhisse import veri_cek, veri_gorsel
```

### Veri Cekme Ornekleri

```python
# Tek hisse, gunluk frekans, logaritmik getiri ve excel olarak kaydet
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

print(veriler)
```

```python
# Bitis tarihi yok ve spesifik isim ile excel olarak kaydet
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

print(veriler)
```

```python
# Birden fazla hisse, haftalik frekans, basit getiri, NA kaldir ve spesifik isim ile excel olarak kaydet
sembol = ['AKBNK','EUPWR']
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
    na_kaldir=na_kaldir
    excel_kaydet=excel_kaydet,
    excel_dosya_ismi=excel_dosya_ismi
)

print(veriler)
```

```python
# Birden fazla hisse, aylik frekans, kapanis fiyati, NA birak ve spesifik isim ile excel olarak kaydet
sembol = ['AKBNK','EUPWR']
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

print(veriler)
```

```python
# Birden fazla hisse, yillik frekans, kapanis fiyati, ortalama fiyatlar, NA kaldir ve excel olarak kaydetme
sembol = ['AKBNK','EUPWR']
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

print(veriler)
```

### Veri Gorsellestirme Ornekleri

```python
veriler_df = veri_cek(
    sembol=['AKBNK','THYAO','GARAN','SISE','EREGL','BIMAS'],
    baslangic_tarih='01-01-2013',
    bitis_tarih='28-07-2023',
    frekans='1g',
    getiri_hesapla=False
)

# Cizgi grafik, fiyatlari normalize et ve linewidth ekle
veri_gorsel(
    df=veriler_df,
    gorsel_turu='1',
    normalizasyon=True,
    linewidth=2
)
```

![](/imgs/gorsel_ornek_1.png)

```python
veriler_df = veri_cek(
    sembol=['AKBNK','THYAO','GARAN','SISE','EREGL','BIMAS'],
    baslangic_tarih='02-01-2013',
    bitis_tarih='28-07-2023',
    frekans='1g',
    getiri_hesapla=True
)

# Korelasyon isi matrisi ve ek bir parametre ekleme
veri_gorsel(
    df=veriler_df,
    gorsel_turu='2'
)
```

![](/imgs/gorsel_ornek_2.png)

```python
veriler_df = veri_cek(
    sembol=['AKBNK','THYAO','GARAN','SISE','EREGL','BIMAS'],
    baslangic_tarih='02-01-2013',
    bitis_tarih='28-07-2023',
    frekans='1g',
    getiri_hesapla=True
)

# Dagilim matrisi ve seffafligi artir
veri_gorsel(
    df=veriler_df,
    gorsel_turu='3',
    alpha=.1
)
```

![](/imgs/gorsel_ornek_3.png)

### `veri_cek` Fonksiyonuna Ait Parametreler

* `sembol` (str veya list, varsayilan None): Hisse senedi sembolu veya sembollerinin listesi (Orn. `'AKBNK'` veya `['AKBNK','EUPWR']`)
* `baslangic_tarih` (str, 'GG-AA-YYYY', varsayilan None): Verilerin baslangic tarihi (Orn. `'03-01-2023'`).
* `bitis_tarih` (str, 'GG-AA-YYYY', varsayilan None): Verilerin bitis tarihi (Orn. `'21-07-2023'`). Eger belirtilmezse, sistem tarihini (bugunku tarihi) otomatik olarak kullanir.
* `frekans` (str, varsayilan '1g'): Veri frekansi (`'1g'`: Gunluk, `'1h'`: Haftalik, `'1a'`: Aylik, `'1y'`: Yillik).
* `gozlem` (str, varsayilan 'son'): Haftalik, aylik ve yillik frekanslarda istenen gozlem (`'son'`: Son, `'ortalama'`: Ortalama)
* `getiri_hesapla` (bool, varsayilan True): Getiri hesaplanacak mi?
* `logaritmik_getiri` (bool, varsayilan True): Logaritmik getiri mi hesaplanacak?
* `na_kaldir` (bool, varsayilan True): Eksik degerler kaldirilacak mi?
* `excel_kaydet` (bool, varsayilan False): pandas DataFrame Excel dosyasina kaydedilsin mi?
* `excel_dosya_ismi` (str, varsayilan None): Kaydedilecek Excel dosyasinin ismi (Orn. 'veriler.xlsx' veya 'veriler'). Gecerli bir dosya ismi belirtilmezse, sistem tarihi kullanilarak 'veriler_YYYYMMDD.xlsx' ismiyle kaydedilir. Eger kaydedilecek dizinde ayni isimden baska bir dosya varsa farkli bir isimle kaydeder.

### `veri_gorsel` Fonksiyonuna Ait Parametreler

* `df` (pandas DataFrame, varsayilan None): Hisse senedi verilerinin bulundugu pandas DataFrame. Bu parametre zorunludur ve veri cercevesini belirtmek gereklidir.
* `gorsel_turu` (str, varsayilan '1'). Hangi turde gorsellestirme yapilacagini belirlemek icin kullanilir.
  * Gorsellestirme turunu belirten parametreye ait degerler:
    * `'1'`: Cizgi Grafigi
    * `'2'`: Korelasyon Isi Matrisi
    * `'3'`: Dagilim Matrisi
* `normalizasyon` (bool, varsayilan False): Verilerin normalize edilip edilmeyecegini belirten bir bool degeri. `True` olarak ayarlandiginda, veriler 0 ile 1 arasinda olceklendirilir.
* `**kwargs`: Gorsellestirme turlerine ozel ek secenekler. Bu parametreler, belirli bir gorsellestirme turu icin ozel ayarlamalar yapmak icin kullanilabilir. Ancak gorsellestirme turune gore farkli olabilir ve zorunlu degildir.
  * Gorsellestirme Turleri icin **kwargs Parametreleri:
    * Cizgi Grafigi (gorsel_turu == '1'):
      * `linewidth` (float, varsayilan 1.5): Cizgi kalinligi.
    * Korelasyon Isi Matrisi (gorsel_turu == '2'):
      * `cmap` (str, varsayilan 'coolwarm'): Renk haritasi.
      * `vmin` (float, varsayilan -1): Renk haritasindaki en kucuk deger.
      * `vmax` (float, varsayilan 1): Renk haritasindaki en buyuk deger.
    * Dagilim Matrisi (gorsel_turu == '3'):
      * `alpha` (float, varsayilan 0.5): Nokta seffafligi.

### Donen Deger

* `veri_cek` fonksiyonu bir pandas DataFrame dondurur.
* `veri_gorsel` fonksiyonu, pandas DataFrame icerisindeki verileri grafikler ve gorsel ogelerle temsil eder.

## Notlar

* Kutuphane, Is Yatirim'in web sitesindeki verilere bagimlidir. Bu nedenle, verilerin dogrulugu ve surekliligi icin lutfen ilgili web sitesini kontrol edin: [Is Yatirim](https://www.isyatirim.com.tr/tr-tr/Sayfalar/default.aspx)
* Kutuphanenin gelistirilmesi ve iyilestirilmesi icin geri bildirimlerinizi bekliyorum. GitHub reposuna katkida bulunun: [GitHub Repo](https://github.com/urazakgul/isyatirimhisse)
* Herhangi bir sorun veya oneride lutfen GitHub reposundaki "Issue" bolumunden yeni bir konu acarak bildirim saglayin: [GitHub Issues](https://github.com/urazakgul/isyatirimhisse/issues)

## Degisiklikler

### v0.1.0 - 25/07/2023

* Ilk surum yayinlandi.

### v0.1.1 - 27/07/2023

* `veri_cek` fonksiyonundaki parametreleri kontrol eden kosul ifadeleri guncellendi.
* `json` kutuphanesi kaldirildi.
* `veri_cek` fonksiyonuna `200` HTTP kodu kosul ile beraber eklendi ve takibe alindi.

### v0.2.0 - 30/07/2023

* `veri_gorsel` fonksiyonu eklendi. Fonksiyon, 3 farkli veri turunde gorsellestirme yapma imkani sunuyor.
* `veri_cek` fonksiyonuna pandas DataFrame'i excel olarak kaydedecek parametreler eklendi.

## Lisans

Bu proje MIT Lisansi altinda lisanslanmistir.

## Katkida Bulunanlar

- [Sinan Erdinc](https://github.com/sinanerdinc)