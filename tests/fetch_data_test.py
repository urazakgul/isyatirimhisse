import pytest
import os
import sys
from isyatirimhisse import fetch_data

# Test Case 1
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_data_case_1():

    symbol = 'GARAN'
    start_date = '03-01-2023'

    data = fetch_data(
        symbol=symbol,
        start_date=start_date
    )

    assert len(data) > 0, "No data found."

    print(data)

# Test Case 2
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_data_case_2():

    symbol=['GARAN','THYAO']
    start_date = '03-01-2023'
    frequency='1w'
    observation='mean'

    data = fetch_data(
        symbol=symbol,
        start_date=start_date,
        frequency=frequency,
        observation=observation
    )

    assert len(data) > 0, "No data found."

    print(data)

# Test Case 3
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_data_case_3():

    symbol=['GARAN','THYAO']
    start_date='01-12-2021'
    end_date='30-12-2022'
    frequency='1m'
    calculate_return=True
    log_return=False
    currency='USD'

    data = fetch_data(
        symbol=symbol,
        start_date=start_date,
        end_date=end_date,
        frequency=frequency,
        calculate_return=calculate_return,
        log_return=log_return,
        currency=currency
    )

    assert len(data) > 0, "No data found."

    print(data)

# Test Case 4
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_data_case_4():

    symbol=['EUPWR','THYAO']
    start_date='02-01-2012'
    end_date='30-12-2022'
    frequency='1y'
    drop_na=False
    save_to_excel=True
    language='tr'
    currency='USD'

    data = fetch_data(
        symbol=symbol,
        start_date=start_date,
        end_date=end_date,
        frequency=frequency,
        drop_na=drop_na,
        save_to_excel=save_to_excel,
        language=language,
        currency=currency
    )

    assert len(data) > 0, "No data found."

    print(data)

# Test Case 5
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_data_case_5():

    symbol=['EUPWR','THYAO']
    start_date='02-01-2012'
    end_date='30-12-2022'
    frequency='1y'
    drop_na=False
    save_to_excel=True
    currency='USD'

    data = fetch_data(
        symbol=symbol,
        start_date=start_date,
        end_date=end_date,
        frequency=frequency,
        drop_na=drop_na,
        save_to_excel=save_to_excel,
        currency=currency
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