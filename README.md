# isyatirimhisse v2.1.3

## Türkçe tercih edenler için:

## Açıklama

`isyatirimhisse`, İş Yatırım'ın web sitesinden veri çekme işlemlerini kolaylaştırmak amacıyla geliştirilmiş, isteğe göre özelleştirilebilir bir Python kütüphanesidir.

*** UYARI ***

`isyatirimhisse`, resmi İş Yatırım Menkul Değerler A.Ş. kütüphanesi değildir ve şirket tarafından doğrulanmamıştır. Kullanıcılar, kütüphaneyi kullanmadan önce ilgili tüm verilere erişim için İş Yatırım Menkul Değerler A.Ş.'nin kullanım koşullarını ve haklarını incelemelidir. `isyatirimhisse`, yalnızca kişisel kullanım amaçları için tasarlanmıştır.

## Kurulum

Kütüphaneyi kullanmak için aşağıdaki adımları izleyin:

1. Python'ı sisteminize yükleyin: https://www.python.org/downloads/
2. Terminali açın ve paketi yüklemek için aşağıdaki komutu çalıştırın:

```bash
pip install isyatirimhisse
```

Spesifik bir versiyona ait kurulum yapacaksanız aşağıdaki örnekte olduğu gibi komutu çalıştırabilirsiniz.

```bash
pip install isyatirimhisse==2.1.3
```

## Kullanım

### Kütüphanenin İçeri Aktarılması

```python
from isyatirimhisse import fetch_data, fetch_financials, visualize_data
```

### Tanımlar

* `fetch_data`: Belirtilen hisse senetlerine ve endekslere ait verileri alır.
* `fetch_financials`: Belirtilen hisse senetlerine ait finansal tabloları alır.
* `visualize_data`: Belirtilen hisse senetlerine ait verileri görselleştirir ve `fetch_data` çıktıları ile uyumlu çalışması için tasarlanmıştır.

### Fonksiyon Parametreleri ve Örnekler

#### `fetch_data`

* `symbol` (str veya list, varsayılan None): Hisse senedi sembolü veya sembollerinin listesi (örn. `'AKBNK'` veya `['AKBNK','THYAO']`).
* `stock_market_index` (str veya list, varsayılan None): Endeks sembolü veya sembollerinin listesi (örn. `'XU100'` veya `['XU100','XBANK']`).
* `start_date` (str, varsayılan None): Verilerin 'GG-AA-YYYY' formatında başlangıç tarihi (örn. `'03-01-2023'`).
* `end_date` (str, varsayılan None): Verilerin 'GG-AA-YYYY' formatında bitiş tarihi (örn. `'31-07-2023'`). Eğer belirtilmezse, sistem tarihini (bugünkü tarihi) otomatik olarak kullanır.
* `frequency` (str, varsayılan '1d'): Veri frekansı (`'1d'`: Günlük, `'1w'`: Haftalık, `'1m'`: Aylık, `'1y'`: Yıllık).
* `observation` (str, varsayılan 'last'): Haftalık, aylık ve yıllık frekanslarda istenen gözlem (`'last'`: Son, `'mean'`: Ortalama).
* `calculate_return` (bool, varsayılan False): Getiri hesaplanacak mı?
* `log_return` (bool, varsayılan True): Logaritmik getiri mi hesaplanacak?
* `drop_na` (bool, varsayılan True): Eksik değerler kaldırılacak mı?
* `save_to_excel` (bool, varsayılan False): Excel dosyasına kaydedilecek mi?
* `excel_file_name` (str, varsayılan None): Kaydedilecek excel dosyasının ismi (örn. 'data.xlsx' veya 'data'). Geçerli bir dosya ismi belirtilmezse, sistem tarihi kullanılarak 'data_YYYYMMDD.xlsx' ismiyle kaydedilir. Eğer kaydedilecek dizinde aynı isimden başka bir dosya varsa farklı bir isimle kaydeder.
* `language` (str, varsayılan 'en'): Çıktıların dili (`'tr'`: Türkçe, `'en'`: İngilizce).
* `exchange` (str, varsayılan 'TL'): Hisse senedi fiyatları için para birimi (`'TL'`: Türk Lirası, `'USD'`: ABD Doları).

`fetch_data` fonksiyonu bir pandas veri çerçevesi döndürür.

