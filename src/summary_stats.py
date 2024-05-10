import pandas as pd
import os
from pathlib import Path


def extract_summary():

    data = pd.read_csv(Path("data/processed/clean_data.csv"))

    # Calculate summary statistics
    summary_stats = data.groupby(["language", "status"])[
        [
            "lifeSpan",
            "authors",
            "commits",
            "pulls",
            "issues",
            "comments",
            "reviews",
        ]
    ].describe()

    # Save summary statistics to a CSV file
    summary_stats.to_csv(Path("data/processed/summary_stats.csv"))

    print(f"Summary_stats.py complete")


if __name__ == "main":
    pass
