"""
test_data_loader.py - Unit Tests for Data Loading Module

Tests for the load_dataset and inspect_dataset functions
in src/data_loader.py.

User Story: US-03 (Data Validation & Quality Assurance)
"""

import os
import pytest
import pandas as pd
from src.data_loader import load_dataset, inspect_dataset


# ---------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------

@pytest.fixture
def sample_csv(tmp_path):
    """Create a temporary CSV file with sample flight data."""
    data = {
        "Airline": ["Biman", "NovoAir", "US-Bangla", "Biman", "NovoAir"],
        "Source": ["Dhaka", "Dhaka", "Chittagong", "Sylhet", "Dhaka"],
        "Destination": ["Chittagong", "Cox's Bazar", "Dhaka", "Dhaka", "Sylhet"],
        "Date": ["2024-01-15", "2024-02-10", "2024-03-05", "2024-01-20", "2024-04-12"],
        "Base Fare": [3500.0, 4200.0, 3100.0, 5000.0, 2800.0],
        "Tax & Surcharge": [500.0, 600.0, 450.0, 700.0, 400.0],
        "Total Fare": [4000.0, 4800.0, 3550.0, 5700.0, 3200.0],
    }
    df = pd.DataFrame(data)
    filepath = os.path.join(tmp_path, "test_flight_data.csv")
    df.to_csv(filepath, index=False)
    return filepath


@pytest.fixture
def empty_csv(tmp_path):
    """Create an empty CSV file."""
    filepath = os.path.join(tmp_path, "empty.csv")
    with open(filepath, "w") as f:
        f.write("")
    return filepath


@pytest.fixture
def sample_dataframe():
    """Create a sample DataFrame for inspection tests."""
    data = {
        "Airline": ["Biman", "NovoAir", "US-Bangla", "Biman"],
        "Base Fare": [3500.0, 4200.0, None, 5000.0],
        "Total Fare": [4000.0, 4800.0, 3550.0, 5700.0],
    }
    return pd.DataFrame(data)


# ---------------------------------------------------------------
# Tests for load_dataset
# ---------------------------------------------------------------

class TestLoadDataset:
    """Tests for the load_dataset function."""

    def test_load_valid_csv(self, sample_csv):
        """Test that a valid CSV file loads successfully."""
        df = load_dataset(sample_csv)
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 5
        assert len(df.columns) == 7

    def test_load_returns_correct_columns(self, sample_csv):
        """Test that loaded DataFrame has expected columns."""
        df = load_dataset(sample_csv)
        expected_cols = [
            "Airline", "Source", "Destination", "Date",
            "Base Fare", "Tax & Surcharge", "Total Fare"
        ]
        assert list(df.columns) == expected_cols

    def test_load_nonexistent_file_raises_error(self):
        """Test that FileNotFoundError is raised for missing files."""
        with pytest.raises(FileNotFoundError):
            load_dataset("nonexistent_file.csv")

    def test_load_empty_file_raises_error(self, empty_csv):
        """Test that ValueError is raised for empty files."""
        with pytest.raises(ValueError):
            load_dataset(empty_csv)


# ---------------------------------------------------------------
# Tests for inspect_dataset
# ---------------------------------------------------------------

class TestInspectDataset:
    """Tests for the inspect_dataset function."""

    def test_inspect_returns_dict(self, sample_dataframe):
        """Test that inspect_dataset returns a dictionary."""
        result = inspect_dataset(sample_dataframe)
        assert isinstance(result, dict)

    def test_inspect_contains_required_keys(self, sample_dataframe):
        """Test that inspection result has all required keys."""
        result = inspect_dataset(sample_dataframe)
        required_keys = [
            "shape", "columns", "dtypes",
            "missing_values", "duplicate_count", "memory_usage"
        ]
        for key in required_keys:
            assert key in result

    def test_inspect_shape_is_correct(self, sample_dataframe):
        """Test that reported shape matches the DataFrame."""
        result = inspect_dataset(sample_dataframe)
        assert result["shape"] == (4, 3)

    def test_inspect_detects_missing_values(self, sample_dataframe):
        """Test that missing values are correctly identified."""
        result = inspect_dataset(sample_dataframe)
        assert result["missing_values"]["Base Fare"] == 1

    def test_inspect_duplicate_count(self, sample_dataframe):
        """Test that duplicate count is calculated correctly."""
        result = inspect_dataset(sample_dataframe)
        assert result["duplicate_count"] == 0

    def test_inspect_memory_usage_positive(self, sample_dataframe):
        """Test that memory usage is a positive number."""
        result = inspect_dataset(sample_dataframe)
        assert result["memory_usage"] >= 0
