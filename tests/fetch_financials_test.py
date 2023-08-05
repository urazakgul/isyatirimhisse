import pytest
import os
import sys
from isyatirimhisse import fetch_financials

# Test Case 1
def test_fetch_data_case_1():

    symbol='AKBNK'
    start_period='2022/3'
    end_period='2023/3'
    save_to_excel=True
    language='tr'

    data = fetch_financials(
        symbol=symbol,
        start_period=start_period,
        end_period=end_period,
        save_to_excel=save_to_excel,
        language=language
    )

    assert len(data) > 0, "No data found."
    symbol_file = f'bilanco_{symbol}.xlsx'
    assert os.path.exists(symbol_file), f"{symbol_file} does not exist."

    print(data)

# Test Case 2
def test_fetch_data_case_2():

    symbols = ['AKBNK', 'THYAO']
    start_period = '2022/3'
    end_period = '2023/3'

    data = fetch_financials(
        symbol=symbols,
        start_period=start_period,
        end_period=end_period
    )

    assert len(data) > 0, "No data found."

    print(data)

# Test Case 3
def test_fetch_data_case_3():

    symbols = ['AKBNK', 'THYAO']
    start_period = '2022/3'
    end_period = '2023/3'
    language='tr'

    data = fetch_financials(
        symbol=symbols,
        start_period=start_period,
        end_period=end_period,
        language=language
    )

    thyao_bilanco = data['THYAO']['bilanco']

    assert len(thyao_bilanco) > 0, "No data found."

    print(thyao_bilanco)

# Test Case 4
def test_fetch_data_case_4():

    symbol='AKBNK'
    start_period='2022/3'
    end_period='2023/3'
    save_to_excel=True

    data = fetch_financials(
        symbol=symbol,
        start_period=start_period,
        end_period=end_period,
        save_to_excel=save_to_excel
    )

    assert len(data) > 0, "No data found."

    print(data)

# Test Case 5
def test_fetch_data_case_5():

    symbols = ['AKBNK', 'THYAO']
    start_period = '2022/3'
    end_period = '2023/3'

    data = fetch_financials(
        symbol=symbols,
        start_period=start_period,
        end_period=end_period
    )

    thyao_balance_sheet = data['THYAO']['balance_sheet']

    assert len(thyao_balance_sheet) > 0, "No data found."

    print(thyao_balance_sheet)

if __name__ == "__main__":
    tests_directory = os.path.dirname(os.path.abspath(__file__))
    isyatirimanaliz_directory = os.path.abspath(os.path.join(tests_directory, '..'))
    if os.path.exists(isyatirimanaliz_directory):
        sys.path.insert(0, isyatirimanaliz_directory)
        print(sys.path)
    else:
        print(f"The directory '{isyatirimanaliz_directory}' does not exist.")

    pytest.main([__file__])