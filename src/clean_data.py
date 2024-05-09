import pandas as pd
import os
from pathlib import Path

def fn_clean_data():

    # Load the merged data from a specified CSV file into a DataFrame
    merged_data = pd.read_csv(Path("data/processed/merged_data.csv"))

    # Rename the 'months' column to 'lifeSpan' for clarity
    merged_data.rename(columns={"months": "lifeSpan"}, inplace=True)

    # Define a list of column names that needs to be retained for further analysis
    columns_to_retain = [
        "repo_name",
        "repoType",
        "authors",
        "commits",
        "pulls",
        "issues",
        "comments",
        "reviews",
        "language",
        "status",
        "lifeSpan",
    ]

    clean_data = merged_data[columns_to_retain]

    # Save the combined data to a CSV file
    clean_data.to_csv(Path("data/processed/clean_data.csv"), index=False)

    print(f"clean_data.py complete")


if __name__ == "main":
    pass
