# Flight Fare Analysis Pipeline (Agile & DevOps Lab)

A robust data engineering pipeline for analyzing flight prices, built with Agile methodologies and DevOps best practices. This project automates data loading, cleaning, exploratory data analysis (EDA), and reporting.

## 🚀 Features

- **Automated Data Cleaning:** Handles missing values, duplicates, and inconsistent city names (e.g., "Dacca" -> "Dhaka").
- **Exploratory Data Analysis (EDA):** Generates statistical summaries and visualizations (Price Distribution, Price Trends).
- **Performance Monitoring:** Tracks execution time and memory usage for each pipeline step.
- **CI/CD Integration:** Automatically linted and tested via GitHub Actions.
- **Logging:** Centralized logging to both console and `logs/pipeline.log`.

## 📂 Project Structure

```
Agile_and_DevOps/
├── .github/workflows/    # CI/CD Pipeline Configuration
├── data/                 # Raw Dataset (flight_data.csv)
├── docs/                 # Documentation (Sprints, Reviews, Images)
├── logs/                 # Execution Logs
├── outputs/              # Generated Reports (Plots, CSVs)
├── src/                  # Source Code
│   ├── data_loader.py    # Data Ingestion
│   ├── data_cleaner.py   # Transformation Logic
│   ├── eda.py            # Analytics & Visualization
│   ├── monitor.py        # Performance Monitoring
│   ├── logger.py         # Logging Configuration
├── tests/                # Unit & Integration Tests
├── main.py               # Main Entry Point
├── run_pipeline.bat      # Windows Execution Script
├── requirements.txt      # Project Dependencies
└── README.md             # Project Documentation
```

## 🛠️ Usage

### Quick Start (Windows)
Double-click `run_pipeline.bat` or run:
```powershell
.\run_pipeline.bat
```

### Manual Execution
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the main script:
   ```bash
   python main.py
   ```
3. Run tests:
   ```bash
   pytest tests/ -v
   ```

## 📊 Outputs

After running the pipeline, check the `outputs/` directory:
- **`outputs/reports/descriptive_statistics.csv`**: Summary stats for numerical columns.
- **`outputs/plots/price_distribution.png`**: Histogram of flight prices.
- **`outputs/plots/price_trend.png`**: Line chart showing price trends over time.

## 🔄 DevOps Practices

- **Agile Sprints:** Development was broken into Sprint 0 (Planning), Sprint 1 (Core Pipeline), and Sprint 2 (EDA & Monitoring).
- **CI/CD:** GitHub Actions workflow runs `flake8` and `pytest` on every push.
- **TDD:** Unit tests were written to validate cleaning logic and ensure reliability.
