import pandas as pd
from matplotlib import pyplot as plt
import os
from pathlib import Path


def status_analysis():
    """This function generates a box plot showing the distribution of
    mean commits for each status (Alive, Dead, Zombie) for different metrics"""

    # Ensure the output directory exists
    output_dir = Path("output")
    os.makedirs(output_dir, exist_ok=True)

    # Load the data
    df = pd.read_csv(Path("data/processed/summary_stats.csv"), header=[0, 1], index_col=[0, 1])
    df.columns = ["_".join(col).strip() for col in df.columns.values]

    # Extract metrics and status from column names
    metrics = sorted(set(col.split("_")[0] for col in df.columns if "mean" in col))
    statuses = sorted(set(df.index.get_level_values(1)))

    # Loop through each metric and create a box plot
    for metric in metrics:
        data = {
            status: df.xs(status, level=1).filter(regex=f"^{metric}_mean$").iloc[:, 0]
            for status in statuses
        }

        # Plot box plot
        plt.figure(figsize=(4, 3))
        plt.boxplot(
            [data[status] for status in statuses], labels=statuses, patch_artist=True
        )
        plt.xlabel("Status")
        plt.ylabel(f"Mean {metric.capitalize()}")
        plt.title(f"Box Plot of Mean {metric.capitalize()} by Status")
        plt.grid(True)

        plt.tight_layout()

        # Save the plot as PDF and eps file
        plt.savefig(f"{output_dir}/{metric}_status_boxplot.eps", format="eps")
        plt.savefig(f"{output_dir}/{metric}_status_boxplot.pdf")

        # plt.show()
        plt.close()

    print(f"Status based analysis complete")


def ecosystem_analysis():
    """This function generates grouped bar charts distribution of projects
    across four ecosytems and repository type"""

    # Ensure the output directory exists
    output_dir = Path("output")
    os.makedirs(output_dir, exist_ok=True)

    # Load 'clean_data.csv' as it has repo_type field
    df = pd.read_csv(Path("data/processed/clean_data.csv"))

    # Group the data by 'language' and 'status', and 'repoType' and 'status'
    # count the number of projects in each group.
    language_status_grouped = (
        df.groupby(["language", "status"]).size().unstack(fill_value=0)
    )
    repo_type_status_grouped = (
        df.groupby(["repoType", "status"]).size().unstack(fill_value=0)
    )

    # create grouped bar charts
    def plot_grouped_bar(data, title, xlabel, filename):
        ax = data.plot(kind="bar", figsize=(10, 6), width=0.8)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel("Number of Projects")
        plt.xticks(rotation=0)  # Set rotation for x labels to 0 for better readability
        plt.grid(True, linestyle="--", alpha=0.6)

        plt.legend(title="Status", bbox_to_anchor=(1.05, 1), loc="upper left")

        plt.tight_layout()

        # Save the plot as PDF and eps file
        plt.savefig(f"{output_dir}/{filename}.eps", format="eps")
        plt.savefig(f"{output_dir}/{filename}.pdf")

        # plt.show()
        plt.close()

    # Create plots
    plot_grouped_bar(
        language_status_grouped,
        "Distribution of Projects by Status (Grouped by Language)",
        "Language",
        "language_distribution_by_status",
    )
    plot_grouped_bar(
        repo_type_status_grouped,
        "Distribution of Projects by Status (Grouped by Repo Type)",
        "Repo Type",
        "repo_type_distribution_by_status",
    )

    print(f"Ecosystem based analysis complete")
