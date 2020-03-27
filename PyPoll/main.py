# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
txtpath = os.path.join('Output', 'election_results.txt')

class my_writer:
    def __init__(self, file_name):
        self.of = open(file_name, "w")

    def write(self, str):
        print(str)
        self.of.write(str)
        self.of.write(os.linesep)

o = my_writer(txtpath)
o.write("Election Results")
o.write("----------------------------")

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    next(csvreader)

    total_votes = 0
    poll = {}

# Objectives
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

    # Read each row of data after the header
    for row in csvreader:
        # The total number of months included in the dataset
        total_votes += 1
        voter_id = row[0]
        county = row[1] # <-- although county is not used in the analysis
        candidate = row[2]

        if candidate in poll:
            poll[candidate] += 1
        else:
            poll[candidate] = 1


    if total_votes > 0:
        o.write(f"Total Votes: {total_votes:,}")
        o.write("----------------------------")
        winner = ""
        max_votes = 0
        for candidate in poll:
            votes = poll[candidate]
            o.write(f"{candidate}: {votes/total_votes:.3%} ({votes:,})")
            if max_votes < votes:
                max_votes = votes
                winner = candidate
        o.write("----------------------------")
        o.write(f"Winner: {winner}")
    else:
        o.write("Dis no big data. Need moar data.")

