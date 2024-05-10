from merge_data import fn_merge_data
from clean_data import fn_clean_data
from summary_stats import extract_summary
from stats_analysis import status_analysis, ecosystem_analysis
from regression_analysis import regression


# Combine two different csv files into one
fn_merge_data()

# Retain only useful fields for futher analysis
fn_clean_data()

# For box plots, get statistics on number fields
extract_summary()

# Get box plots for RQ1
status_analysis()

# Get grouped bar charts for RQ1
ecosystem_analysis()

# Get confusion matrix for RQ1
regression()

if __name__ == "main":
    pass
