
import os
import shutil
import pandas as pd
import pytest
from src.eda import plot_correlation_matrix, plot_outliers

@pytest.fixture
def sample_numeric_df():
    """Create a sample DataFrame with numeric columns for correlation."""
    data = {
        "Base Fare": [100.0, 200.0, 300.0, 400.0, 500.0],
        "Total Fare": [150.0, 250.0, 350.0, 450.0, 550.0],
        "Duration": [1.0, 2.0, 3.0, 4.0, 5.0],
        "Non-Numeric": ["A", "B", "C", "D", "E"]
    }
    return pd.DataFrame(data)

@pytest.fixture
def output_dir():
    """Create a temporary output directory."""
    dir_path = "tests/test_outputs"
    os.makedirs(dir_path, exist_ok=True)
    yield dir_path
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)

def test_plot_correlation_matrix(sample_numeric_df, output_dir):
    """Test that correlation matrix plot is created."""
    plot_correlation_matrix(sample_numeric_df, output_dir)
    expected_file = os.path.join(output_dir, "correlation_matrix.png")
    assert os.path.exists(expected_file)
    assert os.path.getsize(expected_file) > 0

def test_plot_outliers(sample_numeric_df, output_dir):
    """Test that outlier plot is created."""
    plot_outliers(sample_numeric_df, output_dir)
    expected_file = os.path.join(output_dir, "fare_outliers.png")
    assert os.path.exists(expected_file)
    assert os.path.getsize(expected_file) > 0

def test_plot_correlation_matrix_insufficient_data(output_dir):
    """Test that no plot is created if not enough numeric columns."""
    df = pd.DataFrame({"Col1": [1, 2, 3]}) # Only 1 numeric col
    plot_correlation_matrix(df, output_dir)
    expected_file = os.path.join(output_dir, "correlation_matrix.png")
    assert not os.path.exists(expected_file)

def test_plot_outliers_missing_column(output_dir):
    """Test that no plot is created if Total Fare is missing."""
    df = pd.DataFrame({"Other": [1, 2, 3]})
    plot_outliers(df, output_dir)
    expected_file = os.path.join(output_dir, "fare_outliers.png")
    assert not os.path.exists(expected_file)
