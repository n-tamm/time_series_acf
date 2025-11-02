"""
Main: 
    time_series_acf: Loads a time series, computes its autocorrelation function,
    saves an ACF plot, and displays the plot
"""
from pathlib import Path
from dataclasses import dataclass
from typing import Optional
import matplotlib.pyplot as plt
from functions.analysis import compute_acf
from functions.data_loader import load_time_series
from functions.plotter import plot_acf
from functions.utils import check_dir

# Using class to get around pylint param error
@dataclass
class ACF:
    """Holds parameters for running the autocorrelation analysis."""
    input_file: str
    datetime_col: Optional[str]
    value_col: str
    nlags: int
    output_dir: str
    plot_name: str = "acf_plot"
    datetime_format: Optional[str] = None

# Function uses help class ACF to control it's inputs
def time_series_acf(config: ACF) -> None:
    """
    :param input_file: Path to the CSV file containing the time series
    :param datetime_col: Name of the datetime column
    :param value_col: Name of the numeric value column to analyze
    :param nlags: Number of lags to compute acf on
    :param output_dir: Directory to save the generated plot
    :param plot_name: Name of the final plot to save in the output dir
    :datetime_format: Format to convert datetime column
    :return: None
    """
    out_path = Path(config.output_dir)
    check_dir(out_path)
    series = load_time_series(
        config.input_file,
        datetime_col=config.datetime_col,
        value_col=config.value_col,
        datetime_format=config.datetime_format
    )
    acf_vals = compute_acf(series, config.nlags)
    fig_path = out_path / f"{config.plot_name}.png"
    plot_acf(acf_vals, fig_path)
    print(f"Saved ACF plot to {fig_path}")
    plt.show()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Compute and plot ACF for a time series")
    parser.add_argument("input_file", help="Path to CSV file")
    parser.add_argument("value_col", help="Name of the numeric column")
    parser.add_argument("datetime_col", help="Name of the datetime column")
    parser.add_argument("nlags", type=int, help="Number of lags for the numeric column")
    parser.add_argument("--output_dir", help="Directory to save plot", default="output")
    parser.add_argument("--plot_name", help="Name to give saved plot", default="acf_plot")
    parser.add_argument("--datetime_format", help="Datetime format", default=None)
    args = parser.parse_args()
    acf_config = ACF(
        input_file=args.input_file,
        datetime_col=args.datetime_col,
        value_col=args.value_col,
        nlags=args.nlags,
        output_dir=args.output_dir,
        plot_name=args.plot_name,
        datetime_format=args.datetime_format,
    )
    time_series_acf(acf_config)
