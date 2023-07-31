import pytest
import warnings
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

from isyatirimhisse import veri_cek, veri_gorsel

veriler_df = veri_cek(
    sembol=['AKBNK','THYAO','GARAN','SISE','EREGL','BIMAS'],
    baslangic_tarih='02-01-2013',
    bitis_tarih='28-07-2023',
    frekans='1g',
    getiri_hesapla=False
)

def test_veri_gorsel_with_no_df():
    # Test: If 'df' is not provided
    with pytest.raises(ValueError) as e:
        veri_gorsel()
    assert str(e.value) == "Veri çerçevesi (df) parametresi belirtilmelidir."

def test_veri_gorsel_with_non_dataframe_df():
    # Test: If 'df' is not a pandas DataFrame
    with pytest.raises(ValueError) as e:
        veri_gorsel(df=veriler_df.values)
    assert str(e.value) == "Veri çerçevesi (df) parametresi bir pandas DataFrame olmalıdır."

def test_veri_gorsel_with_empty_df():
    # Test: If 'df' is empty
    empty_df = pd.DataFrame(columns=['AKBNK','THYAO','GARAN','SISE','EREGL','BIMAS'])
    with pytest.raises(ValueError) as e:
        veri_gorsel(df=empty_df)
    assert str(e.value) == "Veri çerçevesi (df) boş olmamalıdır."

def test_veri_gorsel_with_invalid_normalizasyon():
    # Test: If 'normalization' is not True or False
    with pytest.raises(ValueError) as e:
        veri_gorsel(df=veriler_df, normalizasyon='Evet')
    assert str(e.value) == "Normalizasyon parametresi bir bool (True/False) değeri olmalıdır."

def test_veri_gorsel_with_invalid_gorsel_turu():
    # Test: If an invalid 'plot_type' parameter is provided
    with pytest.raises(ValueError) as e:
        veri_gorsel(df=veriler_df, gorsel_turu='0')
    assert str(e.value) == "Geçersiz görselleştirme türü. '1', '2' veya '3' olmalıdır."

def test_veri_gorsel_with_kwargs():
    # Test: Check if **kwargs are working
    linewidth = 5.0
    with warnings.catch_warnings(record=True) as caught_warnings:
        warnings.simplefilter("always")
        veri_gorsel(df=veriler_df, gorsel_turu='1', normalizasyon=True, linewidth=linewidth)
        warnings.warn("Test warning", UserWarning)

    # Check for captured warnings
    relevant_warnings = [warning for warning in caught_warnings if issubclass(warning.category, UserWarning)]
    assert len(relevant_warnings) >= 1, "A UserWarning should have been captured."

if __name__ == "__main__":
    pytest.main()