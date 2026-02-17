# Sprint 0: Planning

## 1. Product Vision

**Vision Statement:**
To build a data analysis pipeline that explores and preprocesses Bangladesh flight fare data, uncovering pricing patterns, seasonal trends, and route-based insights through thorough data cleaning and exploratory data analysis. The pipeline will follow production-grade coding standards with automated testing, continuous integration, and comprehensive monitoring.

---

## 2. Product Backlog

### User Stories

| ID | User Story | Priority | Story Points | Sprint |
|----|-----------|----------|-------------|--------|
| US-01 | As a data scientist, I want to load and inspect the flight price dataset so that I can understand the data structure, size, and quality before processing. | High | 2 | Sprint 1 |
| US-02 | As a data scientist, I want to clean and preprocess the raw flight data so that it is free of missing values, duplicates, and inconsistencies for reliable analysis. | High | 4 | Sprint 1 |
| US-03 | As a data scientist, I want to validate the cleaned data and perform quality checks so that I can confirm the data is ready for analysis. | High | 2 | Sprint 1 |
| US-04 | As a data scientist, I want to perform exploratory data analysis with visualizations so that I can discover patterns, trends, and outliers in flight fares. | High | 5 | Sprint 2 |
| US-05 | As a data scientist, I want to add monitoring and logging to the pipeline so that I can track data processing steps and detect issues early. | Medium | 3 | Sprint 2 |
| US-06 | As a data scientist, I want to generate a summary report of EDA insights so that stakeholders can understand key findings from the data. | Medium | 2 | Sprint 2 |

**Total Story Points:** 18

---

### Detailed User Stories with Acceptance Criteria

#### US-01: Data Loading & Inspection
**As a** data scientist,
**I want to** load and inspect the flight price dataset,
**So that** I can understand the data structure, size, and quality before processing.

**Acceptance Criteria:**
- [ ] Dataset (`flight_data.csv`) is loaded successfully into a Pandas DataFrame
- [ ] `.info()` output is displayed showing column names, data types, and non-null counts
- [ ] `.describe()` output is displayed showing statistical summaries for numerical columns
- [ ] `.head()` and `.tail()` are used to preview the first and last rows
- [ ] Dataset shape (rows x columns) is documented
- [ ] Missing value counts per column are identified and documented
- [ ] Duplicate row count is identified and documented

**Story Points:** 2
**Priority:** High

---

#### US-02: Data Cleaning & Preprocessing
**As a** data scientist,
**I want to** clean and preprocess the raw flight data,
**So that** it is free of missing values, duplicates, and inconsistencies for reliable analysis.

**Acceptance Criteria:**
- [ ] Irrelevant or unnamed columns (e.g., "Unnamed", "Index") are dropped
- [ ] Duplicate rows are identified and removed
- [ ] Missing numerical values are imputed using median strategy
- [ ] Missing categorical values are imputed with mode or "Unknown"
- [ ] Negative or zero fare values are handled (replaced with median)
- [ ] Inconsistent city names are normalized (e.g., "Dhaka" vs "Dacca")
- [ ] Numeric columns (`Base Fare`, `Tax & Surcharge`, `Total Fare`) are cast to float
- [ ] Date columns are converted to `datetime` type
- [ ] A summary of all cleaning steps and their impact (rows before/after) is documented

**Story Points:** 4
**Priority:** High

---

#### US-03: Data Validation & Quality Assurance
**As a** data scientist,
**I want to** validate the cleaned data and perform quality checks,
**So that** I can confirm the data is ready for analysis.

**Acceptance Criteria:**
- [ ] Unit tests exist that validate the data loading functions
- [ ] Unit tests exist that validate each cleaning function
- [ ] All fare columns contain only positive values after cleaning
- [ ] No missing values remain in critical columns after cleaning
- [ ] Data types are verified to be correct after conversion
- [ ] A data quality report summarizing validation results is generated
- [ ] All tests pass in the CI pipeline

**Story Points:** 2
**Priority:** High

---

#### US-04: Exploratory Data Analysis & Visualizations
**As a** data scientist,
**I want to** perform exploratory data analysis with visualizations,
**So that** I can discover patterns, trends, and outliers in flight fares.

**Acceptance Criteria:**
- [ ] Descriptive statistics are summarized by airline, source, and destination
- [ ] Distribution plots (histograms) are created for `Total Fare`, `Base Fare`, and `Tax & Surcharge`
- [ ] Box plots show fare variation across airlines
- [ ] Bar chart shows average fare per airline
- [ ] Correlation heatmap is generated for numerical features
- [ ] Top 5 most expensive routes are identified
- [ ] Most popular route (highest flight frequency) is identified
- [ ] All visualizations have clear titles, labels, and legends
- [ ] Plots are saved to the `outputs/plots/` directory

