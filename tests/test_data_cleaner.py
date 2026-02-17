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
    fix_invalid_fares,
    normalize_city_names,
    convert_data_types,
    clean_dataset
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


# ---------------------------------------------------------------
# Tests for normalize_city_names
# ---------------------------------------------------------------

class TestNormalizeCityNames:
    """Tests for the normalize_city_names function."""

    def test_normalizes_dhaka_variants(self):
        """Test that Dacca/dacca/DACCA are converted to Dhaka."""
        df = pd.DataFrame({"Source": ["Dacca", "dacca", "DACCA", "Dhaka"]})
        result = normalize_city_names(df)
        assert (result["Source"] == "Dhaka").all()

    def test_normalizes_chittagong_variants(self):
        """Test that Chittagong variants are converted to Chattogram."""
        df = pd.DataFrame({"Destination": ["Chittagong", "chittagong", "CHITTAGONG"]})
        result = normalize_city_names(df)
        assert (result["Destination"] == "Chattogram").all()

    def test_strips_whitespace(self):
        """Test that leading/trailing whitespace is removed."""
        df = pd.DataFrame({"Source": [" Dhaka ", "Sylhet "]})
        result = normalize_city_names(df)
        assert result["Source"].iloc[0] == "Dhaka"
        assert result["Source"].iloc[1] == "Sylhet"

    def test_title_cases_other_cities(self):
        """Test that other city names are title-cased."""
        df = pd.DataFrame({"Source": ["cox's bazar", "sylhet"]})
        result = normalize_city_names(df)
        assert result["Source"].iloc[0] == "Cox'S Bazar"
        assert result["Source"].iloc[1] == "Sylhet"

    def test_handles_missing_columns(self):
        """Test that function handles missing Source/Destination columns."""
        df = pd.DataFrame({"Other": ["A", "B"]})
        result = normalize_city_names(df)
        assert result.equals(df)


# ---------------------------------------------------------------
# Tests for convert_data_types
# ---------------------------------------------------------------

class TestConvertDataTypes:
    """Tests for the convert_data_types function."""

    def test_converts_fares_to_float(self):
        """Test that fare columns are converted to float."""
        df = pd.DataFrame({
            "Base Fare": ["100", 200, "300.5"],
            "Total Fare": [150, "250", 350.5]
        })
        result = convert_data_types(df)
        assert pd.api.types.is_float_dtype(result["Base Fare"])
        assert pd.api.types.is_float_dtype(result["Total Fare"])
        assert result["Base Fare"].iloc[0] == 100.0

    def test_converts_dates_to_datetime(self):
        """Test that date columns are converted to datetime."""
        df = pd.DataFrame({"Date of Journey": ["2024-01-01", "15/01/2024"]})
        result = convert_data_types(df)
        assert pd.api.types.is_datetime64_any_dtype(result["Date of Journey"])

    def test_handles_invalid_numeric_conversion(self):
        """Test that invalid numeric strings become NaN."""
        df = pd.DataFrame({"Base Fare": ["100", "invalid", "200"]})
        result = convert_data_types(df)
        assert pd.isna(result["Base Fare"].iloc[1])

    def test_handles_invalid_date_conversion(self):
        """Test that invalid date strings become NaT."""
        df = pd.DataFrame({"Date": ["2024-01-01", "not-a-date"]})
        result = convert_data_types(df)
        assert pd.isna(result["Date"].iloc[1])


# ---------------------------------------------------------------
# Tests for clean_dataset (Integration Test)
# ---------------------------------------------------------------

class TestCleanDataset:
    """Tests for the main clean_dataset pipeline."""

    @pytest.fixture
    def dirty_df(self):
        """Create a dirty DataFrame with multiple issues."""
        data = {
            "Unnamed: 0": [0, 1, 2, 3],
            "Date": ["2024-01-01", "2024-01-02", "2024-01-01", "invalid"],
            "Source": ["Dacca", "Dhaka", "Dacca", "Sylhet"],
            "Base Fare": ["3000", -500, "3000", 4000],  # "3000"->3000, -500->Median
            "Total Fare": [3500, 3500, 3500, 4500]      # Duplicate row 0 & 2
        }
        return pd.DataFrame(data)

    def test_pipeline_execution(self, dirty_df):
        """Test that the pipeline executes all steps correctly."""
        result = clean_dataset(dirty_df)

        # 1. Check irrelevant columns dropped
        assert "Unnamed: 0" not in result.columns

        # 2. Check duplicates removed (Row 2 was duplicate of Row 0 but with different index)
        # However, due to "Unnamed" being unique, duplicates might not be caught if checked before drop.
        # clean_dataset drops irrelevant cols first, so duplicates should be caught.
        # Row 0: 2024-01-01, Dacca, 3000, 3500
        # Row 2: 2024-01-01, Dacca, 3000, 3500
        # These are identical after dropping "Unnamed: 0". One should be removed.
        # Original: 4 rows. Expected: 3 rows.
        assert len(result) == 3

        # 3. Check city normalization
        assert (result["Source"] == "Dhaka").sum() == 2 # Row 0 and Row 1 (Dacca->Dhaka)
        # Note: Dacca->Dhaka.
        # Row 0: Dacca -> Dhaka
        # Row 1: Dhaka -> Dhaka
        # Row 3: Sylhet -> Sylhet

        # 4. Check negative fare fixed
        # Row 1 had -500. Valid values: 3000, 4000. Median = 3500.
        assert (result["Base Fare"] > 0).all()

        # 5. Check data types
        assert pd.api.types.is_datetime64_any_dtype(result["Date"])
        assert pd.api.types.is_numeric_dtype(result["Base Fare"])

        # 6. Check NaT/NaN handling (imputation)
        # "invalid" date becomes NaT. handle_missing_values doesn't impute datetime by default strategy?
        # Let's check handle_missing_values implementation.
        # It handles "float64", "int64". Datetime is not explicit.
        # However, convert_data_types runs BEFORE handle_missing_values.
        # So "invalid" -> NaT. NaT is not float/int.
        # The mode strategy (else block) might pick it up?
        # NaT is like None.
        # Let's verify if "Date" remains NaT or gets filled.
        # Ideally we want it filled or dropped.
        # For this basic pipeline, if it's not numeric, it falls to 'else' -> mode or "Unknown".
        assert result["Date"].isnull().sum() == 0
