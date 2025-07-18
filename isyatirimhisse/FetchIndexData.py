import requests
import pandas as pd
from datetime import datetime
from typing import List, Optional, Union

BASE_URL_INDEX = "https://www.isyatirim.com.tr/_Layouts/15/IsYatirim.Website/Common/ChartData.aspx/IndexHistoricalAll"

def fetch_index_data(
    indices: Union[List[str], str],
    start_date: str,
    end_date: Optional[str] = None,
    save_to_excel: bool = False
) -> pd.DataFrame:
    """
    Fetch raw daily index data for one or multiple indices from the IS Investment API.

    Parameters
    ----------
    indices : str or list of str
        Index symbol or list of index symbols for which to fetch data.
    start_date : str
        Start date in 'dd-mm-yyyy' format.
    end_date : str, optional
        End date in 'dd-mm-yyyy' format. If not provided, defaults to today's date.
    save_to_excel : bool, default False
        If True, saves the resulting DataFrame as an Excel file in the current working directory.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing all columns returned by the IS Investment API, combined for all requested indices.
    """
    if isinstance(indices, str):
        indices = [indices]
    if not indices:
        raise ValueError("At least one index symbol must be provided.")
    if not start_date:
        raise ValueError("'start_date' is required in 'dd-mm-yyyy' format.")
    if end_date is None:
        end_date = datetime.now().strftime("%d-%m-%Y")

    try:
        start_dt = datetime.strptime(start_date, "%d-%m-%Y")
        start_date_api = start_dt.strftime("%Y%m%d") + "000000"
    except Exception:
        raise ValueError("start_date must be in 'dd-mm-yyyy' format.")

    try:
        end_dt = datetime.strptime(end_date, "%d-%m-%Y")
        end_date_api = end_dt.strftime("%Y%m%d") + "235959"
    except Exception:
        raise ValueError("end_date must be in 'dd-mm-yyyy' format.")

    data_frames = []
    for idx in indices:
        url = (
            f"{BASE_URL_INDEX}?period=1440"
            f"&from={start_date_api}&to={end_date_api}&endeks={idx}"
        )
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            json_data = response.json()
            raw = json_data.get("data", [])
            if not raw:
                print(f"[Info] No data found for index '{idx}'.")
                continue
            df = pd.DataFrame(raw, columns=["timestamp", "value"])
            df["date"] = pd.to_datetime(df["timestamp"], unit="ms").dt.date + pd.Timedelta(days=1)
            df["INDEX"] = idx
            df = df[["INDEX", "date", "value"]]
            df = df.rename(columns={"date": "DATE", "value": "VALUE"})
        except Exception as e:
            print(f"[Warning] Could not fetch data for index '{idx}': {e}")
            continue

        data_frames.append(df)

    if not data_frames:
        raise ValueError("No data was fetched for any index. Please check the indices and date ranges.")

    combined_data = pd.concat(data_frames, ignore_index=True)
    combined_data = combined_data.sort_values(by=["INDEX", "DATE"])

    if save_to_excel:
        file_name = f"indexdata_{datetime.now().strftime('%Y%m%d')}.xlsx"
        combined_data.to_excel(file_name, index=False)
        print(f"[Success] Data saved to '{file_name}'.")

    return combined_data