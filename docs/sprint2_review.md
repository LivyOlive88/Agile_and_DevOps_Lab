# Sprint 2 Review

**Date:** 2026-02-17
**Sprint Goal:** Implement Exploratory Data Analysis (EDA), Performance Monitoring, and deliver the final report.

## 1. Summary of Work Completed
I successfully completed all planned User Stories for Sprint 2, delivering a robust analytics module and finalizing the project documentation.

| ID | User Story | Status | Story Points |
|----|------------|--------|--------------|
| US-04 | Exploratory Data Analysis (EDA) | Done | 5 |
| US-05 | Pipeline Monitoring & Logging | Done | 3 |
| US-06 | Final Reporting & Documentation | Done | 2 |

**Total Story Points Delivered:** 10/10

## 2. Key Deliverables

### A. EDA Module (`src/eda.py`)
- implemented `compute_statistics` to generate summary stats (mean, median, etc.).
- implemented `plot_price_distribution` and `plot_price_over_time` using Matplotlib/Seaborn.
- **Evidence:**
  > *[Insert Screenshot of 'outputs/plots/price_distribution.png' here]*
  > *[Insert Screenshot of 'outputs/plots/price_trend.png' here]*

### B. Performance Monitoring (`src/monitor.py`)
- Created a `@track_performance` decorator that logs execution time and memory usage for key pipeline steps.
- Integrated into `data_cleaner.py` and `eda.py`.
- **Evidence:**
  > *[Insert Screenshot of log file with performance metrics]*

### C. Final Report Generator (`main.py`)
- Created an orchestration script that runs the entire pipeline end-to-end.
- Added `run_pipeline.bat` for easy execution on Windows.

## 3. Demo Script

To verify the Sprint 2 increment:
1. Run the pipeline:
   ```bash
   .\run_pipeline.bat
   ```
2. Check the `outputs/` folder for generated CSVs and Plots.
3. Check `logs/pipeline.log` to see performance metrics.

## 4. Definition of Done (DoD) Checklist

- [x] Code fulfills the requirements of the User Story.
- [x] Code follows PEP 8 standards and passes `flake8`.
- [x] Unit tests are written and passing (47 tests passed).
- [x] CI pipeline is passing on the main branch.
- [x] Documentation (README, Review) is updated.

## 5. Project Conclusion

The project is now complete. The pipeline successfully ingests raw flight data, cleans it, analyzes it, and produces actionable insights, all while adhering to Agile and DevOps best practices.
