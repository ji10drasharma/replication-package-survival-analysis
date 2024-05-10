This repository provides the replication package for the paper titled *Investigating the survival of open-source libraries*

# Contents

The repository contains all the data required to generate the plots shown in the paper and, thus, come to the conclusions presented in the paper.

## `Setup and Run`

A virtual environment is recommended but not necessary. Follow this simple guide to setting up a virtual environment on Linux or Windows: https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/ For Mac: https://www.geeksforgeeks.org/how-to-install-virtual-environment-in-python-on-macos/

The `requirements.txt` file should list all Python libraries that this project depend on, and they will be installed using:

```
pip install -r requirements.txt
```

1. Navigate to the project directory replication-package-survival-analysis
2. Install the dependencies using above command
3. Run the project with `python src/main.py`

## `src` folder

The `main.py` is the only main file that needs for the results in `output` folder created after completing execution. 

The `merge_data.py` is the initial step in getting the results, it combines the two data files pairs into one.

The `clean_data.py` is the second step, it removes unncessary fields not required for the analysis.

The `regression_analysis.py` performs logistic regression classification on the clean_data.csv with target label status field.

Other files `stats_analysis.py` and `summary_stats.py` are supporting files for the analysis.

## `data` folder

This folder includes the data in CSV files from previous related research by Ait. et. al. https://github.com/SOM-Research/survivalAnalysisGitHub/tree/main/data.

There are 2 types of CSV files, each divided by ecosystem (see suffixes `-laravel`, `-npm`, `-r` and `-wp` for each file). 

These are the files included in `source` folder:

* `metadata-ECOSYSTEM.csv`, which, for each repository, has the information of whether it is a repository owned by a user or organization account (`repoType`), the status at the end of the previous study (used to answer RQ1 and RQ2) (`status`)
* `oracle-ECOSYSTEM.csv`, which complements `metadata.csv`providing the number of users in the community (`authors`), and the number of project resources created along its lifespan (`Commits`, `Pulls`, `Issues`, `Comments` and `Reviews`).
