"""
main.py - Flight Fare Analysis Pipeline Entry Point

This script orchestrates the entire data processing pipeline:
1. Data Loading
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Report Generation

User Story: US-06 (Final Reporting)
"""

import sys
import os
from src.data_loader import load_dataset, inspect_dataset
from src.data_cleaner import clean_dataset
from src.eda import (
    compute_statistics,
    save_statistics,
    plot_price_distribution,
    plot_price_over_time,
    plot_correlation_matrix,
    plot_outliers
)
from src.logger import setup_logger

logger = setup_logger("main")


def main():
    """Execute the full data pipeline."""
    logger.info("Starting flight fare analysis pipeline...")

    # Define paths
    data_path = os.path.join("data", "flight_data.csv")
    output_dir = "outputs"
    
    # Check if data exists
    if not os.path.exists(data_path):
        logger.error("Data file not found at: %s", data_path)
        logger.info("Please ensure 'flight_data.csv' is in the 'data/' directory.")
        sys.exit(1)

    try:
        # Step 1: Load Data
        df = load_dataset(data_path)
        inspect_dataset(df)

        # Step 2: Clean Data
        df = clean_dataset(df)

        # Step 3: EDA & Visualization
        stats = compute_statistics(df)
        if not stats.empty:
            save_statistics(stats, os.path.join(output_dir, "reports"))
        
        plot_output_dir = os.path.join(output_dir, "plots")
        plot_price_distribution(df, plot_output_dir)
        plot_price_over_time(df, plot_output_dir)
        plot_correlation_matrix(df, plot_output_dir)
        plot_outliers(df, plot_output_dir)

        logger.info("Pipeline completed successfully! Check 'outputs/' for results.")

    except Exception as e:
        logger.critical("Pipeline failed: %s", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
