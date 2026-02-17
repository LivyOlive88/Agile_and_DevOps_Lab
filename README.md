# Flight Fare Prediction - Data Analysis Pipeline

## Product Vision
To build a data analysis pipeline that explores and preprocesses Bangladesh flight fare data, uncovering pricing patterns, seasonal trends, and route-based insights through thorough data cleaning and exploratory data analysis.

## Project Overview
This project applies the full data science workflow for analyzing flight fares — from data loading and cleaning to exploratory data analysis (EDA) — while following **Agile principles** and **DevOps practices** throughout the development process.

## Problem Statement
Airlines and travel platforms need to understand ticket pricing patterns based on route, airline, and travel date. This project analyzes historical flight price data from Bangladesh to uncover fare trends, seasonal variations, and route-based pricing insights.

## Dataset
- **Source:** [Flight Price Dataset of Bangladesh](https://www.kaggle.com/) (Kaggle)
- **File:** `flight_data.csv`
- **Key Variables:** Airline, Source, Destination, Date, Base Fare, Tax & Surcharge, Total Fare

## Project Structure
```
Agile_and_DevOps/
|-- data/                          # Raw dataset
|   |-- flight_data.csv
|-- docs/                          # Agile & sprint documentation
|-- src/                           # Source code modules
|-- tests/                         # Unit and integration tests
|-- outputs/                       # Generated plots & reports
|   |-- plots/
|   |-- reports/
|-- .github/                       # CI/CD pipeline
|   |-- workflows/
|-- .gitignore
|-- requirements.txt
|-- README.md
```

## Getting Started

### Prerequisites
- Python 3.9+
- pip (Python package manager)

### Installation
```bash
# Clone the repository
git clone https://github.com/LivyOlive88/Agile_and_DevOps_Lab.git
cd Agile_and_DevOps_Lab

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Agile Methodology
This project follows an Agile approach with 3 sprints:

| Sprint | Focus | Status |
|--------|-------|--------|
| Sprint 0 | Planning & Setup | In Progress |
| Sprint 1 | Data Loading, Cleaning & Validation | Not Started |
| Sprint 2 | EDA, Monitoring & Reporting | Not Started |

