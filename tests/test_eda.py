"""
test_eda.py - Unit Tests for Exploratory Data Analysis Module

Tests for the compute_statistics, save_statistics, and plotting functions
in src/eda.py.

User Story: US-04 (Exploratory Data Analysis)
"""

import os
import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from src.eda import (
    compute_statistics,
    save_statistics,
    plot_price_distribution,
    plot_price_over_time
)


# ---------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------

@pytest.fixture
def sample_numeric_df():
    """Create a DataFrame with numeric columns."""
    data = {
        "Base Fare": [100.0, 200.0, 300.0, 400.0, 500.0],
        "Total Fare": [150.0, 250.0, 350.0, 450.0, 550.0],
        "Category": ["A", "B", "A", "B", "A"]
    }
    return pd.DataFrame(data)


@pytest.fixture
def sample_time_series_df():
    """Create a DataFrame for time series plotting."""
    data = {
        "Date": pd.to_datetime(["2024-01-01", "2024-01-02", "2024-01-03"]),
        "Total Fare": [3000.0, 3200.0, 3100.0]
    }
    return pd.DataFrame(data)


# ---------------------------------------------------------------
# Tests for compute_statistics
# ---------------------------------------------------------------

class TestComputeStatistics:
    """Tests for the compute_statistics function."""

    def test_computes_stats_for_numeric_cols(self, sample_numeric_df):
        """Test that statistics are computed for numeric columns only."""
        result = compute_statistics(sample_numeric_df)
        assert "Base Fare" in result.index
        assert "Total Fare" in result.index
        assert "Category" not in result.index

    def test_computes_correct_values(self, sample_numeric_df):
        """Test that mean and median are calculated correctly."""
        result = compute_statistics(sample_numeric_df)
        # Mean of [100, 200, 300, 400, 500] is 300
        assert result.loc["Base Fare", "mean"] == 300.0
        assert result.loc["Base Fare", "median"] == 300.0

    def test_returns_empty_if_no_numeric(self):
        """Test that empty DataFrame is returned if no numeric cols."""
        df = pd.DataFrame({"A": ["x", "y"]})
        result = compute_statistics(df)
        assert result.empty


# ---------------------------------------------------------------
# Tests for save_statistics
# ---------------------------------------------------------------

class TestSaveStatistics:
    """Tests for the save_statistics function."""

    def test_creates_output_file(self, sample_numeric_df, tmp_path):
        """Test that the CSV file is created."""
        stats = compute_statistics(sample_numeric_df)
        output_dir = str(tmp_path / "reports")
        
        save_statistics(stats, output_dir)
        
        expected_file = os.path.join(output_dir, "descriptive_statistics.csv")
        assert os.path.exists(expected_file)


# ---------------------------------------------------------------
# Tests for plotting functions
# ---------------------------------------------------------------

class TestPlottingFunctions:
    """Tests for plot_price_distribution and plot_price_over_time."""

    @patch("src.eda.plt")
    def test_plot_price_distribution_calls_savefig(self, mock_plt, sample_numeric_df):
        """Test that price distribution plot saves a figure."""
        # Create a dummy DataFrame with the required Total Fare column
        df = pd.DataFrame({"Total Fare": [100.0, 200.0, 300.0]})
        
        plot_price_distribution(df, output_dir="dummy_dir")
        
        # Verify savefig was called
        mock_plt.savefig.assert_called_once()
        # Verify close was called to free memory
        mock_plt.close.assert_called_once()

    @patch("src.eda.plt")
    def test_plot_price_trend_calls_savefig(self, mock_plt):
        """Test that price trend plot saves a figure."""
        # Create a dummy DataFrame with Date and Total Fare
        df = pd.DataFrame({
            "Date": pd.to_datetime(["2024-01-01", "2024-01-02"]),
            "Total Fare": [3000.0, 3200.0]
        })
        
        plot_price_over_time(df, output_dir="dummy_dir")
        
        mock_plt.savefig.assert_called_once()
        mock_plt.close.assert_called_once()

    @patch("src.eda.plt")
    def test_plot_handles_missing_columns(self, mock_plt):
        """Test that functions return early if columns are missing."""
        df = pd.DataFrame({"A": [1, 2]})
        
        # Should NOT call savefig because columns are missing
        plot_price_distribution(df)
        plot_price_over_time(df)
        
        mock_plt.savefig.assert_not_called()
