import pandas as pd
import pytest
import os
import sys
from isyatirimhisse import fetch_data, visualize_data

# Test Case 1
def test_visualize_data_line_plot_tr():
    data = fetch_data(
        symbol=['AKBNK', 'THYAO', 'GARAN', 'SISE', 'EREGL', 'BIMAS'],
        start_date='01-01-2013',
        end_date='31-07-2023'
    )

    visualize_data(
        df=data,
        plot_type='1',
        normalization=True,
        language='tr',
        linewidth=2,
        fontsize=14
    )

# Test Case 2
def test_visualize_data_line_plot_en():
    data = fetch_data(
        symbol=['AKBNK', 'THYAO', 'GARAN', 'SISE', 'EREGL', 'BIMAS'],
        start_date='01-01-2013',
        end_date='31-07-2023'
    )

    visualize_data(
        df=data,
        plot_type='1',
        normalization=True,
        linewidth=2,
        fontsize=14
    )

# Test Case 3
def test_visualize_data_heatmap_tr():
    data = fetch_data(
        symbol=['AKBNK', 'THYAO', 'GARAN', 'SISE', 'EREGL', 'BIMAS'],
        start_date='01-12-2012',
        end_date='31-07-2023',
        frequency='1m',
        calculate_return=True
    )

    visualize_data(
        df=data,
        plot_type='2',
        language='tr'
    )

# Test Case 4
def test_visualize_data_heatmap_en():
    data = fetch_data(
        symbol=['AKBNK', 'THYAO', 'GARAN', 'SISE', 'EREGL', 'BIMAS'],
        start_date='01-12-2012',
        end_date='31-07-2023',
        frequency='1m',
        calculate_return=True
    )

    visualize_data(
        df=data,
        plot_type='2'
    )

# Test Case 5
def test_visualize_data_scatter_matrix_tr():
    data = fetch_data(
        symbol=['AKBNK', 'THYAO', 'GARAN'],
        start_date='01-12-2012',
        end_date='31-07-2023',
        frequency='1m',
        calculate_return=True
    )

    visualize_data(
        df=data,
        plot_type='3',
        language='tr',
        alpha=0.1
    )

# Test Case 6
def test_visualize_data_scatter_matrix_en():
    data = fetch_data(
        symbol=['AKBNK', 'THYAO', 'GARAN'],
        start_date='01-12-2012',
        end_date='31-07-2023',
        frequency='1m',
        calculate_return=True
    )

    visualize_data(
        df=data,
        plot_type='3',
        alpha=0.1
    )

if __name__ == "__main__":
    tests_directory = os.path.dirname(os.path.abspath(__file__))
    your_module_directory = os.path.abspath(os.path.join(tests_directory, '..'))
    if os.path.exists(your_module_directory):
        sys.path.insert(0, your_module_directory)
        print(sys.path)
    else:
        print(f"The directory '{your_module_directory}' does not exist.")

    pytest.main([__file__])