```python
# Örnek 1: Tek hisse senedine ait başlangıç tarihi belli ve son işlem gününe kadar olan kapanış fiyatlarını al.
symbol='GARAN'
start_date='03-01-2023'

data=fetch_data(
    symbol=symbol,
    start_date=start_date
)
```

```python
# Örnek 2: Birden fazla hisse senedine ait başlangıç tarihi belli ve son işlem gününe kadar olan haftalık ortalama kapanış fiyatlarını al.
symbol=['GARAN','THYAO']
start_date='03-01-2023'
frequency='1w'
observation='mean'

data=fetch_data(
    symbol=symbol,
    start_date=start_date,
    frequency=frequency,
    observation=observation
)
```

```python
# Örnek 3: Birden fazla hisse senedine ait başlangıç ve bitiş tarihleri belli aylık USD kapanış fiyatları üzerinden basit getirileri al.
symbol=['GARAN','THYAO']
start_date='01-12-2021'
end_date='30-12-2022'
frequency='1m'
calculate_return=True
log_return=False
exchange='USD'

data=fetch_data(
    symbol=symbol,
    start_date=start_date,
    end_date=end_date,
    frequency=frequency,
    calculate_return=calculate_return,
    log_return=log_return,
    exchange=exchange
)
```

```python
# Örnek 4: Birden fazla hisse senedine ait başlangıç ve bitiş tarihleri belli eksik değerleri kaldırmadan yıllık ortalama USD kapanış fiyatlarını al. Ayrıca dosya ismi belirtmeden excel dosyasına kaydet ve çıktıları Türkçe yap.
symbol=['EUPWR','THYAO']
start_date='02-01-2012'
end_date='30-12-2022'
frequency='1y'
drop_na=False
save_to_excel=True
language='tr'
exchange='USD'

# Not: Örnekte bulunan EUPWR hisse senedinin 2023 yılı öncesi verileri olmadığı için çıktıda görünmeyecektir.
data=fetch_data(
    symbol=symbol,
    start_date=start_date,
    end_date=end_date,
    frequency=frequency,
    drop_na=drop_na,
    save_to_excel=save_to_excel,
    language=language,
    exchange=exchange
)
```

```python
# Örnek 5: Birden fazla hisse senedine ve endekse ait başlangıç ve bitiş tarihleri belli eksik değerleri kaldırmadan aylık ortalama USD kapanış fiyatlarını al. Ayrıca dosya ismi belirtmeden excel dosyasına kaydet ve çıktıları Türkçe yap.
symbol=['GARAN','THYAO']
stock_market_index=['XU030','XBANK']
start_date='02-01-2012'
end_date='31-07-2023'
frequency='1m'
drop_na=False
save_to_excel=True
language='tr'
exchange='USD'

data=fetch_data(
    symbol=symbol,
    stock_market_index=stock_market_index,
    start_date=start_date,
    end_date=end_date,
    frequency=frequency,
    drop_na=drop_na,
    save_to_excel=save_to_excel,
    language=language,
    exchange=exchange
)
```

#### `fetch_financials`

* `symbol` (str veya list, varsayılan None): Hisse senedi sembolü veya sembollerinin listesi (örn. `'AKBNK'` veya `['AKBNK','THYAO']`).
* `start_year` (str, varsayılan None): Finansal tabloların YYYY formatında başlangıç yılı (örn. `'2022'`).
* `end_year` (str, varsayılan None): Finansal tabloların YYYY formatında bitiş yılı (örn. `'2023'`).
* `exchange` (str, varsayılan 'TRY'): Finansal tablolar için para birimi (`'TRY'`: Türk Lirası, `'USD'`: ABD Doları).
* `financial_group` (str, varsayılan '1'): Finansal tablo türü (`'1'`: Seri XI NO:29, `'2'`: Konsolide Olmayan UFRS, `'3'`: Konsolide UFRS).
* `save_to_excel` (bool, varsayılan False): Excel dosyasına kaydedilecek mi?
* `language` (str, varsayılan 'en'): Çıktıların dili (`'tr'`: Türkçe, `'en'`: İngilizce).

`fetch_financials` fonksiyonu bir sözlük döndürür.

```python
# Örnek 1: Tek bir hisse senedi için finansal tabloları çek ve dili Türkçe olarak ayarlayıp excel dosyasına kaydet.
symbol='THYAO'
start_year='2022'
end_year='2023'
save_to_excel=True
language='tr'

data=fetch_financials(
    symbol=symbol,
    start_year=start_year,
    end_year=end_year,
    save_to_excel=save_to_excel,
    language=language
)
```

