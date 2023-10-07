# isyatirimhisse v4.0.0

## Türkçe tercih edenler için:

***Those who prefer English can scroll down the page.***

## Açıklama

`isyatirimhisse`, İş Yatırım'ın web sitesinden veri çekme işlemlerini kolaylaştırmak amacıyla geliştirilmiş, isteğe göre özelleştirilebilir bir Python kütüphanesidir.

*** UYARI ***

`isyatirimhisse`, resmi İş Yatırım Menkul Değerler A.Ş. kütüphanesi değildir ve şirket tarafından doğrulanmamıştır. Kullanıcılar, kütüphaneyi kullanmadan önce ilgili tüm verilere erişim için İş Yatırım Menkul Değerler A.Ş.'nin kullanım koşullarını ve haklarını incelemelidir. `isyatirimhisse`, yalnızca kişisel kullanım amaçları için tasarlanmıştır.

İş Yatırım web sitesinden hisse senedi verileri ve finansal tablolara erişmek için Python paketini kullanırken, aşırı talep göndermenin potansiyel sonuçlarına dikkat etmek çok önemlidir. Aşırı talep aşağıdaki çeşitli olumsuz etkilere neden olabilir:

* **Performans Etkisi:** Kısa bir süre içinde çok fazla talep göndermek, İş Yatırım web sitesinin performansını ve yanıt verme hızını ciddi şekilde etkileyebilir.

* **Hizmet Kesintisi:** Yoğun veri çekme işlemleri, web sitesindeki güvenlik önlemlerini tetikleyebilir ve geçici hizmet kesintilerine neden olabilir.

* **IP Engelleme:** Tekrarlayan veya agresif veri çekme davranışları, IP adresinizin web sitesine erişimini geçici veya kalıcı olarak engellemesine yol açabilir.

Bu sorunlardan kaçınmak ve sorunsuz bir işlem sağlamak için aşağıdaki önerileri dikkate alabilirsiniz.

- Taleplerinizin hızını, web sitesinin kapasitesini dikkate alarak makul bir seviyede tutun.
- Sıkça çekilen verileri yerel olarak saklamaya çalışın. Böylece tekrarlayan taleplere gerek kalmayacaktır.

Bu kurallara uymak, kesinti riskini en aza indirgeyebilir ve İş Yatırım web sitesinin hem sizin hem de diğer kullanıcılar için güvenilir bir deneyim sunmasını sağlar.

## Kurulum

Kütüphaneyi kullanmak için aşağıdaki adımları izleyin:

1. Python'ı sisteminize yükleyin: https://www.python.org/downloads/
2. Terminali açın ve paketi yüklemek için aşağıdaki komutu çalıştırın:

```bash
pip install isyatirimhisse
```

Spesifik bir versiyona ait kurulum yapacaksanız aşağıdaki örnekte olduğu gibi komutu çalıştırabilirsiniz.

```bash
pip install isyatirimhisse==4.0.0
```

Yüklü paketin versiyonuna aşağıdaki komut yardımıyla ulaşabilirsiniz.

```bash
pip show isyatirimhisse
```

## Kullanım

### Kütüphanenin İçeri Aktarılması

```python
from isyatirimhisse import StockData, Financials
```

### Tanımlar

* `StockData`: Belirtilen hisse senetlerine ve endekslere ait verileri alır.
* `Financials`: Belirtilen hisse senetlerine ait finansal tabloları alır.

### Metot Parametreleri ve Örnekler

#### `StockData`

* `symbols` (str veya list, varsayılan None): Hisse senedi sembolü veya sembollerinin listesi (örn. `'AKBNK'` veya `['AKBNK','THYAO']`).
* `start_date` (str, varsayılan None): Verilerin 'GG-AA-YYYY' formatında başlangıç tarihi (örn. `'03-01-2023'`).
* `end_date` (str, varsayılan None): Verilerin 'GG-AA-YYYY' formatında bitiş tarihi (örn. `'29-09-2023'`). Eğer belirtilmezse, sistem tarihini (bugünkü tarihi) otomatik olarak kullanır.
* `exchange` (str, varsayılan '2'): Hisse senedi fiyatları için para birimi (`'0'`: Türk Lirası, `'1'`: ABD Doları, `'2'`: Türk Lirası ve ABD Doları).
* `frequency` (str, varsayılan '1d'): Veri frekansı (`'1d'`: Günlük, `'1w'`: Haftalık, `'1mo'`: Aylık, `'3mo'`: Çeyreklik, `'1y'`: Yıllık).
* `observation` (str, varsayılan 'last'): Haftalık, aylık ve yıllık frekanslarda istenen gözlem (`'last'`: Son, `'mean'`: Ortalama).
* `return_type` (str, varsayılan '0'): Ham veriler mi kullanılacak yoksa getiri mi hesaplanacak? (`'0'`: Ham, `'1'`: Logaritmik Getiri, `'2'`: Basit Getiri)
* `save_to_excel` (bool, varsayılan False): Excel dosyasına kaydedilecek mi?

