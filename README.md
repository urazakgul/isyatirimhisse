# isyatirimhisse v5.0.0

## Türkçe tercih edenler için:

***Those who prefer English can scroll down the page.***

## Açıklama

`isyatirimhisse`, İş Yatırım'ın web sitesinden hisse senedi, endeks ve finansal tablo verilerini kolayca çekmek için geliştirilmiş bir Python kütüphanesidir.

*** UYARI ***

`isyatirimhisse`, resmi İş Yatırım Menkul Değerler A.Ş. kütüphanesi değildir ve şirket tarafından doğrulanmamıştır. Kullanıcılar, kütüphaneyi kullanmadan önce ilgili tüm verilere erişim için İş Yatırım Menkul Değerler A.Ş.'nin kullanım koşullarını ve haklarını incelemelidir. `isyatirimhisse`, yalnızca kişisel kullanım amaçları için tasarlanmıştır.

İş Yatırım web sitesinden hisse senedi verileri ve finansal tablolara erişmek için Python paketini kullanırken, aşırı talep göndermenin potansiyel sonuçlarına dikkat etmek çok önemlidir. Aşırı talep aşağıdaki çeşitli olumsuz etkilere neden olabilir:

* **Performans Etkisi:** Kısa bir süre içinde çok fazla talep göndermek, İş Yatırım web sitesinin performansını ve yanıt verme hızını ciddi şekilde etkileyebilir.

* **Hizmet Kesintisi:** Yoğun veri çekme işlemleri, web sitesindeki güvenlik önlemlerini tetikleyebilir ve geçici hizmet kesintilerine neden olabilir.

* **IP Engelleme:** Tekrarlayan veya agresif veri çekme davranışları, IP adresinizin web sitesine erişimini geçici veya kalıcı olarak engellemesine yol açabilir.

Bu sorunlardan kaçınmak ve sorunsuz bir işlem sağlamak için aşağıdaki önerileri dikkate alabilirsiniz.

* Taleplerinizin hızını, web sitesinin kapasitesini dikkate alarak makul bir seviyede tutun.

