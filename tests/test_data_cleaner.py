"""
test_data_cleaner.py - Unit Tests for Data Cleaning Module

Tests for the drop_irrelevant_columns and remove_duplicates
functions in src/data_cleaner.py.

User Story: US-03 (Data Validation & Quality Assurance)
"""

import pytest
import pandas as pd
from src.data_cleaner import (
    drop_irrelevant_columns,
    remove_duplicates,
    handle_missing_values,
    fix_invalid_fares
)


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


# ---------------------------------------------------------------
# Tests for handle_missing_values
# ---------------------------------------------------------------

class TestHandleMissingValues:
    """Tests for the handle_missing_values function."""

    @pytest.fixture
    def df_with_missing(self):
        """Create a DataFrame with missing values."""
        data = {
            "Numerical": [10.0, None, 30.0, 40.0, None],  # Median=30
            "Categorical": ["A", "B", None, "A", None],   # Mode=A
            "Other": [None, None, "C", "C", "C"]          # Mode=C
        }
        return pd.DataFrame(data)

    def test_imputes_numerical_with_median(self, df_with_missing):
        """Test that numerical columns are imputed with median."""
        result = handle_missing_values(df_with_missing)
        # Median of [10, 30, 40] is 30
        assert result["Numerical"].isnull().sum() == 0
        assert result["Numerical"].iloc[1] == 30.0
        assert result["Numerical"].iloc[4] == 30.0

    def test_imputes_categorical_with_mode(self, df_with_missing):
        """Test that categorical columns are imputed with mode."""
        result = handle_missing_values(df_with_missing)
        # Mode of ["A", "B", "A"] is "A"
        assert result["Categorical"].isnull().sum() == 0
        assert result["Categorical"].iloc[2] == "A"
        assert result["Categorical"].iloc[4] == "A"

    def test_handles_all_missing_column(self):
        """Test behavior when a column is entirely missing."""
        df = pd.DataFrame({"Empty": [None, None, None]})
        result = handle_missing_values(df)
        # Should fill with "Unknown" as mode is empty
        assert result["Empty"].isnull().sum() == 0
        assert result["Empty"].iloc[0] == "Unknown"

    def test_no_change_when_no_missing(self):
        """Test that complete DataFrames are unchanged."""
        df = pd.DataFrame({"A": [1, 2], "B": ["x", "y"]})
        result = handle_missing_values(df)
        assert result.isnull().sum().sum() == 0
        assert result.equals(df)


# ---------------------------------------------------------------
# Tests for fix_invalid_fares
# ---------------------------------------------------------------

class TestFixInvalidFares:
    """Tests for the fix_invalid_fares function."""

    @pytest.fixture
    def df_with_invalid_fares(self):
        """Create a DataFrame with negative and zero fares."""
        data = {
            "Base Fare": [3500.0, -500.0, 4000.0, 0.0],  # Median of valid (3500, 4000) = 3750
            "Tax & Surcharge": [500.0, 100.0, -50.0, 0.0],
            "Total Fare": [4000.0, -400.0, 0.0, 4500.0],
            "Other": [-100, 200, 300, 400]  # Should be ignored
        }
        return pd.DataFrame(data)

    def test_fixes_negative_fares(self, df_with_invalid_fares):
        """Test that negative fares are replaced."""
        result = fix_invalid_fares(df_with_invalid_fares)
        assert (result["Base Fare"] > 0).all()
        assert (result["Tax & Surcharge"] > 0).all()
        assert (result["Total Fare"] > 0).all()

    def test_fixes_zero_fares(self, df_with_invalid_fares):
        """Test that zero fares are replaced."""
        result = fix_invalid_fares(df_with_invalid_fares)
        assert (result["Base Fare"] != 0).all()

    def test_uses_median_for_replacement(self, df_with_invalid_fares):
        """Test that the replacement value is the median of valid entries."""
        # Valid Base Fares: 3500, 4000 -> Median 3750
        result = fix_invalid_fares(df_with_invalid_fares)
        # Index 1 was -500, Index 3 was 0
        assert result["Base Fare"].iloc[1] == 3750.0
        assert result["Base Fare"].iloc[3] == 3750.0

    def test_ignores_non_fare_columns(self, df_with_invalid_fares):
        """Test that non-identified fare columns are untouched."""
        result = fix_invalid_fares(df_with_invalid_fares)
        assert result["Other"].iloc[0] == -100  # Should remain negative

    def test_no_change_valid_fares(self):
        """Test that valid fares are unchanged."""
        df = pd.DataFrame({"Total Fare": [100.0, 200.0]})
        result = fix_invalid_fares(df)
        assert result.equals(df)
