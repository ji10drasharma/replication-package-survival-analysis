import pandas as pd
import os
from pathlib import Path


def merge_csv(file_path1, file_path2, language):
    # Load the first CSV file into a DataFrame
    df1 = pd.read_csv(Path(file_path1))
    df1["repo_name"] = df1["repo_name"].str.lower()

    # Load the second CSV file into a DataFrame
    df2 = pd.read_csv(Path(file_path2))
    df2["repo"] = df2["repo"].str.lower()

    # Add a 'language' column to df1
    df1["language"] = language

    # Merge the two dataframes based on the column 'common_column'
    merged_df = pd.merge(df1, df2, left_on="repo_name", right_on="repo")

    return merged_df


def fn_merge_data():

    # Ensure the output directory exists
    data_dir = Path("data/processed")
    os.makedirs(data_dir, exist_ok=True)

    # Initialize an empty DataFrame to hold all merged data
    all_data = pd.DataFrame()

    # Define the file paths for each pair of CSV files
    csv_pairs = [
        ("data/source/metadata-laravel.csv","data/source/oracle-laravel.csv","Laravel",),
        ("data/source/metadata-npm.csv", "data/source/oracle-npm.csv", "NPM"),
        ("data/source/metadata-r.csv", "data/source/oracle-r.csv", "R"),
        ("data/source/metadata-wp.csv", "data/source/oracle-wp.csv", "WordPress"),
    ]

    # Process each pair
    for file_path1, file_path2, language in csv_pairs:
        merged_df = merge_csv(file_path1, file_path2, language)
        all_data = pd.concat([all_data, merged_df], ignore_index=True)

    # Save the combined data to a CSV file
    all_data.to_csv(f"{data_dir}/merged_data.csv", index=False)

    print(f"File pairs combined and saved to {data_dir}")


if __name__ == "main":
    pass
