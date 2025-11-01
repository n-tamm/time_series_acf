"""
Plotting utility functions:
    plot_acf: Creates and saves an autocorrelation stem plot
"""
from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

def plot_acf(acf_values: pd.Series, out_path: str) -> None:
    """
    :param acf_values: Series indexed by lag
    :param out_path: Path to save PNG
    :return: None
    """
    out_path = Path(out_path)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.stem(acf_values.index, acf_values.values)
    ax.set_xlabel("Lag")
    ax.set_ylabel("ACF")
    ax.set_title("Autocorrelation (ACF)")
    ax.grid(True, linestyle=":", linewidth=0.5)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
