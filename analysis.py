
from pathlib import Path
from statistics import pstdev

import matplotlib.pyplot as plt

from superpipe import (
    load_runs,
    average_score,
    best_score,
    consistency,
    most_consistent,
    highest_average,
    highest_single_score,
)


BASE = Path(__file__).resolve().parent
GRAPH_DIR = BASE / "graphs"
GRAPH_DIR.mkdir(exist_ok=True)

# Load the single source of data
run_data = load_runs()

# Combine all recorded final runs by athlete
athletes = {}

for year, rounds in sorted(run_data.items()):
    for athlete, scores in rounds.get("final", {}).items():
        athletes.setdefault(athlete, []).extend(scores)

# Answer three research questions
print("WOMEN'S SKI SUPERPIPE ANALYSIS (2024-2026)")
print("-" * 50)

print("1. Most consistent:", most_consistent(athletes))
print("2. Highest average:", highest_average(athletes))
print("3. Highest single score:", highest_single_score(athletes))

# Graph 1: Overall average scores
names = list(athletes.keys())
averages = [average_score(athletes[name]) for name in names]

plt.figure(figsize=(11, 5))
plt.bar(names, averages)
plt.title("X Games Aspen 2024-2026 - Average Recorded Final Run Scores")
plt.ylabel("Average Score")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(GRAPH_DIR / "average_scores.png")
plt.close()

# Graph 2: Highest individual run scores
highest = [best_score(athletes[name]) for name in names]

plt.figure(figsize=(11, 5))
plt.bar(names, highest)
plt.title("X Games Aspen 2024-2026 - Highest Recorded Final Run Scores")
plt.ylabel("Best Score")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(GRAPH_DIR / "highest_scores.png")
plt.close()

# Graph 3: Overall consistency
eligible = {
    name: scores
    for name, scores in athletes.items()
    if len(scores) >= 2
}

if eligible:
    ranges = [consistency(scores) for scores in eligible.values()]

    plt.figure(figsize=(11, 5))
    plt.bar(list(eligible.keys()), ranges)
    plt.title("X Games Aspen 2024-2026 - Recorded Score Ranges")
    plt.ylabel("Score Range (Lower = More Consistent)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(GRAPH_DIR / "consistency.png")
    plt.close()

print("\nGraphs saved in:", GRAPH_DIR)


# --------------------------------------------------
# Individual Run Analysis by Year
# --------------------------------------------------

for year, rounds in sorted(run_data.items()):
    if "final" not in rounds:
        continue

    athletes_runs = rounds["final"]

    print(f"\n{year} WOMEN'S SKI SUPERPIPE - FINAL RUNS")
    print("-" * 50)

    names = []
    averages = []
    best_scores = []
    ranges = []
    deviations = []

    for athlete, scores in athletes_runs.items():
        avg = average_score(scores)
        best = best_score(scores)
        score_range = consistency(scores)
        std_dev = pstdev(scores)

        names.append(athlete)
        averages.append(avg)
        best_scores.append(best)
        ranges.append(score_range)
        deviations.append(std_dev)

        print(
            f"{athlete} ({len(scores)} recorded runs): "
            f"Best={best:.2f}, "
            f"Average={avg:.2f}, "
            f"Range={score_range:.2f}, "
            f"Std Dev={std_dev:.2f}"
        )

    # Graph 4: Best score vs average run score
    x = range(len(names))
    width = 0.35

    plt.figure(figsize=(11, 6))
    plt.bar(
        [i - width / 2 for i in x],
        best_scores,
        width,
        label="Best run"
    )
    plt.bar(
        [i + width / 2 for i in x],
        averages,
        width,
        label="Average run"
    )

    plt.xticks(list(x), names, rotation=30, ha="right")
    plt.ylabel("Score")
    plt.title(f"{year} Women's Ski SuperPipe - Best vs Average")
    plt.legend()
    plt.tight_layout()
    plt.savefig(GRAPH_DIR / f"{year}_best_vs_average.png")
    plt.close()

    # Graph 5: Score range
    plt.figure(figsize=(11, 6))
    plt.bar(names, ranges)
    plt.ylabel("Score Range (Lower = More Consistent)")
    plt.title(f"{year} Women's Ski SuperPipe - Run Consistency")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(GRAPH_DIR / f"{year}_run_consistency.png")
    plt.close()

    # Graph 6: Standard deviation
    plt.figure(figsize=(11, 6))
    plt.bar(names, deviations)
    plt.ylabel("Standard Deviation (Lower = More Consistent)")
    plt.title(f"{year} Women's Ski SuperPipe - Score Variation")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(GRAPH_DIR / f"{year}_score_variation.png")
    plt.close()

    print(f"\nSaved three run-level graphs for {year}.")
