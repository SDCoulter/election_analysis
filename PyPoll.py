# The data we need to retrieve:
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

import os, csv

# Assign file paths and names to variables.
# One for the initial data, and one for the analysis to be performed.
DATA_FILE = os.path.join("resources", "election_results.csv")
ANALYSIS_FILE = os.path.join("analysis", "election_analysis.txt")

# Open these election results and read the file.
with open(DATA_FILE) as f_obj:
    # Read the file object with the reader function.
    file_reader = csv.reader(f_obj)
    # Save the headers and move on - don't need to analyze.
    headers = next(file_reader)

    print(headers)
