"""
test_data_cleaner.py - Unit Tests for Data Cleaning Module

Tests for the drop_irrelevant_columns and remove_duplicates
functions in src/data_cleaner.py.

User Story: US-03 (Data Validation & Quality Assurance)
"""

import pytest
import pandas as pd
from src.data_cleaner import drop_irrelevant_columns, remove_duplicates


# ---------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------

@pytest.fixture
def df_with_unnamed_columns():
    """Create a DataFrame with unnamed/irrelevant columns."""
    data = {
        "Unnamed: 0": [0, 1, 2],
        "index": [100, 101, 102],
        "Airline": ["Biman", "NovoAir", "US-Bangla"],
        "Base Fare": [3500.0, 4200.0, 3100.0],
        "Total Fare": [4000.0, 4800.0, 3550.0],
    }
    return pd.DataFrame(data)


@pytest.fixture
def df_without_unnamed_columns():
    """Create a DataFrame with no unnamed columns."""
    data = {
        "Airline": ["Biman", "NovoAir", "US-Bangla"],
        "Base Fare": [3500.0, 4200.0, 3100.0],
        "Total Fare": [4000.0, 4800.0, 3550.0],
    }
    return pd.DataFrame(data)


@pytest.fixture
def df_with_duplicates():
    """Create a DataFrame with duplicate rows."""
    data = {
        "Airline": ["Biman", "NovoAir", "Biman", "US-Bangla", "Biman"],
        "Source": ["Dhaka", "Dhaka", "Dhaka", "Chittagong", "Dhaka"],
        "Destination": ["Chittagong", "Sylhet", "Chittagong", "Dhaka", "Chittagong"],
        "Total Fare": [4000.0, 3200.0, 4000.0, 3550.0, 4000.0],
    }
    return pd.DataFrame(data)


@pytest.fixture
def df_without_duplicates():
    """Create a DataFrame with no duplicate rows."""
    data = {
        "Airline": ["Biman", "NovoAir", "US-Bangla"],
        "Source": ["Dhaka", "Dhaka", "Chittagong"],
        "Total Fare": [4000.0, 3200.0, 3550.0],
    }
    return pd.DataFrame(data)


# ---------------------------------------------------------------
# Tests for drop_irrelevant_columns
# ---------------------------------------------------------------

class TestDropIrrelevantColumns:
    """Tests for the drop_irrelevant_columns function."""

    def test_drops_unnamed_columns(self, df_with_unnamed_columns):
        """Test that 'Unnamed' columns are removed."""
        result = drop_irrelevant_columns(df_with_unnamed_columns)
        unnamed_cols = [
            col for col in result.columns
            if col.lower().startswith("unnamed")
        ]
        assert len(unnamed_cols) == 0

    def test_drops_index_column(self, df_with_unnamed_columns):
        """Test that 'index' column is removed."""
        result = drop_irrelevant_columns(df_with_unnamed_columns)
        assert "index" not in result.columns

    def test_keeps_relevant_columns(self, df_with_unnamed_columns):
        """Test that relevant columns are preserved."""
        result = drop_irrelevant_columns(df_with_unnamed_columns)
        assert "Airline" in result.columns
        assert "Base Fare" in result.columns
        assert "Total Fare" in result.columns

    def test_column_count_after_drop(self, df_with_unnamed_columns):
        """Test that exactly 2 irrelevant columns are dropped."""
        result = drop_irrelevant_columns(df_with_unnamed_columns)
        assert len(result.columns) == 3

    def test_no_columns_dropped_when_clean(self, df_without_unnamed_columns):
        """Test that no columns are dropped from a clean DataFrame."""
        result = drop_irrelevant_columns(df_without_unnamed_columns)
        assert len(result.columns) == 3

    def test_row_count_unchanged(self, df_with_unnamed_columns):
        """Test that row count is not affected by column dropping."""
        result = drop_irrelevant_columns(df_with_unnamed_columns)
        assert len(result) == 3


# ---------------------------------------------------------------
# Tests for remove_duplicates
# ---------------------------------------------------------------

class TestRemoveDuplicates:
    """Tests for the remove_duplicates function."""

    def test_removes_duplicate_rows(self, df_with_duplicates):
        """Test that duplicate rows are removed."""
        result = remove_duplicates(df_with_duplicates)
        assert len(result) == 3

    def test_no_duplicates_remain(self, df_with_duplicates):
        """Test that no duplicates remain after removal."""
        result = remove_duplicates(df_with_duplicates)
        assert result.duplicated().sum() == 0

    def test_no_change_when_no_duplicates(self, df_without_duplicates):
        """Test that DataFrame is unchanged when there are no duplicates."""
        result = remove_duplicates(df_without_duplicates)
        assert len(result) == 3

    def test_returns_dataframe(self, df_with_duplicates):
        """Test that the function returns a DataFrame."""
        result = remove_duplicates(df_with_duplicates)
        assert isinstance(result, pd.DataFrame)

    def test_columns_preserved_after_dedup(self, df_with_duplicates):
        """Test that all columns are preserved after deduplication."""
        result = remove_duplicates(df_with_duplicates)
        expected_cols = ["Airline", "Source", "Destination", "Total Fare"]
        assert list(result.columns) == expected_cols
