
from superpipe import (
    load_runs,
    average_score,
    best_score,
    consistency,
    most_consistent
)

# SELF-CHECK 1: Average score
assert average_score([80, 90, 100]) == 90

# SELF-CHECK 2: Best score
assert best_score([85, 91, 88]) == 91

# SELF-CHECK 3: Consistency
assert consistency([88, 90, 91]) == 3

# SELF-CHECK 4: Identical scores
assert consistency([90, 90, 90]) == 0

# SELF-CHECK 5: Exclude athletes with one score
sample = {
    "Skier One": [85, 90],
    "Skier Two": [95]
}
assert most_consistent(sample) == ["Skier One"]

# SELF-CHECK 6: Two athletes can tie
sample = {
    "Skier One": [80, 85],
    "Skier Two": [90, 95]
}
assert most_consistent(sample) == ["Skier One", "Skier Two"]


# --------------------------------------------
# Tests for the real CSV dataset
# --------------------------------------------

runs = load_runs()

# SELF-CHECK 7: All three years are loaded
assert set(runs.keys()) == {2024, 2025, 2026}

# SELF-CHECK 8: Each year contains a final round
for year in (2024, 2025, 2026):
    assert "final" in runs[year]

# SELF-CHECK 9: Correct number of athletes
expected_athletes = {
    2024: 3,
    2025: 4,
    2026: 8
}

for year, expected in expected_athletes.items():
    assert len(runs[year]["final"]) == expected

# SELF-CHECK 10: Correct number of recorded runs
expected_runs = {
    2024: 9,
    2025: 8,
    2026: 23
}

for year, expected in expected_runs.items():
    actual = sum(
        len(scores)
        for scores in runs[year]["final"].values()
    )
    assert actual == expected

# SELF-CHECK 11: Scores are numeric floats
for year, rounds in runs.items():
    for round_name, athletes in rounds.items():
        for athlete, scores in athletes.items():
            assert all(isinstance(score, float) for score in scores)

print("All 11 SELF-CHECK tests passed!")
