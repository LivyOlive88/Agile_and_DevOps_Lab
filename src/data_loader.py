"""
data_loader.py - Data Loading Utilities

This module provides functions to load the flight price dataset
from CSV format into a Pandas DataFrame.

User Story: US-01 (Data Loading & Inspection)
"""

import os
import pandas as pd
from src.logger import setup_logger

logger = setup_logger(__name__)


def load_dataset(filepath: str) -> pd.DataFrame:
    """
    Load the flight price dataset from a CSV file.

    Parameters
    ----------
    filepath : str
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded dataset as a Pandas DataFrame.

    Raises
    ------
    FileNotFoundError
        If the specified file does not exist.
    ValueError
        If the file is empty or cannot be parsed.
    """
    if not os.path.exists(filepath):
        logger.error("File not found: %s", filepath)
        raise FileNotFoundError(f"Dataset file not found: {filepath}")

    logger.info("Loading dataset from: %s", filepath)

    try:
        df = pd.read_csv(filepath)
    except pd.errors.EmptyDataError:
        logger.error("The file is empty.")
        raise ValueError("The CSV file is empty and cannot be loaded.")
    except pd.errors.ParserError as e:
        logger.error("Error parsing CSV: %s", e)
        raise ValueError(f"Error parsing the CSV file: {e}")

    logger.info(
        "Dataset loaded successfully: %d rows, %d columns",
        df.shape[0], df.shape[1]
    )
    return df


def inspect_dataset(df: pd.DataFrame) -> dict:
    """
    Perform initial inspection of the dataset and return a summary.

    Parameters
    ----------
    df : pd.DataFrame
        The loaded dataset.

    Returns
    -------
    dict
        A dictionary containing inspection results:
        - shape: tuple of (rows, columns)
        - columns: list of column names
        - dtypes: dict of column data types
        - missing_values: dict of missing value counts per column
        - duplicate_count: int count of duplicate rows
        - memory_usage: float memory usage in MB
    """
    logger.info("Inspecting dataset...")

    inspection = {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicate_count": int(df.duplicated().sum()),
        "memory_usage": round(
            df.memory_usage(deep=True).sum() / (1024 * 1024), 2
        ),
    }

    logger.info("Shape: %s", inspection["shape"])
    logger.info(
        "Missing values: %d total",
        sum(inspection["missing_values"].values())
    )
    logger.info("Duplicate rows: %d", inspection["duplicate_count"])
    logger.info("Memory usage: %.2f MB", inspection["memory_usage"])

    return inspection


if __name__ == "__main__":
    DATA_PATH = os.path.join("data", "flight_data.csv")

    try:
        dataset = load_dataset(DATA_PATH)
        inspection = inspect_dataset(dataset)
        print(f"\nDataset Shape: {inspection['shape'][0]} rows x {inspection['shape'][1]} columns")
        print(f"Memory Usage: {inspection['memory_usage']} MB")
        print(f"Duplicate Rows: {inspection['duplicate_count']}")
        print(f"\nColumns: {inspection['columns']}")
        print(f"\nMissing Values: {inspection['missing_values']}")
        print("\nFirst 5 Rows:")
        print(dataset.head())
    except (FileNotFoundError, ValueError) as e:
        logger.error("Failed to load dataset: %s", e)
