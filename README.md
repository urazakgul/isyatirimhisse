# isyatirimhisse v0.1.1

## Açıklama

`isyatirimhisse`, İş Yatırım'ın web sitesinden veri çekme işlemlerini kolaylaştırmak amacıyla geliştirilmiş, isteğe göre özelleştirilebilir bir Python kütüphanesidir.

> :warning: `isyatirimhisse`, resmi İş Yatırım Menkul Değerler A.Ş. kütüphanesi değildir ve şirket tarafından doğrulanmamıştır. Kullanıcılar, bu kütüphaneyi kullanmadan önce ilgili tüm verilere erişim için İş Yatırım Menkul Değerler A.Ş. kullanım koşullarını ve haklarını incelemelidir. `isyatirimhisse` kütüphanesi, yalnızca kişisel kullanım amaçları için tasarlanmıştır.

## Kurulum

Kütüphaneyi kullanmak için aşağıdaki adımları izleyin:

- Python'ı sisteminize yükleyin: https://www.python.org/downloads/
- Terminali açın ve paketi yüklemek için aşağıdaki komutu çalıştırın:

```bash
pip install isyatirimhisse
```

## Kullanım

### Kütüphanenin İçeri Aktarılması

```python
from isyatirimhisse import veri_cek
```

### Veri Çekme Örnekleri

```python
# Tek hisse, günlük frekans ve logaritmik getiri
sembol = 'AKBNK'
baslangic_tarih = '03-01-2023'
bitis_tarih = '21-07-2023'
frekans = '1g'
gozlem = 'son'
getiri_hesapla = True
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

```python
# Bitiş tarihi yok
sembol = 'AKBNK'
baslangic_tarih = '03-01-2023'
frekans = '1g'
gozlem = 'son'
getiri_hesapla = True
logaritmik_getiri = True
na_kaldir = True

veriler = veri_cek(
    sembol=sembol,
    baslangic_tarih=baslangic_tarih,
    frekans=frekans,
    gozlem=gozlem,
    getiri_hesapla=getiri_hesapla,
    logaritmik_getiri=logaritmik_getiri,
    na_kaldir=na_kaldir
)

print(veriler)
```

```python
# Birden fazla hisse, haftalık frekans, basit getiri ve NA kaldır
sembol = ['AKBNK','EUPWR']
baslangic_tarih = '03-01-2023'
bitis_tarih = '21-07-2023'
frekans = '1h'
gozlem = 'son'
getiri_hesapla = True
logaritmik_getiri = False
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

```python
# Birden fazla hisse, aylık frekans, kapanış fiyatı ve NA bırak
sembol = ['AKBNK','EUPWR']
baslangic_tarih = '03-01-2023'
bitis_tarih = '21-07-2023'
frekans = '1a'
gozlem = 'son'
getiri_hesapla = False
logaritmik_getiri = True
na_kaldir = False

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

```python
# Birden fazla hisse, yıllık frekans, kapanış fiyatı, ortalama fiyatlar ve NA kaldır
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

### Fonksiyon Parametreleri

* `sembol` (str veya list, varsayılan None): Hisse senedi sembolü veya sembollerinin listesi (Örn. 'AKBNK' veya ['AKBNK','EUPWR'])
* `baslangic_tarih` (str, 'GG-AA-YYYY', varsayılan None): Verilerin başlangıç tarihi (Örn. '03-01-2023').
* `bitis_tarih` (str, 'GG-AA-YYYY', varsayılan None): Verilerin bitiş tarihi (Örn. '21-07-2023'). Eğer belirtilmezse, sistem tarihini (bugünkü tarihi) otomatik olarak kullanır.
* `frekans` (str, varsayılan '1g'): Veri frekansı (Günlük: '1g', Haftalık: '1h', Aylık: '1a', Yıllık: '1y').
* `gozlem` (str, varsayılan 'son'): Haftalık, aylık ve yıllık frekanslarda istenen gözlem ('son': Son, 'ortalama': Ortalama)
* `getiri_hesapla` (bool, varsayılan True): Getiri hesaplanacak mı?
* `logaritmik_getiri` (bool, varsayilan True): Logaritmik getiri mi hesaplanacak?
* `na_kaldir` (bool, varsayilan True): Eksik değerler kaldırılacak mı?

### Dönen Değer

`veri_cek` fonksiyonu bir pandas DataFrame döndürür.

## Notlar

* Kütüphane, İş Yatırım'ın web sitesindeki verilere bağlıdır. Bu nedenle, verilerin doğruluğu ve sürekliliği için lütfen ilgili web sitesini kontrol edin: [İş Yatırım](https://www.isyatirim.com.tr/tr-tr/Sayfalar/default.aspx)
* Kütüphanenin geliştirilmesi ve iyileştirilmesi için geri bildirimlerinizi bekliyorum. GitHub reposuna katkıda bulunun: [GitHub Repo](https://github.com/urazakgul/isyatirimhisse)
* Herhangi bir sorun veya öneride lütfen GitHub reposundaki "Issue" bölümünden yeni bir konu açarak bildirim sağlayın: [GitHub Issues](https://github.com/urazakgul/isyatirimhisse/issues)

## Değişiklikler

### v0.1.0 - 25/07/2023

* İlk sürüm yayınlandı.

### v0.1.1 - 27/07/2023

* `veri_cek` fonksiyonundaki parametreleri kontrol eden koşul ifadeleri güncellendi.
* `json` kütüphanesi kaldırıldı.
* `veri_cek` fonksiyonuna `200` HTTP kodu koşul ile beraber eklendi ve takibe alındı.

## Lisans

Bu kütüphane, MIT lisansı altında lisanslanmıştır.

## Katkıda Bulunanlar

- [Sinan Erdinç](https://github.com/sinanerdinc)
