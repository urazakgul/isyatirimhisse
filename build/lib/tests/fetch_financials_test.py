import pytest
import os
import sys
from datetime import datetime
from isyatirimhisse import fetch_financials

# Scenario 1: Symbol Not Entered
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_financials_no_symbol():

    start_year='2020'

    data = fetch_financials(
        start_year=start_year
    )

    assert len(data) > 0, "No data found."

    print(data)

# Scenario 2: Incorrect Symbol Entered
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_financials_incorrect_symbol():

    symbol='AKBNK.IS'
    start_year='2020'

    data = fetch_financials(
        symbol=symbol,
        start_year=start_year
    )

    assert len(data) > 0, "No data found."

    print(data)

# Scenario 3: Start Year Not Entered
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_financials_no_start_year():

    symbol='AKBNK'

    data = fetch_financials(
        symbol=symbol
    )

    assert len(data) > 0, "No data found."
    #symbol_file = f"financials_{symbol}_{datetime.now().strftime('%Y%m%d')}"
    #assert os.path.exists(symbol_file), f"{symbol_file} does not exist."

    print(data)

# Scenario 4: End Year Earlier Than Start Year
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_financials_end_year_earlier():

    symbol='AKBNK'
    start_year='2020'
    end_year='2019'

    data = fetch_financials(
        symbol=symbol,
        start_year=start_year,
        end_year=end_year
    )

    assert len(data) > 0, "No data found."

    print(data)

# Scenario 5: Incorrect Exchange Entered
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_financials_incorrect_exchange():

    symbol='AKBNK'
    start_year='2020'
    exchange='GBP'

    data = fetch_financials(
        symbol=symbol,
        start_year=start_year,
        exchange=exchange
    )

    assert len(data) > 0, "No data found."

    print(data)

# Scenario 6: Incorrect Financial Group Entered
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_financials_incorrect_financial_group():

    symbol='THYAO'
    start_year='2020'
    financial_group='4'

    data = fetch_financials(
        symbol=symbol,
        start_year=start_year,
        financial_group=financial_group
    )

    assert len(data) > 0, "No data found."

    print(data)

# Scenario 7: Incorrect Language Entered
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_financials_incorrect_language():

    symbol='THYAO'
    start_year='2020'
    language='de'

    data = fetch_financials(
        symbol=symbol,
        start_year=start_year,
        language=language
    )

    assert len(data) > 0, "No data found."

    print(data)

# Scenario 8: Incorrect Boolean Value (True as String) Entered
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_financials_incorrect_boolean_value():

    symbol='THYAO'
    start_year='2020'
    save_to_excel='True'

    data = fetch_financials(
        symbol=symbol,
        start_year=start_year,
        save_to_excel=save_to_excel
    )

    assert len(data) > 0, "No data found."

    print(data)

# Example 1
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_financials_example_1():

    symbol='THYAO'
    start_year='2022'
    end_year='2023'
    save_to_excel=True
    language='tr'

    data = fetch_financials(
        symbol=symbol,
        start_year=start_year,
        end_year=end_year,
        save_to_excel=save_to_excel,
        language=language
    )

    assert len(data) > 0, "No data found."

    print(data)

# Example 2
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_financials_example_2():

    symbols=['AKBNK', 'THYAO']
    start_year='2022'
    end_year='2023'
    financial_group='2'
    language='tr'

    data = fetch_financials(
        symbol=symbols,
        start_year=start_year,
        end_year=end_year,
        financial_group=financial_group,
        language=language
    )

    assert len(data) > 0, "No data found."

    print(data)

# Example 3
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_financials_example_3():

    symbols = ['AKBNK', 'THYAO']
    start_year = '2018'
    language='tr'
    exchange='USD'

    data = fetch_financials(
        symbol=symbols,
        start_year=start_year,
        language=language,
        exchange=exchange
    )

    thyao_finansallar = data['THYAO']

    assert len(thyao_finansallar) > 0, "No data found."

    print(thyao_finansallar)

# Example 4
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_financials_example_4():

    symbol=['THYAO','SISE']
    start_year='2022'
    end_year='2023'
    save_to_excel=True

    data = fetch_financials(
        symbol=symbol,
        start_year=start_year,
        end_year=end_year,
        save_to_excel=save_to_excel
    )

    assert len(data) > 0, "No data found."

    print(data)

if __name__ == "__main__":
    tests_directory = os.path.dirname(os.path.abspath(__file__))
    isyatirimanaliz_directory = os.path.abspath(os.path.join(tests_directory, '..'))
    if os.path.exists(isyatirimanaliz_directory):
        sys.path.insert(0, isyatirimanaliz_directory)
        print(sys.path)
    else:
        print(f"The directory '{isyatirimanaliz_directory}' does not exist.")

    pytest.main([__file__])