
import csv
from pathlib import Path
from collections import defaultdict

# Project directory
BASE = Path(__file__).resolve().parent
DATA_FILE = BASE / "data" / "superpipe_scores.csv"


def load_scores(filepath=None):
    """Load athlete scores from CSV into a dictionary."""
    if filepath is None:
        filepath = DATA_FILE

    scores = defaultdict(list)

    with open(filepath, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            athlete = row["athlete"]
            score = float(row["score"])
            scores[athlete].append(score)

    return dict(scores)


def average_score(scores):
    """Calculate the average score."""
    return sum(scores) / len(scores)


def best_score(scores):
    """Return the highest score."""
    return max(scores)


def consistency(scores):
    """Calculate the difference between highest and lowest scores."""
    return max(scores) - min(scores)


def most_consistent(athletes):
    """Find the most consistent athletes with at least 2 scores."""
    eligible = {
        name: scores
        for name, scores in athletes.items()
        if len(scores) >= 2
    }

    if not eligible:
        return []

    smallest_range = min(
        consistency(scores) for scores in eligible.values()
    )

    return [
        name for name, scores in eligible.items()
        if abs(consistency(scores) - smallest_range) < 1e-9
    ]


def highest_average(athletes):
    """Find athletes with the highest average score."""
    if not athletes:
        return []

    highest = max(
        average_score(scores) for scores in athletes.values()
    )

    return [
        name for name, scores in athletes.items()
        if abs(average_score(scores) - highest) < 1e-9
    ]


def highest_single_score(athletes):
    """Find athletes with the highest individual score."""
    if not athletes:
        return []

    highest = max(
        best_score(scores) for scores in athletes.values()
    )

    return [
        name for name, scores in athletes.items()
        if best_score(scores) == highest
    ]


def load_runs(filepath=None):
    """Load run scores grouped by year, round, and athlete."""
    if filepath is None:
        filepath = BASE / "data" / "superpipe_runs.csv"

    runs = {}

    with open(filepath, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            year = int(row["year"])
            round_name = row["round"]
            athlete = row["athlete"]
            score = float(row["score"])

            if year not in runs:
                runs[year] = {}

            if round_name not in runs[year]:
                runs[year][round_name] = {}

            if athlete not in runs[year][round_name]:
                runs[year][round_name][athlete] = []

            runs[year][round_name][athlete].append(score)

    return runs
