"""
Main: 
    main: Loads a time series, computes its autocorrelation function,
    saves an ACF plot, and displays the plot
"""
from pathlib import Path
from typing import Optional
import pandas as pd
import matplotlib.pyplot as plt
from functions.analysis import compute_acf
from functions.data_loader import load_time_series
from functions.plotter import plot_acf
from functions.utils import check_dir

def main(
    input_file: str,
    datetime_col: Optional[str],
    value_col: str,
    output_dir: str,
    datetime_format: Optional[str] = None,
) -> None:
    """
    :param input_file: Path to the CSV file containing the time series
    :param datetime_col: Name of the datetime column
    :param value_col: Name of the numeric value column to analyze
    :param output_dir: Directory to save the generated plot
    :datetime_format: Format to convert datetime column
    :return: None
    """
    out_path = Path(output_dir)
    check_dir(out_path)

    series = load_time_series(
        input_file, 
        datetime_col=datetime_col, 
        value_col=value_col,
        datetime_format=datetime_format
    )

    acf_vals = compute_acf(series)

    fig_path = out_path / "acf_plot.png"
    plot_acf(acf_vals, fig_path)
    print(f"Saved ACF plot to {fig_path}")

    plt.show()

    return None

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Compute and plot ACF for a time series")
    parser.add_argument("input_file", help="Path to CSV file")
    parser.add_argument("value_col", help="Name of the numeric column")
    parser.add_argument("datetime_col", help="Name of the datetime column")
    parser.add_argument("output_dir", help="Directory to save plot", default="output")
    parser.add_argument("--datetime_format", help="Datetime format", default=None)
    
    args = parser.parse_args()
    
    main(
        input_file=args.input_file,
        value_col=args.value_col,
        datetime_col=args.datetime_col,
        output_dir=args.output_dir,
        datetime_format=args.datetime_format
    )