`StockData` sınıfına ait `get_data` metodu bir pandas veri çerçevesi döndürür.

```python
# Örnek 1: Tek hisse senedine ait başlangıç tarihi belli ve son işlem gününe kadar olan kapanış fiyatlarını al.

stock_data = StockData()

df = stock_data.get_data(
    symbols='THYAO',
    start_date='02-01-2023'
)
print(df)
```

```python
# Örnek 2: Birden fazla hisse senedine ait başlangıç tarihi belli ve son işlem gününe kadar olan haftalık ortalama kapanış fiyatlarını TL bazında al.

stock_data = StockData()

df = stock_data.get_data(
    symbols=['THYAO','PGSUS'],
    start_date = '02-01-2023',
    exchange='0',
    frequency='1w',
    observation='mean'
)
print(df)

# Haftalık frekansta veriler Pazar günleri başlangıç kabul edilerek ayarlanmaktadır.
```

```python
# Örnek 3: Birden fazla hisse senedine ait başlangıç ve bitiş tarihleri belli aylık USD fiyatları üzerinden logaritmik getirileri al.

stock_data = StockData()

df = stock_data.get_data(
    symbols=['THYAO','PGSUS'],
    start_date='01-01-2023',
    end_date='29-09-2023',
    exchange='1',
    frequency='1mo',
    return_type='1'
)
print(df)
```

```python
# Örnek 4: Birden fazla hisse senedine ait başlangıç ve bitiş tarihleri belli çeyreklik USD fiyatları üzerinden basit getirileri al.

stock_data = StockData()

df = stock_data.get_data(
    symbols=['THYAO','PGSUS'],
    start_date='01-01-2023',
    end_date='29-09-2023',
    exchange='1',
    frequency='3mo',
    return_type='2'
)
print(df)
```

```python
# Örnek 5: Birden fazla hisse senedine ait başlangıç ve bitiş tarihleri belli yıllık ortalama USD fiyatlarını al. Sonucu excel dosyasına kaydet.

stock_data = StockData()

df = stock_data.get_data(
    symbols=['THYAO','EUPWR'],
    start_date='01-01-2012',
    end_date='06-10-2023',
    exchange='1',
    frequency='1y',
    return_type='1',
    save_to_excel=True
)
print(df)

# Not: Örnekte bulunan EUPWR hisse senedinin 2023 yılı öncesi verileri olmadığı için çıktıda görünmeyecektir.
```

#### `Financials`

* `symbols` (str veya list, varsayılan None): Hisse senedi sembolü veya sembollerinin listesi (örn. `'AKBNK'` veya `['AKBNK','THYAO']`).
* `start_year` (str, varsayılan None): Finansal tabloların 'YYYY' formatında başlangıç yılı (örn. `'2022'`). Belirtilmezse 2 yıl öncesini dikkate alır.
* `end_year` (str, varsayılan None): Finansal tabloların 'YYYY' formatında bitiş yılı (örn. `'2023'`). Belirtilmezse mevcut yılı dikkate alır.
* `exchange` (str, varsayılan 'TRY'): Finansal tablolar için para birimi (`'TRY'`: Türk Lirası, `'USD'`: ABD Doları).
* `financial_group` (str, varsayılan '1'): Finansal tablo türü (`'1'`: Seri XI NO:29, `'2'`: Konsolide Olmayan UFRS, `'3'`: Konsolide UFRS).
* `save_to_excel` (bool, varsayılan False): Excel dosyasına kaydedilecek mi?

`Financials` fonksiyonunun `get_data` metodu bir sözlük döndürür.

```python
# Örnek 1: Tek bir hisse senedi için finansal tabloları istenilen başlangıç yılından itibaren çek.

financials = Financials()

df = financials.get_data(
    symbols='THYAO',
    start_year='2020'
)
print(df)
```

```python
# Örnek 2: Birden fazla hisse senedi için finansal tabloları istenilen başlangıç ve bitiş yılı aralığında çek.
# Sözlük tipinde saklanan verilerden istenen şirket aşağıdaki gibi çekilebilir.

financials = Financials()

df = financials.get_data(
    symbols=['THYAO','PGSUS'],
    start_year='2019',
    end_year='2023',
    exchange='TRY',
    financial_group='1',
    save_to_excel=True
)

import pandas as pd

df_thyao = pd.DataFrame(df['THYAO'])
```

