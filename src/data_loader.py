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


if __name__ == "__main__":
    DATA_PATH = os.path.join("data", "flight_data.csv")

    try:
        dataset = load_dataset(DATA_PATH)
        print(f"\nDataset Shape: {dataset.shape[0]} rows x {dataset.shape[1]} columns")
        print(f"\nColumns: {dataset.columns.tolist()}")
        print(f"\nFirst 5 Rows:")
        print(dataset.head())
    except (FileNotFoundError, ValueError) as e:
        logger.error("Failed to load dataset: %s", e)
