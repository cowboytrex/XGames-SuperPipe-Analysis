
from pathlib import Path
import matplotlib.pyplot as plt

from superpipe import (
    load_scores,
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

athletes = load_scores()

# Answer three research questions
print("WOMEN'S SKI SUPERPIPE ANALYSIS")
print("-" * 40)

print("1. Most consistent:", most_consistent(athletes))
print("2. Highest average:", highest_average(athletes))
print("3. Highest single score:", highest_single_score(athletes))

# Graph 1: Average scores
names = list(athletes.keys())
averages = [average_score(s) for s in athletes.values()]

plt.figure(figsize=(10, 5))
plt.bar(names, averages)
plt.title("X Games Aspen - Average Scores")
plt.ylabel("Average Score")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(GRAPH_DIR / "average_scores.png")
plt.close()

# Graph 2: Highest scores
highest = [best_score(s) for s in athletes.values()]

plt.figure(figsize=(10, 5))
plt.bar(names, highest)
plt.title("X Games Aspen - Highest Scores")
plt.ylabel("Best Score")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(GRAPH_DIR / "highest_scores.png")
plt.close()

# Graph 3: Consistency (only 2+ scores)
eligible = {
    name: scores
    for name, scores in athletes.items()
    if len(scores) >= 2
}

if eligible:
    ranges = [consistency(s) for s in eligible.values()]

    plt.figure(figsize=(10, 5))
    plt.bar(list(eligible.keys()), ranges)
    plt.title("X Games Aspen - Score Consistency")
    plt.ylabel("Score Range (Lower = More Consistent)")
    plt.tight_layout()
    plt.savefig(GRAPH_DIR / "consistency.png")
    plt.close()

print("\nGraphs saved in:", GRAPH_DIR)
