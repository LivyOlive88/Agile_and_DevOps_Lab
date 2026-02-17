# Sprint 2 Retrospective

**Date:** 2026-02-17
**Sprint Goal:** Implement Exploratory Data Analysis (EDA), Performance Monitoring, and deliver final documentation.

## 1. What Went Well (Positives)
- **Monitoring Decorator:** Using a Python decorator (`@track_performance`) was an elegant solution to monitor performance without cluttering the business logic. It kept the code clean and reusable.
- **Robust CI/CD:** Having the CI pipeline running on every push caught a major issue with `requirements.txt` encoding early on, preventing broken builds on other machines.
- **Visualization:** The automated plot generation works perfectly and saves high-quality images directly to the output folder.

## 2. What Didn't Go Well (Negatives & Challenges)
- **Environment Differences:** We encountered a tricky issue where PowerShell's `echo` command created a UTF-16 encoded `requirements.txt`, which broke `pip install` on the Linux CI runner. This taught us to be careful with cross-platform text handling.
- **Mocking Complex Dependencies:** Writing unit tests for plotting functions required mocking `matplotlib.pyplot`, which was a bit complex to get right but ultimately successful.

## 3. Improvements for Future Sprints (If Project continued)
- **Interactive Dashboards:** Instead of static PNGs, we could use Plotly or Streamlit for interactive data exploration.
- **Dockerization:** Containerizing the whole application would solve the environment discrepancies once and for all.
- **Advanced EDA:** We could add correlation matrices and outlier detection algorithms.

## 4. Final Project Reflection
This project successfully demonstrated the Agile/DevOps lifecycle. By breaking the work into small sprints and user stories, we maintained a steady pace of delivery. The automated testing and linting ensured high code quality throughout. The final pipeline is robust, documented, and ready for use.

**Result:** COMPLETE.
