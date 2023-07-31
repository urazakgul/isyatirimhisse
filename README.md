# isyatirimhisse v0.2.1

## Açıklama

`isyatirimhisse`, İş Yatırım'ın web sitesinden veri çekme işlemlerini kolaylaştırmak amacıyla geliştirilmiş, isteğe göre özelleştirilebilir bir Python kütüphanesidir.

*** UYARI ***

`isyatirimhisse`, resmi İş Yatırım Menkul Değerler A.Ş. kütüphanesi değildir ve şirket tarafından doğrulanmamıştır. Kullanıcılar, bu kütüphaneyi kullanmadan önce ilgili tüm verilere erişim için İş Yatırım Menkul Değerler A.Ş. kullanım koşullarını ve haklarını incelemelidir. `isyatirimhisse` kütüphanesi, yalnızca kişisel kullanım amaçları için tasarlanmıştır.

## Kurulum

Kütüphaneyi kullanmak için aşağıdaki adımları izleyin:

1. Python'ı sisteminize yükleyin: https://www.python.org/downloads/
2. Terminali açın ve paketi yüklemek için aşağıdaki komutu çalıştırın:

```bash
pip install isyatirimhisse
```

Spesifik bir versiyona ait kurulum yapacaksanız aşağıdaki örnekte olduğu gibi komutu çalıştırabilirsiniz.

```bash
pip install isyatirimhisse==0.2.1
```

## Kullanım

### Kütüphanenin İçeri Aktarılması

```python
from isyatirimhisse import veri_cek, veri_gorsel
```

### Veri Çekme Örnekleri

```python
# Tek hisse, günlük frekans, logaritmik getiri ve excel olarak kaydet
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
# Bitiş tarihi yok ve spesifik isim ile excel olarak kaydet
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
# Birden fazla hisse, haftalık frekans, basit getiri, NA kaldır ve spesifik isim ile excel olarak kaydet
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
# Birden fazla hisse, aylık frekans, kapanış fiyatı, NA bırak ve spesifik isim ile excel olarak kaydet
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
# Birden fazla hisse, yıllık frekans, kapanış fiyatı, ortalama fiyatlar, NA kaldır ve excel olarak kaydetme
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

### Veri Görselleştirme Örnekleri

```python
veriler_df = veri_cek(
    sembol=['AKBNK','THYAO','GARAN','SISE','EREGL','BIMAS'],
    baslangic_tarih='01-01-2013',
    bitis_tarih='28-07-2023',
    frekans='1g',
    getiri_hesapla=False
)

# Çizgi grafik, fiyatları normalize et ve linewidth ekle
veri_gorsel(
    df=veriler_df,
    gorsel_turu='1',
    normalizasyon=True,
    linewidth=2
)
```

![](https://github.com/urazakgul/isyatirimhisse/blob/main/imgs/gorsel_ornek_1.png?raw=true)

```python
veriler_df = veri_cek(
    sembol=['AKBNK','THYAO','GARAN','SISE','EREGL','BIMAS'],
    baslangic_tarih='02-01-2013',
    bitis_tarih='28-07-2023',
    frekans='1g',
    getiri_hesapla=True
)

# Korelasyon ısı matrisi ve ek bir parametre ekleme
veri_gorsel(
    df=veriler_df,
    gorsel_turu='2'
)
```

![](https://github.com/urazakgul/isyatirimhisse/blob/main/imgs/gorsel_ornek_2.png?raw=true)

```python
veriler_df = veri_cek(
    sembol=['AKBNK','THYAO','GARAN','SISE','EREGL','BIMAS'],
    baslangic_tarih='02-01-2013',
    bitis_tarih='28-07-2023',
    frekans='1g',
    getiri_hesapla=True
)