**Story Points:** 5
**Priority:** High

---

#### US-05: Pipeline Monitoring & Logging
**As a** data scientist,
**I want to** add monitoring and logging to the pipeline,
**So that** I can track data processing steps and detect issues early.

**Acceptance Criteria:**
- [ ] Logging is implemented across all pipeline modules using Python's `logging` module
- [ ] Each major processing step logs start time, completion time, and record counts
- [ ] Warning logs are generated for data quality issues (missing values, invalid fares)
- [ ] Error handling with informative error messages is implemented
- [ ] A pipeline execution summary is logged at the end of each run
- [ ] Log output format includes timestamp, module name, level, and message

**Story Points:** 3
**Priority:** Medium

---

#### US-06: EDA Insights & Final Reporting
**As a** data scientist,
**I want to** generate a summary report of EDA insights,
**So that** stakeholders can understand key findings from the data.

**Acceptance Criteria:**
- [ ] Key findings from EDA are documented in a structured markdown report
- [ ] Average fare per airline is summarized
- [ ] Seasonal fare variation patterns are identified and documented
- [ ] Route-based pricing insights are documented
- [ ] All visualizations are referenced in the report with descriptions
- [ ] A non-technical summary of findings is included

**Story Points:** 2
**Priority:** Medium

---

## 3. Definition of Done (DoD)

A user story is considered **"Done"** when ALL of the following criteria are met:

1. **Code Complete:** All code for the story is written, functional, and follows Python best practices 
2. **Acceptance Criteria Met:** Every acceptance criterion listed for the story has been fulfilled
3. **Tested:** Unit tests or integration tests are written and passing for any utility functions or data processing logic
4. **Documented:** Code is commented, and any relevant documentation (README, markdown notes) is updated
5. **Version Controlled:** All changes are committed to Git with meaningful, descriptive commit messages
6. **CI Pipeline Passing:** The CI/CD pipeline runs successfully with no test failures or linting errors
7. **Peer Reviewed:** Code has been self-reviewed for quality and correctness
8. **Artifacts Generated:** Any required outputs (visualizations, tables, reports) are generated and saved

---

## 4. Sprint Plans

### Sprint 1 Plan
**Sprint Goal:** Establish the data foundation -- load, clean, and validate the flight price dataset while setting up the DevOps pipeline.

**Selected Stories:**

| ID | User Story | Story Points |
|----|-----------|-------------|
| US-01 | Data Loading & Inspection | 2 |
| US-02 | Data Cleaning & Preprocessing | 4 |
| US-03 | Data Validation & Quality Assurance | 2 |

**Sprint 1 Velocity Target:** 8 story points

**DevOps Tasks (Sprint 1):**
- Set up `.gitignore` for Python projects
- Create `requirements.txt` with project dependencies
- Set up GitHub Actions CI pipeline (linting + tests)
- Write unit tests for data loading and cleaning functions
- Establish project folder structure

---

### Sprint 2 Plan
**Sprint Goal:** Perform exploratory data analysis, add monitoring and logging to the pipeline, and generate a comprehensive insights report.

**Selected Stories:**

| ID | User Story | Story Points |
|----|-----------|-------------|
| US-04 | Exploratory Data Analysis & Visualizations | 5 |
| US-05 | Pipeline Monitoring & Logging | 3 |
| US-06 | EDA Insights & Final Reporting | 2 |

**Sprint 2 Velocity Target:** 10 story points

**DevOps Tasks (Sprint 2):**
- Apply improvements from Sprint 1 Retrospective
- Add monitoring and logging to the data pipeline
- Enhance CI pipeline with additional test coverage
- Final documentation updates

---

## 5. Effort Estimation Summary

| Sprint | Stories | Total Story Points | Focus Area |
|--------|---------|-------------------|------------|
| Sprint 0 | Planning | -- | Agile setup, backlog creation, project structure |
| Sprint 1 | US-01, US-02, US-03 | 8 | Data foundation, cleaning, validation, DevOps setup |
| Sprint 2 | US-04, US-05, US-06 | 10 | EDA, monitoring, reporting |

**Total Project Story Points:** 18

---

## 6. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Dataset has excessive missing data | Medium | High | Implement robust imputation strategies; document assumptions |
| CI/CD pipeline configuration issues | Low | Medium | Use established GitHub Actions templates; test locally first |
| Data quality issues not caught during cleaning | Medium | Medium | Implement comprehensive validation tests (US-03) |
| EDA visualizations are unclear or misleading | Low | Medium | Follow visualization best practices; add clear labels and titles |
| Time constraints for Sprint 2 scope | Medium | High | Prioritize US-04 and US-05; treat US-06 as a stretch goal |

