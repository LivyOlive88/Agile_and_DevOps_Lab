"""
eda.py - Exploratory Data Analysis

This module provides functions to perform statistical analysis and
generate visualizations for the flight price dataset.

User Story: US-04 (Exploratory Data Analysis)
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.logger import setup_logger

logger = setup_logger(__name__)


def compute_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute descriptive statistics for numerical columns.

    Parameters
    ----------
    df : pd.DataFrame
        The cleaned dataset.

    Returns
    -------
    pd.DataFrame
        Summary statistics (mean, median, std, min, max, etc.).
    """
    logger.info("Computing summary statistics...")
    
    # Select numerical columns
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    if numeric_df.empty:
        logger.warning("No numerical columns found for statistics.")
        return pd.DataFrame()

    stats = numeric_df.describe().T
    stats['median'] = numeric_df.median()
    
    logger.info("Statistics computed for %d columns.", len(stats))
    return stats


def save_statistics(stats: pd.DataFrame, output_dir: str = "outputs/reports"):
    """
    Save computed statistics to a CSV file.

    Parameters
    ----------
    stats : pd.DataFrame
        The statistics DataFrame.
    output_dir : str
        Directory to save the report.
    """
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "descriptive_statistics.csv")
    
    try:
        stats.to_csv(output_path)
        logger.info("Statistics saved to: %s", output_path)
    except Exception as e:
        logger.error("Failed to save statistics: %s", e)
        raise