# Dağılım matrisi ve şeffaflığı artır
veri_gorsel(
    df=veriler_df,
    gorsel_turu='3',
    alpha=.1
)
```

![](https://github.com/urazakgul/isyatirimhisse/blob/main/imgs/gorsel_ornek_3.png?raw=true)

### `veri_cek` Fonksiyonuna Ait Parametreler

* `sembol` (str veya list, varsayılan None): Hisse senedi sembolü veya sembollerinin listesi (Örn. `'AKBNK'` veya `['AKBNK','EUPWR']`)
* `baslangic_tarih` (str, 'GG-AA-YYYY', varsayılan None): Verilerin başlangıç tarihi (Örn. `'03-01-2023'`).
* `bitis_tarih` (str, 'GG-AA-YYYY', varsayılan None): Verilerin bitiş tarihi (Örn. `'21-07-2023'`). Eğer belirtilmezse, sistem tarihini (bugünkü tarihi) otomatik olarak kullanır.
* `frekans` (str, varsayılan '1g'): Veri frekansı (`'1g'`: Günlük, `'1h'`: Haftalık, `'1a'`: Aylık, `'1y'`: Yıllık).
* `gozlem` (str, varsayılan 'son'): Haftalık, aylık ve yıllık frekanslarda istenen gözlem (`'son'`: Son, `'ortalama'`: Ortalama)
* `getiri_hesapla` (bool, varsayılan True): Getiri hesaplanacak mı?
* `logaritmik_getiri` (bool, varsayılan True): Logaritmik getiri mi hesaplanacak?
* `na_kaldir` (bool, varsayılan True): Eksik değerler kaldırılacak mı?
* `excel_kaydet` (bool, varsayılan False): pandas DataFrame Excel dosyasına kaydedilsin mi?
* `excel_dosya_ismi` (str, varsayılan None): Kaydedilecek Excel dosyasının ismi (Örn. 'veriler.xlsx' veya 'veriler'). Geçerli bir dosya ismi belirtilmezse, sistem tarihi kullanılarak 'veriler_YYYYMMDD.xlsx' ismiyle kaydedilir. Eğer kaydedilecek dizinde aynı isimden başka bir dosya varsa farklı bir isimle kaydeder.

### `veri_gorsel` Fonksiyonuna Ait Parametreler

* `df` (pandas DataFrame, varsayılan None): Hisse senedi verilerinin bulunduğu pandas DataFrame. Bu parametre zorunludur ve veri çerçevesini belirtmek gereklidir.
* `gorsel_turu` (str, varsayılan '1'). Hangi türde görselleştirme yapılacağını belirlemek için kullanılır.
  * Görselleştirme türünü belirten parametreye ait değerler:
    * `'1'`: Çizgi Grafiği
    * `'2'`: Korelasyon Isı Matrisi
    * `'3'`: Dağılım Matrisi
* `normalizasyon` (bool, varsayılan False): Verilerin normalize edilip edilmeyeceğini belirten bir bool değeri. `True` olarak ayarlandığında, veriler 0 ile 1 arasında ölçeklendirilir.
* `**kwargs`: Görselleştirme türlerine özel ek seçenekler. Bu parametreler, belirli bir görselleştirme türü için özel ayarlamalar yapmak için kullanılabilir. Ancak görselleştirme türüne göre farklı olabilir ve zorunlu değildir.
  * Görselleştirme Türleri için **kwargs Parametreleri:
    * Çizgi Grafiği (gorsel_turu == '1'):
      * `linewidth` (float, varsayılan 1.5): Çizgi kalınlığı.
    * Korelasyon Isı Matrisi (gorsel_turu == '2'):
      * `cmap` (str, varsayılan 'coolwarm'): Renk haritası.
      * `vmin` (float, varsayılan -1): Renk haritasındaki en küçük değer.
      * `vmax` (float, varsayılan 1): Renk haritasindaki en büyük değer.
    * Dağılım Matrisi (gorsel_turu == '3'):
      * `alpha` (float, varsayılan 0.5): Nokta şeffaflığı.

### Dönen Değer

* `veri_cek` fonksiyonu bir pandas DataFrame döndürür.
* `veri_gorsel` fonksiyonu, pandas DataFrame içerisindeki verileri grafikler ve görsel öğelerle temsil eder.

## Notlar

* Kütüphane, İş Yatırım'ın web sitesindeki verilere bağımlıdır. Bu nedenle, verilerin doğruluğu ve sürekliliği için lütfen ilgili web sitesini kontrol edin: [İş Yatırım](https://www.isyatirim.com.tr/tr-tr/Sayfalar/default.aspx)
* Kütüphanenin geliştirilmesi ve iyileştirilmesi için geri bildirimlerinizi bekliyorum. GitHub reposuna katkıda bulunun: [GitHub Repo](https://github.com/urazakgul/isyatirimhisse)
* Herhangi bir sorun veya öneride lütfen GitHub reposundaki "Issue" bölümünden yeni bir konu açarak bildirim sağlayın: [GitHub Issues](https://github.com/urazakgul/isyatirimhisse/issues)

## Değişiklikler

### v0.1.0 - 25/07/2023

* İlk sürüm yayınlandı.

### v0.1.1 - 27/07/2023

* `veri_cek` fonksiyonundaki parametreleri kontrol eden koşul ifadeleri güncellendi.
* `json` kütüphanesi kaldırıldı.
* `veri_cek` fonksiyonuna `200` HTTP kodu koşul ile beraber eklendi ve takibe alındı.

### v0.2.0 - 30/07/2023

* `veri_gorsel` fonksiyonu eklendi. Fonksiyon, 3 farklı veri türünde görselleştirme yapma imkanı sunuyor.
* `veri_cek` fonksiyonuna pandas DataFrame'i excel olarak kaydedecek parametreler eklendi.

### v0.2.1 - 31/07/2023

* 0.2.0 sürümündeki kurulum hatası giderildi.
* Dokümantasyondaki Türkçe karakter problemi giderildi.
* Dokümantasyonda görünmeyen görseller görünür hale getirildi.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır.

## Katkıda Bulunanlar

- [Sinan Erdinç](https://github.com/sinanerdinc)