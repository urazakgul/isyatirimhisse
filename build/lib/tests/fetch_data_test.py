import pytest
import os
import sys
from isyatirimhisse import fetch_data

# Scenario 1: No Symbol Entered
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_data_no_symbol():

    start_date='03-01-2023'

    data = fetch_data(
        start_date=start_date
    )

    assert len(data) > 0, "No data found."

    print(data)

# Scenario 2: Start Date Not Entered
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_data_no_start_date():

    symbol='GARAN'

    data = fetch_data(
        symbol=symbol
    )

    assert len(data) > 0, "No data found."

    print(data)

# Scenario 3: Incorrect Frequency Entered
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_data_incorrect_frequency():

    symbol='GARAN'
    start_date='01-12-2021'
    frequency='1h'

    data = fetch_data(
        symbol=symbol,
        start_date=start_date,
        frequency=frequency
    )

    assert len(data) > 0, "No data found."

    print(data)

# Scenario 4: Incorrect Observation Entered
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_data_incorrect_observation():

    symbol='GARAN'
    start_date='02-01-2012'
    end_date='30-12-2022'
    frequency='1m'
    observation='median'

    data = fetch_data(
        symbol=symbol,
        start_date=start_date,
        end_date=end_date,
        frequency=frequency,
        observation=observation
    )

    assert len(data) > 0, "No data found."

    print(data)

# Scenario 5: Incorrect Symbol Entered
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_data_incorrect_symbol():

    symbol='GARAN.IS'
    start_date='02-01-2012'
    end_date='30-12-2022'

    data = fetch_data(
        symbol=symbol,
        start_date=start_date,
        end_date=end_date
    )

    assert len(data) > 0, "No data found."

    print(data)

# Scenario 6: Incorrect Language Entered
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_data_incorrect_language():

    symbol='GARAN.IS'
    start_date='02-01-2012'
    end_date='30-12-2022'
    language='de'

    data = fetch_data(
        symbol=symbol,
        start_date=start_date,
        end_date=end_date,
        language=language
    )

    assert len(data) > 0, "No data found."

    print(data)

# Scenario 7: Incorrect Exchange Entered
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_data_incorrect_exchange():

    symbol='GARAN.IS'
    start_date='02-01-2012'
    end_date='30-12-2022'
    exchange='GBP'

    data = fetch_data(
        symbol=symbol,
        start_date=start_date,
        end_date=end_date,
        exchange=exchange
    )

    assert len(data) > 0, "No data found."

    print(data)

# Scenario 8: Incorrect Boolean Value (True as String) Entered
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_data_incorrect_boolean_value():

    symbol='GARAN.IS'
    start_date='02-01-2012'
    end_date='30-12-2022'
    calculate_return='True'

    data = fetch_data(
        symbol=symbol,
        start_date=start_date,
        end_date=end_date,
        calculate_return=calculate_return
    )

    assert len(data) > 0, "No data found."

    print(data)

# Scenario 9: End Date Earlier Than Start Date
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_data_end_date_earlier():

    symbol='GARAN.IS'
    start_date='02-01-2012'
    end_date='30-12-2021'

    data = fetch_data(
        symbol=symbol,
        start_date=start_date,
        end_date=end_date
    )

    assert len(data) > 0, "No data found."

    print(data)

# Example 1
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_data_example_1():

    symbol='GARAN'
    start_date='03-01-2023'

    data = fetch_data(
        symbol=symbol,
        start_date=start_date
    )

    assert len(data) > 0, "No data found."

    print(data)

# Example 2
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_data_example_2():

    symbol=['GARAN','THYAO']
    start_date='03-01-2023'
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

# Example 3
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_data_example_3():

    symbol=['GARAN','THYAO']
    start_date='01-12-2021'
    end_date='30-12-2022'
    frequency='1m'
    calculate_return=True
    log_return=False
    exchange='USD'

    data = fetch_data(
        symbol=symbol,
        start_date=start_date,
        end_date=end_date,
        frequency=frequency,
        calculate_return=calculate_return,
        log_return=log_return,
        exchange=exchange
    )

    assert len(data) > 0, "No data found."

    print(data)

# Example 4
# @pytest.mark.skip(reason="This test is currently disabled.")
def test_fetch_data_example_4():

    symbol=['EUPWR','THYAO']
    start_date='02-01-2012'
    end_date='30-12-2022'
    frequency='1y'
    drop_na=False
    save_to_excel=True
    language='tr'
    exchange='USD'

    data = fetch_data(
        symbol=symbol,
        start_date=start_date,
        end_date=end_date,
        frequency=frequency,
        drop_na=drop_na,
        save_to_excel=save_to_excel,
        language=language,
        exchange=exchange
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