```python
# Örnek 3: Birden fazla hisse senedi için finansal tabloları istenilen başlangıç ve bitiş yılı aralığında çek.

financials = Financials()

df = financials.get_data(
    symbols=['THYAO','AKBNK'],
    start_year='2019',
    end_year='2023',
    exchange='TRY',
    financial_group='1',
    save_to_excel=True
)

# Not: Örnekte bulunan AKBNK hisse senedi Seri XI NO:29'a uymadığı için (UFRS kullanılmalı) çıktıda görünmeyecektir.
```

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

### v3.0.0 - 19/08/2023

* `fetch_data` fonksiyonu asenkron yapıya geçirilmiştir.
* `fetch_data` fonksiyonundaki sembol parametresi 400 sembol ile sınırlandırılmıştır.
* `visualize_data` fonksiyonunun çalıştırılma şekli asenkron yapı nedeniyle değişmiştir.

### v3.0.1 - 20/08/2023

* Veri çerçevesindeki tarih aralığı problemi düzeltildi.

### v3.0.2 - 05/10/2023

* 400 olan sembol sınırlaması kaldırıldı.

### v4.0.0 - 07/10/2023

* `StockData` ve `Financials` isimli iki sınıf oluşturuldu.
* `StockData` sınıfındaki `get_data` ve `Financials` sınıfındaki `get_data` metotlarının parametreleri güncellendi.
* Tablo çıktılarının yapısı değiştirildi.
* Veri görselleştirme özelliği kaldırıldı.
* Asenkron yapı kaldırıldı.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır.

## Katkıda Bulunanlar

