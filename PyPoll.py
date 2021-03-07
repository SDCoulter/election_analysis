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

# Initialize starting variables.
total_votes = 0
candidate_options = []
candidate_votes = {}

# Initialize winning candidate variables.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open these election results and read the file.
with open(DATA_FILE) as f_obj:
    # Read the file object with the reader function.
    file_reader = csv.reader(f_obj)
    # Save the headers and move on - don't need to analyze.
    headers = next(file_reader)

    for row in file_reader:
        # Increment vote count for every row of data.
        total_votes += 1
        # Find the candidate name in each row.
        candidate_name = row[2]

        # Check if the name is unique, if so, add it to our list of names.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Begin tracking votes for the unique candidate with a dict.
            candidate_votes[candidate_name] = 0

        # Increment candidate's votes each time their name appears.
        candidate_votes[candidate_name] += 1

with open(ANALYSIS_FILE, "w") as f_obj:
    # Add some formatting for our text output file.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save to the file.
    f_obj.write(election_results)

    # Get the votes each and percentage of the total vote.
    for name in candidate_options:
        ind_votes = candidate_votes[name]
        # Find the percentage - (is there need for float()?).
        vote_percent = float(ind_votes) / float(total_votes) * 100
        # Save the candidate's results string and use F-string formatting.
        candidate_results = f"{name}: {vote_percent:.1f}% ({ind_votes:,})\n"
        # Then print to terminal and write to our output file.
        print(candidate_results)
        f_obj.write(candidate_results)

        # Find the winner of the election.
        if (ind_votes > winning_count) and (vote_percent > winning_percentage):
            # If a candidate has a higher vote count assign that data to
            # the winning variables.
            winning_candidate = name
            winning_count = ind_votes
            winning_percentage = vote_percent

    # Winning candidate summary.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    # Save this summary to the output text file.
    print(winning_candidate_summary)
    f_obj.write(winning_candidate_summary)
