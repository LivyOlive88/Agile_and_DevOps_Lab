# Sprint 1 Retrospective

**Date:** 2026-02-17
**Sprint Goal:** Deliver first increment of working software (Data Loading & Cleaning) and establish DevOps pipeline.

## 1. What Went Well (Positives)
- **Incremental Delivery:** I successfully broke down the user stories into small, manageable commits (15 commits so far), adhering to the incremental approach outlined in the project brief.
- **Robustness:** The data cleaning pipeline is robust, handling edge cases like "Dacca" vs "Dhaka" and negative fares effectively.
- **Automated QA:** The CI pipeline caught a few linting issues early on, and having 40 passing unit tests gives me high confidence in the code's stability.
- **Logging:** Implementing a centralized logger (`src/logger.py`) early was a great decision, providing clear visibility into the pipeline's execution.

## 2. What Didn't Go Well (Negatives & Challenges)
- **Test Coverage Gap:** Initially, I added new cleaning functions (`handle_missing_values`) without immediately adding their corresponding tests. This meant the CI pipeline was "green" but wasn't actually testing the new code. I caught this and fixed it in Commit 11.
- **Image Handling:** I initially saved evidence screenshots to `outputs/images` which is gitignored, leading to broken links in the review document. I had to move them to `docs/images`.

## 3. Improvements for Sprint 2 (Action Items)
- **Strict TDD:** For the next sprint (EDA), I will write the test (or at least the test plan) *before* or *simultaneously* with the feature code to avoid coverage gaps.
- **Better Documentation Management:** I will store all documentation assets (diagrams, screenshots) directly in `docs/images` from the start to avoid path issues.
- **Visualization Quality:** For US-04, I will ensure all plots are saved with high DPI and self-contained titles/labels and legends to make the final report professional.

## 4. Reflection on Agile & DevOps
This sprint demonstrated the value of the "fail fast" philosophy. By running tests frequently, I caught issues with data types (e.g., float vs int inference) quickly. Using a project board (simulated via `sprint0_planning.md`) helped keep track of which stories were "In Progress" versus "Done".

**Confidence for Sprint 2:** High. The foundation (loader + cleaner + CI) is solid.