- [Sinan Erdinç](https://github.com/sinanerdinc)
- [Tugay Şengel](https://github.com/Brigade45)
- [Anıl Öz](https://twitter.com/hocestnonsatis)

## For those who prefer English:

## Description

`isyatirimhisse` is a customizable Python library developed to simplify data fetching from Is Investment's website.

*** WARNING ***

`isyatirimhisse` is not the official Is Investment Securities library and has not been verified by the company. Users should review Is Investment Securities' terms of use and rights to access all relevant data before using the library. `isyatirimhisse` is intended for personal use only.

When using the Python package to access stock data and financial statements from the Is Investment website, it is crucial to be mindful of the potential consequences of excessive requests. Excessive requests can lead to various adverse effects:

* **Performance Impact:** Sending too many requests in a short period can significantly affect the performance and response time of the Is Investment website.

* **Service Disruption:** Intensive data retrieval processes can trigger security measures on the website, causing temporary service disruptions.

* **IP Blocking:** Repetitive or aggressive data retrieval behavior may lead to your IP address being temporarily or permanently blocked from accessing the website.

To avoid these issues and ensure smooth operations, consider the following recommendations:

- Keep the speed of your requests at a reasonable level, taking into account the website's capacity.
- Attempt to store frequently retrieved data locally, eliminating the need for repetitive requests.

Adhering to these guidelines can minimize the risk of interruptions and ensure that the Is Investment website provides a reliable experience for both you and other users.

## Installation

Follow the steps below to use the library:

1. Install Python on your system: https://www.python.org/downloads/
2. Open the terminal and run the following command to install the package:

```bash
pip install isyatirimhisse
```

If you want to install a specific version, you can run the command as in the example below.

```bash
pip install isyatirimhisse==4.0.0
```

You can find the version of the installed package with the following command.

```bash
pip show isyatirimhisse
```

## Usage

### Importing the Library

```python
from isyatirimhisse import StockData, Financials
```

### Definitions

* `StockData`: Fetches data for the specified stocks and indices.
* `Financials`: Fetches financial statements for the specified stocks.

### Method Parameters and Examples

#### `StockData`

* `symbol` (str or list, default None): The stock symbol or list of symbols (e.g. `'AKBNK'` or `['AKBNK','THYAO']`).
* `start_date` (str, default None): Start date of the data in 'DD-MM-YYYY' format (e.g. `'03-01-2023'`).
* `end_date` (str, default None): End date of the data in 'DD-MM-YYYY' format (e.g. `29-09-2023`). If not specified, it automatically uses the system date (today's date).
* `exchange` (str, default '2'): Exchange for stock prices (`'0'`: Turkish Lira, `'1'`: US Dollar, `'2'`: Turkish Lira and US Dollar).
* `frequency` (str, default '1d'): Data frequency (`'1d'`: Daily, `'1w'`: Weekly, `'1m'`: Monthly, `'3mo'`: Quarterly, `'1y'`: Yearly).
* `observation` (str, default 'last'): The desired observation at weekly, monthly, quarterly and yearly frequencies (`'last'`, `'mean'`).
* `return_type` (str, default '0'): Will raw data be used or returns be calculated? (`'0'`: Raw, `'1'`: Logarithmic Return, `'2'`: Simple Return)
* `save_to_excel` (bool, default False): Will it be saved in excel file?

The `get_data` method of the `StockData` class returns a pandas DataFrame.

```python
# Example 1: Retrieve the closing prices for a single stock with a specified start date and up to the last trading day.

stock_data = StockData()

df = stock_data.get_data(
    symbols='THYAO',
    start_date='02-01-2023'
)
print(df)
```

```python
# Example 2: Retrieve the weekly average closing prices in Turkish Lira for multiple stocks with specified start dates and up to the last trading day.

stock_data = StockData()

df = stock_data.get_data(
    symbols=['THYAO','PGSUS'],
    start_date = '02-01-2023',
    exchange='0',
    frequency='1w',
    observation='mean'
)
print(df)

# The data is adjusted with a weekly frequency, considering Sunday as the starting point.
```

```python
# Example 3: Compute the logarithmic returns for multiple stocks with known start and end dates, using monthly USD prices.

stock_data = StockData()

df = stock_data.get_data(
    symbols=['THYAO','PGSUS'],
    start_date='01-01-2023',
    end_date='29-09-2023',
    exchange='1',
    frequency='1mo',
    return_type='1'
)
print(df)
```

```python
# Example 4: Compute the simple returns for multiple stocks with known start and end dates, using quarterly USD prices.

stock_data = StockData()

df = stock_data.get_data(
    symbols=['THYAO','PGSUS'],
    start_date='01-01-2023',
    end_date='29-09-2023',
    exchange='1',
    frequency='3mo',
    return_type='2'
)
print(df)
```

```python
# Example 5: Retrieve the annual average USD prices for multiple stocks with known start and end dates. Save the result to an Excel file.

stock_data = StockData()

df = stock_data.get_data(
    symbols=['THYAO','EUPWR'],
    start_date='01-01-2012',
    end_date='06-10-2023',
    exchange='1',
    frequency='1y',
    return_type='1',
    save_to_excel=True
)
print(df)

# Note: Data for the EUPWR stock before the year 2023 is unavailable, and therefore, it will not be displayed in the output.
```

#### `Financials`

* `symbol` (str or list, default None): Stock symbol or list of symbols (e.g. `'AKBNK'` or `['AKBNK','THYAO']`).
* `start_year` (str, default None): Start year of the financial statements in 'YYYY' format (e.g. `'2022'`). If not specified, it defaults to two years ago.
* `end_year` (str, default None): End year of the financial statements in 'YYYY' format (e.g. `'2023'`). If not specified, it defaults to the current year.
* `exchange` (str, default 'TRY'): Exchange for financial statements (`'TRY'`: Turkish Lira, `'USD'`: US Dollar).
* `financial_group` (str, default '1'): Type of financial statement (`'1'`: Series XI NO:29, `'2'`: Non-Consolidated IFRS, `'3'`: Consolidated IFRS).
* `save_to_excel` (bool, default False): Will it be saved in excel file?

The `get_data` method of the `Financials` class returns a dictionary.

```python
# Example 1: Retrieve financial statements for a single stock starting from the desired start year.

financials = Financials()

df = financials.get_data(
    symbols='THYAO',
    start_year='2020'
)
print(df)
```

```python
# Example 2: Retrieve financial statements for multiple stocks within the desired start and end year range.
# The desired company can be extracted from data stored in a dictionary as shown below.

financials = Financials()

df = financials.get_data(
    symbols=['THYAO','PGSUS'],
    start_year='2019',
    end_year='2023',
    exchange='TRY',
    financial_group='1',
    save_to_excel=True
)

import pandas as pd

df_thyao = pd.DataFrame(df['THYAO'])
```

```python
# Example 3: Retrieve financial statements for multiple stocks within the desired start and end year range.

financials = Financials()

df = financials.get_data(
    symbols=['THYAO','AKBNK'],
    start_year='2019',
    end_year='2023',
    exchange='TRY',
    financial_group='1',
    save_to_excel=True
)

# Note: The AKBNK stock featured in the example will not appear in the output due to non-compliance with Series XI NO:29 (IFRS should be used).
```

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

### v3.0.0 - 19/08/2023

* The `fetch_data` function is asynchronous.
* The symbol parameter in the `fetch_data` function is limited to 400 symbols.
* The way `visualize_data` is executed changed due to its asynchronous structure.

### v3.0.1 - 20/08/2023

* Fixed date range problem in the data frame.

### v3.0.2 - 05/10/2023

* Removed the limit on the number of stock symbols, which was 400.

### v4.0.0 - 07/10/2023

* Created two classes, `StockData` and `Financials`.
* Updated parameters for the `get_data` method in the `StockData` class and the `get_data` method in the `Financials` class.
* Modified the structure of table outputs.
* Removed data visualization feature.
* Removed asynchronous structure.

## License

This project is licensed under the MIT License.

## Contributors

- [Sinan Erdinç](https://github.com/sinanerdinc)
- [Tugay Şengel](https://github.com/Brigade45)
- [Anıl Öz](https://twitter.com/hocestnonsatis)