```python
# Örnek 2: Birden fazla hisse senedi için konsolide olmayan UFRS'ye göre finansal tabloları çek.
symbols=['AKBNK', 'THYAO']
start_year='2022'
end_year='2023'
financial_group='2'
language='tr'

data=fetch_financials(
    symbol=symbols,
    start_year=start_year,
    end_year=end_year,
    financial_group=financial_group,
    language=language
)
```

```python
# Örnek 3: Belirtilen birden fazla hisse senedi için USD bazlı finansal tabloları al ve örnek bir hisse senedine ait finansal tablolara Türkçe kullanarak ulaş.
symbols=['AKBNK', 'THYAO']
start_year='2018'
language='tr'
exchange='USD'

data=fetch_financials(
    symbol=symbols,
    start_year=start_year,
    language=language,
    exchange=exchange
)

# Örnekte bulunan THYAO hisse senedinin finansal tabloları
thyao_finansallar=data['THYAO']

# İstenen hisse senedine ait finansal tablolar gelmiyorsa veri kaynağı belirtilen financial_group parametresi değerine ait tabloyu yayınlamamıştır.
```

#### `visualize_data`

* `df` (pandas DataFrame, varsayılan None): Hisse senedi verilerinin bulunduğu pandas DataFrame.
* `plot_type` (str, varsayılan '1'). Görselleştirme türü (`'1'`: Çizgi Grafiği, `'2'`: Korelasyon Isı Matrisi, `'3'`: Dağılım Matrisi).
* `normalization` (bool, varsayılan False): Veriler normalize edilecek mi? True olarak ayarlandığında veriler 0 ile 1 arasında ölçeklendirilir.
* `language` (str, varsayılan 'en'): Çıktıların dili (`'tr'`: Türkçe, `'en'`: İngilizce).
* `**kwargs`: Görselleştirme türlerine özel ek seçenekler. Bu parametreler, belirli bir görselleştirme türü için özel ayarlamalar yapmak için kullanılabilir.
  * Görselleştirme Türleri için **kwargs Parametreleri:
    * Çizgi Grafiği:
      * `linewidth` (float, varsayılan 1.5): Çizgi kalınlığı.
      * `fontsize` (int, varsayılan 12): Başlık büyüklüğü.
      * `figsize` (tuple, varsayılan (10, 6)): Grafik çıktısının boyutu.
    * Korelasyon Isı Matrisi:
      * `cmap` (str, varsayılan 'coolwarm'): Renk haritası.
      * `vmin` (float, varsayılan -1): Renk haritasındaki en küçük değer.
      * `vmax` (float, varsayılan 1): Renk haritasindaki en büyük değer.
      * `fontsize` (int, varsayılan 12): Başlık büyüklüğü.
      * `figsize` (tuple, varsayılan (10, 6)): Grafik çıktısının boyutu.
    * Dağılım Matrisi:
      * `alpha` (float, varsayılan 0.5): Nokta şeffaflığı.
      * `fontsize` (int, varsayılan 12): Başlık büyüklüğü.
      * `height` (float, varsayılan 2.5): Her alt grafiğin yüksekliği.
      * `aspect` (float, varsayılan 1): Her alt grafiğin genişlik-yükselik oranı.

`visualize_data` fonksiyonu, pandas veri çerçevesi içerisindeki verileri grafikler ve görsel öğelerle temsil eder.

```python
data=fetch_data(
    symbol=['AKBNK', 'THYAO', 'GARAN', 'SISE', 'EREGL', 'BIMAS'],
    start_date='01-01-2013',
    end_date='31-07-2023'
)

# Çizgi grafik, fiyatları normalize et, çizgileri kalınlaştır, başlığı büyüt ve çıktıyı Türkçe al.
visualize_data(
    df=data,
    plot_type='1',
    normalization=True,
    language='tr',
    linewidth=2,
    fontsize=14
)
```

