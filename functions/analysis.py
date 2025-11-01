"""
Analysis functions: 
    compute_acf: Computes autocorrelation values
"""
from __future__ import annotations
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import acf

def compute_acf(series: pd.Series, nlags: int = 48) -> pd.Series:
    """
    :param series: time-indexed series
    :param nlags: number of lags to compute
    :return: pandas.Series of ACF values indexed by the specified lag (0..nlags)
    """
    if series.empty:
        raise ValueError("Empty series provided to compute_acf")
    vals = acf(series.values, nlags=nlags, fft=True, missing="conservative")
    lags = np.arange(len(vals))

    return pd.Series(vals, index=lags)
