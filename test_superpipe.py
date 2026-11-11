from superpipe import (
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

# Example: an athlete with only one score is excluded
sample = {
    "Skier One": [85, 90],
    "Skier Two": [95]
}
assert most_consistent(sample) == ["Skier One"]

# Example: two athletes can tie
sample = {
    "Skier One": [80, 85],
    "Skier Two": [90, 95]
}
assert most_consistent(sample) == ["Skier One", "Skier Two"]


print("All 6 SELF-CHECK tests passed!")