![](https://github.com/urazakgul/isyatirimhisse/blob/main/imgs/gorsel_ornek_1.png?raw=true)

```python
data=fetch_data(
    symbol=['AKBNK', 'THYAO', 'GARAN', 'SISE', 'EREGL', 'BIMAS'],
    start_date='01-12-2012',
    end_date='31-07-2023',
    frequency='1m',
    calculate_return=True
)

# Korelasyon ısı matrisi, ek bir parametre ekleme ve çıktıyı Türkçe al.
visualize_data(
    df=data,
    plot_type='2',
    language='tr'
)
```

![](https://github.com/urazakgul/isyatirimhisse/blob/main/imgs/gorsel_ornek_2.png?raw=true)

```python
data=fetch_data(
    symbol=['AKBNK', 'THYAO', 'GARAN'],
    start_date='01-12-2012',
    end_date='31-07-2023',
    frequency='1m',
    calculate_return=True
)

# Dağılım matrisi, daha şeffaf ve çıktıyı Türkçe al.
visualize_data(
    df=data,
    plot_type='3',
    language='tr',
    alpha=0.1
)
```

![](https://github.com/urazakgul/isyatirimhisse/blob/main/imgs/gorsel_ornek_3.png?raw=true)

## Notlar

* Kütüphane, İş Yatırım'ın web sitesindeki verilere bağımlıdır. Bu nedenle, verilerin doğruluğu ve sürekliliği için lütfen ilgili web sitesini kontrol edin: [İş Yatırım](https://www.isyatirim.com.tr/tr-tr/Sayfalar/default.aspx)
* Kütüphanenin geliştirilmesi ve iyileştirilmesi için geri bildirimlerinizi bekliyorum. GitHub reposuna katkıda bulunun: [GitHub Repo](https://github.com/urazakgul/isyatirimhisse)
* Herhangi bir sorun veya öneride lütfen GitHub reposundaki "Issue" bölümünden yeni bir konu açarak bildirim sağlayın: [GitHub Issues](https://github.com/urazakgul/isyatirimhisse/issues)

## Sürüm Notları

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

### v1.0.0 - 05/08/2023

* Fonksiyonlar İngilizce diline çevrildi.
  * `veri_cek`: `fetch_data`
  * `veri_gorsel`: `visualize_data`
* Finansal (Mali) tabloları alabilmeyi sağlayan `fetch_financials` fonksiyonu eklendi.
* Fonksiyonlara çıktıları iki dilde (İngilizce ve Türkçe) alabilme özelliği eklendi.
* `fetch_data` fonksiyonu, hisse senetlerinin TL bazlı fiyatlarının yanı sıra USD bazlı fiyatlarını da alabilme imkanı sunacak şekilde güncellendi.
* `visualize_data` fonksiyonuna ekstra özellik ekleyebilmeyi sağlayan **kwargs parametreleri genişletildi.
* Dokümantasyon içeriği Türkçe ve İngilizce olacak şekilde güncellendi.

### v2.0.0 - 10/08/2023

* `fetch_data` fonksiyonundaki `currency` parametresi `exchange` olarak değiştirildi.
* `fetch_financials` fonksiyonundaki `selenium` paketi bağımlılığı kaldırıldı.
* `fetch_financials` fonksiyonu ile finansal tablolar tek bir tablo olarak alınacak şekilde güncellendi.
* `fetch_financials` fonksiyonundaki `start_period` ve `end_period` parametreleri sırasıyla `start_year` ve `end_year` olarak güncellendi.
* `fetch_financials` fonksiyonuna `exchange` ve `financial_group` parametreleri eklendi.
* `fetch_data` ve `fetch_financials` fonksiyonlarındaki kontroller artırıldı.

### v2.1.0 - 12/08/2023

* `fetch_data` fonksiyonuna endekslere ait verileri çekmeyi sağlayacak `stock_market_index` parametresi eklenmiştir.
* `fetch_financials` fonksiyonları ile çekilen finansalların kalemlerinde bulunan boşluklar kaldırılmıştır.

### v2.1.1 - 13/08/2023

* `fetch_data` fonksiyonu ile gönderilen istekler kontrol edilecek.

### v2.1.2 - 13/08/2023

* 2.1.1 sürümündeki kod hatası düzeltilmiştir.

### v2.1.3 - 13/08/2023

* Gönderilen isteklerdeki zaman kısıtlaması iyileştirildi.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır.

## Katkıda Bulunanlar

- [Sinan Erdinç](https://github.com/sinanerdinc)
- [Tugay Şengel](https://github.com/Brigade45)
- [Anıl Öz](https://twitter.com/hocestnonsatis)

## For those who prefer English:

## Description

`isyatirimhisse` is a customizable Python library developed to simplify data fetching from IS Investment's website.

*** WARNING ***

`isyatirimhisse` is not the official IS Investment Securities library and has not been verified by the company. Users should review IS Investment Securities' terms of use and rights to access all relevant data before using the library. `isyatirimhisse` is intended for personal use only.

## Installation

Follow the steps below to use the library:

1. Install Python on your system: https://www.python.org/downloads/
2. Open the terminal and run the following command to install the package:

```bash
pip install isyatirimhisse
```

If you want to install a specific version, you can run the command as in the example below.

```bash
pip install isyatirimhisse==2.1.3
```

## Usage

### Importing the Library

```python
from isyatirimhisse import fetch_data, fetch_financials, visualize_data
```

### Definitions

* `fetch_data`: Fetches data for the specified stocks and indices.
* `fetch_financials`: Fetches financial statements for the specified stocks.
* `visualize_data`: Visualizes the data for the specified stocks is designed to work with the outputs of `fetch_data`.

### Function Parameters and Examples

#### `fetch_data`

* `symbol` (str or list, default None): The stock symbol or list of symbols (e.g. `'AKBNK'` or `['AKBNK','THYAO']`).
* `stock_market_index` (str or list, default None): The index symbol or list of indices (e.g. `'XU100'` or `['XU100','XBANK']`).
* `start_date` (str, default None): Start date of the data in 'DD-MM-YYYY' format (e.g. `'03-01-2023'`).
* `end_date` (str, default None): End date of the data in 'DD-MM-YYYY' format (e.g. `31-07-2023`). If not specified, it automatically uses the system date (today's date).
* `frequency` (str, default '1d'): Data frequency (`'1d'`: Daily, `'1w'`: Weekly, `'1m'`: Monthly, `'1y'`: Yearly).
* `observation` (str, default 'last'): The desired observation at weekly, monthly and yearly frequencies (`'last'`: Last, `'mean'`: Average).
* `calculate_return` (bool, default False): Will the return be calculated?
* `log_return` (bool, default True): Will a logarithmic return be calculated?
* `drop_na` (bool, default True): Will missing values be removed?
* `save_to_excel` (bool, default False): Will it be saved in excel file?
* `excel_file_name` (str, default None): The name of the excel file to save to (e.g. 'data.xlsx' or 'data'). If no valid file name is specified, it will be saved as 'data_YYYYMMDD.xlsx' using the system date. If there is another file with the same name in the directory to be saved, it will save with a different name.
* `language` (str, default 'en'): The language of the output (`'tr'`: Turkish, `'en'`: English).
* `exchange` (str, default 'TL'): Exchange for stock prices (`'TL'`: Turkish Lira, `'USD'`: US Dollar).

The `fetch_data` function returns a pandas data frame.

```python
# Example 1: Get the closing prices of a single stock with a given start date up to the last trading day.
symbol='GARAN'
start_date='03-01-2023'

data=fetch_data(
    symbol=symbol,
    start_date=start_date
)
```

```python
# Example 2: Get the weekly average closing prices of multiple stocks with a given start date up to the last trading day.
symbol=['GARAN','THYAO']
start_date='03-01-2023'
frequency='1w'
observation='mean'

data=fetch_data(
    symbol=symbol,
    start_date=start_date,
    frequency=frequency,
    observation=observation
)
```

```python
# Example 3: Get the simple returns of multiple stocks based on monthly USD closing prices with specific start and end dates.
symbol=['GARAN','THYAO']
start_date='01-12-2021'
end_date='30-12-2022'
frequency='1m'
calculate_return=True
log_return=False
exchange='USD'

data=fetch_data(
    symbol=symbol,
    start_date=start_date,
    end_date=end_date,
    frequency=frequency,
    calculate_return=calculate_return,
    log_return=log_return,
    exchange=exchange
)
```

```python
# Example 4: Get the annual average USD closing prices of multiple stocks without removing missing values with specific start and end dates. Also save to excel file without specifying a filename.
symbol=['EUPWR','THYAO']
start_date='02-01-2012'
end_date='30-12-2022'
frequency='1y'
drop_na=False
save_to_excel=True
exchange='USD'

# Note: The EUPWR stock in the example will not appear in the output because it has no data before 2023.
data=fetch_data(
    symbol=symbol,
    start_date=start_date,
    end_date=end_date,
    frequency=frequency,
    drop_na=drop_na,
    save_to_excel=save_to_excel,
    exchange=exchange
)
```

```python
# Example 5: Get the monthly average USD closing prices of multiple stocks and indices without removing missing values with specific start and end dates. Also save to excel file without specifying a filename.
symbol=['GARAN','THYAO']
stock_market_index=['XU030','XBANK']
start_date='02-01-2012'
end_date='30-12-2022'
frequency='1m'
drop_na=False
save_to_excel=True
exchange='USD'

data=fetch_data(
    symbol=symbol,
    stock_market_index=stock_market_index,
    start_date=start_date,
    end_date=end_date,
    frequency=frequency,
    drop_na=drop_na,
    save_to_excel=save_to_excel,
    exchange=exchange
)
```

#### `fetch_financials`

* `symbol` (str or list, default None): Stock symbol or list of symbols (e.g. `'AKBNK'` or `['AKBNK','THYAO']`).
* `start_year` (str, default None): Start year of the financial statements in 'YYYY' format (e.g. `'2022'`).
* `end_year` (str, default None): End year of the financial statements in 'YYYY' format (e.g. `'2023'`).
* `exchange` (str, default 'TRY'): Exchange for financial statements (`'TRY'`: Turkish Lira, `'USD'`: US Dollar).
* `financial_group` (str, default '1'): Type of financial statement (`'1'`: Series XI NO:29, `'2'`: Non-Consolidated IFRS, `'3'`: Consolidated IFRS).
* `save_to_excel` (bool, default False): Will it be saved in excel file?
* `language` (str, default 'en'): Language of the outputs (`'tr'`: Turkish, `'en'`: English).

The `fetch_financials` function returns a dictionary.

```python
# Example 1: Get the financial statements for a single stock, and save to excel file.
symbol='THYAO'
start_year='2022'
end_year='2023'
save_to_excel=True

data=fetch_financials(
    symbol=symbol,
    start_year=start_year,
    end_year=end_year,
    save_to_excel=save_to_excel
)
```

```python
# Example 2: Get the financial statements for multiple stocks according to non-consolidated IFRS.
symbols=['AKBNK', 'THYAO']
start_year='2022'
end_year='2023'
financial_group='2'

data=fetch_financials(
    symbol=symbols,
    start_year=start_year,
    end_year=end_year
)
```

```python
# Example 3: Get financial statements for multiple specified stocks and access the balance sheet of a sample stock.
symbols=['AKBNK', 'THYAO']
start_year='2022'
end_year='2023'

data=fetch_financials(
    symbol=symbols,
    start_year=start_year,
    end_year=end_year
)

# Financial statements of the THYAO stock in the example
thyao_financials=data['THYAO']

# If the financial statements of the requested stock are not available, the data source has not published the table associated with the specified financial_group parameter.
```

#### `visualize_data`

* `df` (pandas DataFrame, default None): The pandas DataFrame with stock data.
* `plot_type` (str, default '1'). Visualization type (`'1'`: Line Chart, `'2'`: Correlation Heat Matrix, `'3'`: Scatter Matrix).
* `normalization` (bool, default False): Will the data be normalized? When set to True the data is scaled between 0 and 1.
* `language` (str, default 'en'): Language of the outputs (`'tr'`: Turkish, `'en'`: English).
* `**kwargs`: Additional options specific to visualization types. These parameters can be used to make special adjustments for a specific visualization type.
  * **kwargs Parameters for Visualization Types:
    * Line Graph:
      * `linewidth` (float, default 1.5): Line thickness.
      * `fontsize` (int, default 12): Title size.
      * `figsize` (tuple, default (10, 6)): Size of the graph output.
    * Correlation Heat Matrix:
      * `cmap` (str, default 'coolwarm'): Color map.
      * `vmin` (float, default -1): The smallest value in the color map.
      * `vmax` (float, default 1): The largest value in the color map.
      * `fontsize` (int, default 12): Title size.
      * `figsize` (tuple, default (10, 6)): Size of the graph output.
    * Scatter Matrix:
      * `alpha` (float, default 0.5): Point transparency.
      * `fontsize` (int, default 12): Title size.
      * `height` (float, default 2.5): Height of each subgraph.
      * `aspect` (float, default 1): The width-to-height ratio of each subgraph.

The `visualize_data` function represents the data in the pandas data frame with graphs and visual elements.

```python
data=fetch_data(
    symbol=['AKBNK', 'THYAO', 'GARAN', 'SISE', 'EREGL', 'BIMAS'],
    start_date='01-01-2013',
    end_date='31-07-2023'
)

# Example 1: Line chart with normalized prices, thicker lines, increased title size, and output in English.
visualize_data(
    df=data,
    plot_type='1',
    normalization=True,
    linewidth=2,
    fontsize=14
)
```

![](https://github.com/urazakgul/isyatirimhisse/blob/main/imgs/gorsel_ornek_4.png?raw=true)

```python
data=fetch_data(
    symbol=['AKBNK', 'THYAO', 'GARAN', 'SISE', 'EREGL', 'BIMAS'],
    start_date='01-12-2012',
    end_date='31-07-2023',
    frequency='1m',
    calculate_return=True
)

# Example 2: Correlation heat matrix with default parameters and output in English.
visualize_data(
    df=data,
    plot_type='2'
)
```

![](https://github.com/urazakgul/isyatirimhisse/blob/main/imgs/gorsel_ornek_5.png?raw=true)

```python
data=fetch_data(
    symbol=['AKBNK', 'THYAO', 'GARAN'],
    start_date='01-12-2012',
    end_date='31-07-2023',
    frequency='1m',
    calculate_return=True
)

# Example 3: Scatter matrix with higher transparency, and output in English.
visualize_data(
    df=data,
    plot_type='3',
    alpha=0.1
)
```

![](https://github.com/urazakgul/isyatirimhisse/blob/main/imgs/gorsel_ornek_6.png?raw=true)

## Notes

* The library is dependent on the data on IS Investment's website. Therefore, please check the relevant website for the accuracy and continuity of the data: [IS Investment](https://www.isyatirim.com.tr/tr-tr/Sayfalar/default.aspx)
* I welcome your feedback for the development and improvement of the library. Contribute to the GitHub repo: [GitHub Repo](https://github.com/urazakgul/isyatirimhisse)
* Please report any issues or suggestions by opening a new issue in the "Issue" section of the GitHub repo: [GitHub Issues](https://github.com/urazakgul/isyatirimhisse/issues)

## Release Notes

### v0.1.0 - 25/07/2023

* First version released.

### v0.1.1 - 27/07/2023

* Updated condition statements that check parameters in the `veri_cek` function.
* Removed the `json` library.
* Added `200` HTTP code with a condition to the `veri_cek` function and added tracking.

### v0.2.0 - 30/07/2023

* Added the `veri_gorsel` function, which allows visualization in 3 different data types.
* Added parameters to the `veri_cek` function to save pandas DataFrame as excel.

### v0.2.1 - 31/07/2023

* Resolved the installation error present in version 0.2.0.
* Fixed the Turkish character problem in the documentation.
* Made images that were not visible in the documentation visible.

### v1.0.0 - 05/08/2023

* The functions were translated into English.
  * `veri_cek`: `fetch_data`
  * `veri_gorsel`: `visualize_data`
* Added `fetch_financials` function to fetch financial statements.
* Added the ability to get outputs in two languages (English and Turkish) for the functions.
* Updated the `fetch_data` function to fetch both TRY-based and USD-based prices of stocks.
* Extended **kwargs parameters for the `visualize_data` function to allow adding extra features.
* Updated documentation content to be available in both Turkish and English.

### v2.0.0 - 10/08/2023

* Changed the `currency` parameter in the `fetch_data` function to `exchange`.
* Removed the dependency on the `selenium` package from the `fetch_financials` function.
* Updated the `fetch_financials` function to acquire financial statements as a single table.
* Renamed the `start_period` and `end_period` parameters in the `fetch_financials` function to `start_year` and `end_year`, respectively.
* Added new parameters, `exchange` and `financial_group`, to the `fetch_financials` function.
* Enhanced checks and validations in both the `fetch_data` and `fetch_financials` functions.

### v2.1.0 - 12/08/2023

* Added the `stock_market_index` parameter to the `fetch_data` function to fetch data for specific stock market indices.
* Removed the spaces in the items of the financials fetched with the `fetch_financials` functions.

### v2.1.1 - 13/08/2023

* Requests sent by the `fetch_data` function will be controlled.

### v2.1.2 - 13/08/2023

* Fixed a code bug in version 2.1.1.

### v2.1.3 - 13/08/2023

* Improved the time restriction on sent requests.

## License

This project is licensed under the MIT License.

## Contributors

- [Sinan Erdinç](https://github.com/sinanerdinc)
- [Tugay Şengel](https://github.com/Brigade45)
- [Anıl Öz](https://twitter.com/hocestnonsatis)