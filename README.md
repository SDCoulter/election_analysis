# Challenge - Election Analysis

## Challenge - Overview

The purpose of this analysis was to provide a user-friendly, readable file to confirm the votes of a US Congressional election in Colorado. We were to confirm the total number of votes, the candidates and their respective votes and percentage of votes, declare the winner, and then finish up by comparing the counties. If this was a successful endeavour the program could be used on other similar elections, so we wanted it to be adaptable too.

## Challenge - Election-Audit Results

* There were a total of 369,711 votes cast in this election.
* The voter turnout of the counties in this election were:
    * Jefferson: 10.5% (38,855)
    * Denver: 82.8% (306,055)
    * Arapahoe: 6.7% (24,801)
* **Denver** county had the largest number of votes with **306,055**, making up **82.8%** of the total votes.
* The candidates and their results were:
    * Charles Casper Stockham: 23.0% (85,213)
    * Diana DeGette: 73.8% (272,892)
    * Raymon Anthony Doane: 3.1% (11,606)
* The winner of this Congressional election was:
    * **Diana DeGette** with **272,892** votes making up **73.8%** of the total votes.

## Challenge - Summary

This Python script was designed with the idea of being adaptable to other elections. It was deliberately decided not to use the specific names of the counties and candidates in the program, but to instead let the program find the unique ones and store those. With this setup you are able to have any number of candidates and counties in your `election_results.csv` file and the program will function the same.

To make it even more adaptable you could first change how the `candidate_name` and `county_name` variables are assigned. Currently we assign them with their location in the row:

```python
# Get the candidate name from each row.
candidate_name = row[2]

# 3: Extract the county name from each row.
county_name = row[1]
```

This works well for our intended needs for this election, but other CSV datasets might have a different order to the counties/candidates. To remedy this we would first read in the header of the file and then assign the names based on which column the counties and candidates were found in. This could look something like this:

```python
# Get the header row.
headers = next(file_reader)
# Find index positions and assign to variables.
counties_row_index = headers.index("County")
candidates_row_index = headers.index("Candidate")
# Assign the names more dynamically.
county_name = row[counties_row_index]
candidate_name = row[candidates_row_index]
```

As the program stands it is setup for a US Congressional election, and includes only counties. To make this program work for other races you may need to consider more than counties, this could include looking at `States`, `Districts`, `Cities`, and other population-defining groups. There are a number of ways to do this, first by having a top-level variable that you could change depending on the race. For our purposes it would be set to `"County"`, but could be any population area that defines an election:

```python
AREA_TYPE = "County"
# Or:
AREA_TYPE = "District"
# Or:
AREA_TYPE = "State"
    ...
```

You could even take this a step further and read in the type of area your program should work with from the command line (`> python PyPollChallenge.py "County"`):

```python
import sys
# Read the first argument from the command line.
AREA_TYPE = sys.argv[1]
```

If the goal is to make the program more versatile these would be the places to start. Beyond that you could begin looking into turning parts of the program into functions, (there's a lot of repetition that could be avoided), and then using this program more like a module that you can import and interact with that way.

### Context
This is the result of Module 3 of the University of Toronto School of Continuing Studies Data Analysis Bootcamp Course. Following the guidance of the module we end up pushing this selection of files to GitHub.
