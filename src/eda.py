"""
eda.py - Exploratory Data Analysis

This module provides functions to perform statistical analysis and
generate visualizations for the flight price dataset.

User Story: US-04 (Exploratory Data Analysis)
"""

import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from src.logger import setup_logger
from src.monitor import track_performance

logger = setup_logger(__name__)


@track_performance
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
        
        
def plot_price_distribution(df: pd.DataFrame, output_dir: str = "outputs/plots"):
    """
    Plot the distribution of Total Fare.

    Parameters
    ----------
    df : pd.DataFrame
        The cleaned dataset.
    output_dir : str
        Directory to save the plot.
    """
    if "Total Fare" not in df.columns:
        logger.warning("Total Fare column not found for plotting.")
        return

    os.makedirs(output_dir, exist_ok=True)
    plt.figure(figsize=(10, 6))
    
    sns.histplot(df["Total Fare"], kde=True, bins=30)
    plt.title("Distribution of Total Flight Fares")
    plt.xlabel("Total Fare (BDT)")
    plt.ylabel("Frequency")
    
    output_path = os.path.join(output_dir, "price_distribution.png")
    plt.savefig(output_path, dpi=300)
    plt.close()
    
    logger.info("Price distribution plot saved to: %s", output_path)


def plot_price_over_time(df: pd.DataFrame, output_dir: str = "outputs/plots"):
    """
    Plot the average Total Fare over time.

    Parameters
    ----------
    df : pd.DataFrame
        The cleaned dataset.
    output_dir : str
        Directory to save the plot.
    """
    date_cols = [c for c in df.columns if "date" in c.lower()]
    if not date_cols or "Total Fare" not in df.columns:
        logger.warning("Date or Fare column missing for time series plot.")
        return

    date_col = date_cols[0]
    
    # Calculate daily average fare
    daily_avg = df.groupby(date_col)["Total Fare"].mean().reset_index()
    
    os.makedirs(output_dir, exist_ok=True)
    plt.figure(figsize=(12, 6))
    
    sns.lineplot(data=daily_avg, x=date_col, y="Total Fare", marker="o")
    plt.title("Average Daily Flight Fare Trend")
    plt.xlabel("Date")
    plt.ylabel("Average Total Fare (BDT)")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.7)
    
    plt.tight_layout()
    output_path = os.path.join(output_dir, "price_trend.png")
    plt.savefig(output_path, dpi=300)
    plt.close()
    
    logger.info("Price trend plot saved to: %s", output_path)


def plot_correlation_matrix(df: pd.DataFrame, output_dir: str = "outputs/plots"):
    """
    Plot heatmap of correlation matrix for numerical features.

    Parameters
    ----------
    df : pd.DataFrame
        The cleaned dataset.
    output_dir : str
        Directory to save the plot.
    """
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    if numeric_df.empty or numeric_df.shape[1] < 2:
        logger.warning("Not enough numerical columns for correlation matrix.")
        return

    os.makedirs(output_dir, exist_ok=True)
    plt.figure(figsize=(10, 8))
    
    corr = numeric_df.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Correlation Matrix of Numerical Features")
    
    output_path = os.path.join(output_dir, "correlation_matrix.png")
    plt.savefig(output_path, dpi=300)
    plt.close()
    
    logger.info("Correlation matrix saved to: %s", output_path)


def plot_outliers(df: pd.DataFrame, output_dir: str = "outputs/plots"):
    """
    Plot boxplots for Total Fare to visualize outliers.

    Parameters
    ----------
    df : pd.DataFrame
        The cleaned dataset.
    output_dir : str
        Directory to save the plot.
    """
    if "Total Fare" not in df.columns:
        logger.warning("Total Fare column missing for outlier plot.")
        return

    os.makedirs(output_dir, exist_ok=True)
    plt.figure(figsize=(8, 6))
    
    sns.boxplot(y=df["Total Fare"])
    plt.title("Boxplot of Total Fare (Outlier Detection)")
    plt.ylabel("Total Fare (BDT)")
    
    output_path = os.path.join(output_dir, "fare_outliers.png")
    plt.savefig(output_path, dpi=300)
    plt.close()
    
    logger.info("Outlier plot saved to: %s", output_path)
