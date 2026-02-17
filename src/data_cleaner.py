"""
data_cleaner.py - Data Cleaning & Preprocessing

This module provides functions to clean and preprocess the flight price
dataset, handling missing values, duplicates, inconsistencies, and
type conversions.

User Story: US-02 (Data Cleaning & Preprocessing)
"""

import pandas as pd
from src.logger import setup_logger

logger = setup_logger(__name__)


def drop_irrelevant_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop irrelevant or unnamed columns from the dataset.

    Parameters
    ----------
    df : pd.DataFrame
        The raw dataset.

    Returns
    -------
    pd.DataFrame
        Dataset with irrelevant columns removed.
    """
    cols_to_drop = [
        col for col in df.columns
        if col.lower().startswith("unnamed") or col.lower() == "index"
    ]

    if cols_to_drop:
        logger.info("Dropping irrelevant columns: %s", cols_to_drop)
        df = df.drop(columns=cols_to_drop)
    else:
        logger.info("No irrelevant columns found to drop.")

    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows from the dataset.

    Parameters
    ----------
    df : pd.DataFrame
        The dataset.

    Returns
    -------
    pd.DataFrame
        Dataset with duplicates removed.
    """
    initial_count = len(df)
    df = df.drop_duplicates()
    removed_count = initial_count - len(df)

    logger.info(
        "Removed %d duplicate rows (%d -> %d)",
        removed_count, initial_count, len(df)
    )

    return df
