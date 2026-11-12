# XGames-SuperPipe-Analysis
Python analysis of Women's Ski SuperPipe competition results from 2024–2026.
**Dataset:** `data/superpipe_runs.csv` contains recorded final-run scores.
**Structure:** Scores are loaded into dictionaries of lists using `superpipe.py`.
**Question 1:** Which athlete has the most consistent scores?
**Question 2:** Which athlete has the highest average score?
**Question 3:** Which athlete has the highest individual score?
**Analysis:** `analysis.py` calculates statistics and generates Matplotlib graphs.
**Run:** `python3 analysis.py` | **Tests:** `python3 test_superpipe.py`
**Sources:** X Games and PRIME Skiing; coverage is incomplete and one 2025 score remains disputed.