* Sıkça çekilen verileri yerel olarak saklamaya çalışın. Böylece tekrarlayan taleplere gerek kalmayacaktır.

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
pip install isyatirimhisse==5.0.0
```

Yüklü paketin versiyonuna aşağıdaki komut yardımıyla ulaşabilirsiniz.

```bash
pip show isyatirimhisse
```

## Kullanım

### Kütüphanenin İçeri Aktarılması

```python
from isyatirimhisse import fetch_stock_data, fetch_index_data, fetch_financials
```

### Fonksiyonlar ve Parametreleri

#### Hisse Senedi Verisi Çekme (`fetch_stock_data`)

```python
df = fetch_stock_data(
    symbols="THYAO",
    start_date="01-01-2023",
    end_date="18-07-2025",
    save_to_excel=True
)
```

* `symbols`: (str | list) - Bir veya birden fazla hisse kodu.
* `start_date`: (str) - Veri başlangıç tarihi, 'GG-AA-YYYY' formatında.
* `end_date`: (str, opsiyonel) - Veri bitiş tarihi, 'GG-AA-YYYY' formatında.
* `save_to_excel`: (bool, opsiyonel) - Sonuçları Excel dosyasına kaydet (varsayılan: False).

#### Endeks Verisi Çekme (`fetch_index_data`)

```python
df = fetch_index_data(
    indices="XU100",
    start_date="01-01-2023",
    end_date="18-07-2025",
    save_to_excel=True
)
```

* `indices`: (str | list) - Bir veya birden fazla endeks kodu.
* `start_date`: (str) - Veri başlangıç tarihi, 'GG-AA-YYYY' formatında.
* `end_date`: (str, opsiyonel) - Veri bitiş tarihi, 'GG-AA-YYYY' formatında.
* `save_to_excel`: (bool, opsiyonel) - Sonuçları Excel dosyasına kaydet (varsayılan: False).

#### Finansal Tablo Verisi Çekme (`fetch_financials`)

```python
df = fetch_financials(
    symbols="THYAO",
    start_year=2023,
    end_year=2025,
    exchange="TRY",
    financial_group='1',
    save_to_excel=True
)
```

* `symbols`: (str | list) - Bir veya birden fazla hisse kodu.
* `start_year`: (int | str) - Başlangıç yılı.
* `end_year`: (int | str, opsiyonel) - Bitiş yılı.
* `exchange`: (str, opsiyonel) - Döviz türü ('TRY' veya 'USD'), varsayılan 'TRY'.
* `financial_group`: (str) - Finansal tablo grubu.
  * '1': XI_29
  * '2': UFRS
  * '3': UFRS_K
* `save_to_excel`: (bool, opsiyonel) - Sonuçları Excel dosyasına kaydet (varsayılan: False).

### İpuçları:

* Birden fazla hisse veya endeks ile çalışırken, string yerine mutlaka köşeli parantezli (`[]`) liste kullanınız.
* Liste girilmediği durumda, tek bir sembol için doğrudan string yazabilirsiniz.

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

### v5.0.0 - 19/07/2025

* Sınıf yapısı kaldırıldı, fonksiyon tabanlı API yapısına geçildi.
* `fetch_stock_data`, `fetch_index_data`, `fetch_financials` fonksiyonları eklendi.
* Kod ve dökümantasyon sadeleştirildi.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır.

## For those who prefer English:

## Description

`isyatirimhisse` is a Python library developed to easily fetch stock, index, and financial statement data from the Is Investment website.

*** WARNING ***

`isyatirimhisse` is not the official library of Is Investment Securities Inc. and has not been verified by the company. Before using the library, users should review Is Investment Securities Inc.'s terms of use and rights regarding data access. `isyatirimhisse` is designed for personal use only.

When using the Python package to access stock and financial statement data from the Is Investment website, it is very important to be aware of the potential consequences of sending excessive requests. Excessive requests can cause various negative effects, such as:

* **Performance Impact:** Sending too many requests in a short period can seriously affect the performance and response speed of the Is Investment website.

* **Service Disruption:** Intensive data fetching operations can trigger the website’s security measures and cause temporary service interruptions.

* **IP Blocking:** Repetitive or aggressive data fetching behaviors can cause your IP address to be temporarily or permanently blocked from accessing the website.

To avoid these issues and ensure smooth operation, please consider the following recommendations:

* Keep the speed of your requests at a reasonable level, considering the website's capacity.

* Try to store frequently fetched data locally, so you won’t need to make repetitive requests.

Following these rules will minimize the risk of interruption and help ensure that the Is Investment website provides a reliable experience for both you and other users.

## Installation

To use the library, follow these steps:

1. Install Python on your system: https://www.python.org/downloads/

2. Open the terminal and run the following command to install the package:

```bash
pip install isyatirimhisse
```

If you want to install a specific version, run the command as shown below:

```bash
pip install isyatirimhisse==5.0.0
```

You can check the installed package version using the following command:

```bash
pip show isyatirimhisse
```

## Usage

### Importing the Library

```python
from isyatirimhisse import fetch_stock_data, fetch_index_data, fetch_financials
```

### Functions and Parameters

#### Fetching Stock Data (`fetch_stock_data`)

```python
df = fetch_stock_data(
    symbols="THYAO",
    start_date="01-01-2023",
    end_date="18-07-2025",
    save_to_excel=True
)
```

* `symbols`: (str | list) - One or more stock tickers.
* `start_date`: (str) - Start date for the data, in 'DD-MM-YYYY' format.
* `end_date`: (str, optional) - End date for the data, in 'DD-MM-YYYY' format.
* `save_to_excel`: (bool, optional) - Save results to an Excel file (default: False).

#### Fetching Index Data (`fetch_index_data`)

```python
df = fetch_index_data(
    indices="XU100",
    start_date="01-01-2023",
    end_date="18-07-2025",
    save_to_excel=True
)
```

* `indices`: (str | list) - One or more index codes.
* `start_date`: (str) - Start date for the data, in 'DD-MM-YYYY' format.
* `end_date`: (str, optional) - End date for the data, in 'DD-MM-YYYY' format.
* `save_to_excel`: (bool, optional) - Save results to an Excel file (default: False).

#### Fetching Financial Statement Data (`fetch_financials`)

```python
df = fetch_financials(
    symbols="THYAO",
    start_year=2023,
    end_year=2025,
    exchange="TRY",
    financial_group='1',
    save_to_excel=True
)
```

* `symbols`: (str | list) - One or more stock tickers.
* `start_year`: (int | str) - Start year.
* `end_year`: (int | str, optional) - End year.
* `exchange`: (str, optional) - Currency ('TRY' or 'USD'), default is 'TRY'.
* `financial_group`: (str) - Financial statement group.
  * '1': XI_29
  * '2': IFRS
  * '3': IFRS_K
* `save_to_excel`: (bool, optional) - Save results to an Excel file (default: False).

### Tips

* When working with multiple stocks or indices, always use a list with square brackets (`[]`) instead of a string.
* For a single symbol, you can provide it directly as a string.

## Notes

* The library depends on the data available on the Is Investment website. Therefore, please check the relevant website for the accuracy and continuity of the data: [IS Investment](https://www.isyatirim.com.tr/tr-tr/Sayfalar/default.aspx)
* I welcome your feedback and contributions for the development and improvement of the library. Please contribute to the GitHub repo: [GitHub Repo](https://github.com/urazakgul/isyatirimhisse)
* For any problems or suggestions, please open a new issue in the "Issues" section of the GitHub repo: [GitHub Issues](https://github.com/urazakgul/isyatirimhisse/issues)

## Release Notes

### v0.1.0 - 25/07/2023

* First release.

### v0.1.1 - 27/07/2023

* Updated conditional statements checking parameters in the `veri_cek` function.
* Removed the `json` library.
* Added HTTP code `200` condition to the `veri_cek` function and started tracking it.

### v0.2.0 - 30/07/2023

* Added the `veri_gorsel` function, providing visualization in 3 different data types.
* Added parameters to the `veri_cek` function to save pandas DataFrame as Excel.

### v0.2.1 - 31/07/2023

* Fixed the installation error present in version 0.2.0.
* Fixed Turkish character problems in the documentation.
* Made previously invisible images in the documentation visible.

### v1.0.0 - 05/08/2023

* Functions translated into English:
  * `veri_cek` -> `fetch_data`
  * `veri_gorsel` -> `visualize_data`
* Added the `fetch_financials` function for fetching financial statements.
* Added the option to receive outputs in both English and Turkish.
* Updated the `fetch_data` function to fetch USD-based as well as TRY-based prices.
* Extended **kwargs in the `visualize_data` function to allow extra features.
* Updated documentation to be available in both Turkish and English.

### v2.0.0 - 10/08/2023

* Changed the `currency` parameter in the `fetch_data` function to `exchange`.
* Removed the `selenium` dependency from the `fetch_financials` function.
* Updated the `fetch_financials` function to fetch financial statements as a single table.
* Renamed `start_period` and `end_period` parameters to `start_year` and `end_year` in the `fetch_financials function`.
* Added `exchange` and `financial_group` parameters to the `fetch_financials` function.
* Added more checks and validation to both `fetch_data` and `fetch_financials`.

### v2.1.0 - 12/08/2023

* Added `stock_market_index` parameter to the `fetch_data` function for index data.
* Removed spaces in the items of financial statements fetched with `fetch_financials`.

### v2.1.1 - 13/08/2023

* Requests sent with the `fetch_data` function will be checked.

### v2.1.2 - 13/08/2023

* Fixed a code bug present in version 2.1.1.

### v2.1.3 - 13/08/2023

* Improved time restriction for requests sent.

### v3.0.0 - 19/08/2023

* `fetch_data` function made asynchronous.
* Symbol parameter in `fetch_data` limited to 400 symbols.
* The way `visualize_data` is executed changed due to asynchronous structure.

### v3.0.1 - 20/08/2023

* Fixed date range problem in data frames.

### v3.0.2 - 05/10/2023

* Removed the 400-symbol limit.

### v4.0.0 - 07/10/2023

* Created two classes: `StockData` and `Financials`.
* Updated parameters for the `get_data` methods of both classes.
* Modified the structure of table outputs.
* Removed data visualization feature.
* Removed asynchronous structure.

### v5.0.0 - 19/07/2025

* Removed class structure; switched to a function-based API.
* Added `fetch_stock_data`, `fetch_index_data`, and `fetch_financials` functions.
* Simplified code and documentation.

## License

This project is licensed under the MIT License.