"""
Data loading utilities:
    load_time_series: loads a csv and returns a pandas series indexed by the datetime column
"""
from __future__ import annotations
from pathlib import Path
from typing import Optional
import pandas as pd

def load_time_series(
    csv_path: str,
    datetime_col: str,
    value_col: str,
    datetime_format: Optional[str] = None
) -> pd.Series:
    """
    :param csv_path: Path to CSV file
    :param datetime_col: Name of the datetime column
    :param value_col: Name of the numeric column to analyze
    :param datetime_format: Optional format for datetime if in an odd format
    :return: pandas.Series indexed by datetime
    """

    csv_path = Path(csv_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"Input file not found: {csv_path}")

    df = pd.read_csv(csv_path)

    if datetime_col not in df.columns:
        raise ValueError(f"Datetime column '{datetime_col}' not found in CSV.")

    try:
        df[datetime_col] = pd.to_datetime(df[datetime_col], format=datetime_format, errors="raise")
    except Exception as exc:
        raise ValueError(
            f"Failed to parse datetime column '{datetime_col}'. "
            f"Consider passing the correct 'datetime_format'."
        ) from exc

    if value_col not in df.columns:
        raise ValueError(f"Value column '{value_col}' not found in CSV.")

    series = df.set_index(datetime_col)[value_col].sort_index()
    series = pd.to_numeric(series, errors="coerce").dropna()

    return series
