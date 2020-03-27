# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
txtpath = os.path.join('Output', 'financial_analysis.txt')

class my_writer:
    def __init__(self, file_name):
        self.of = open(file_name, "w")

    def write(self, str):
        print(str)
        self.of.write(str)
        self.of.write(os.linesep)

o = my_writer(txtpath)
o.write("Financial Analysis")
o.write("----------------------------")

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    next(csvreader)

    months = 0
    net_total = 0
    delta_total = 0
    first = True
    prev_profit = 0
    max_month = ''
    max_delta = 0
    min_month = ''
    min_delta = 0

    # Read each row of data after the header
    for row in csvreader:
        # The total number of months included in the dataset
        months += 1
        month = row[0]
        profit = int(row[1])

        # The net total amount of "Profit/Losses" over the entire period
        net_total += profit

        # The average of the changes in "Profit/Losses" over the entire period
        if first:
            first = False
        else:
            delta = profit - prev_profit
            delta_total += delta
            # The greatest increase in profits (date and amount) over the entire period
            if max_delta < delta:
                max_month = month
                max_delta = delta

            # The greatest decrease in losses (date and amount) over the entire period
            if min_delta > delta:
                min_month = month
                min_delta = delta

        prev_profit = profit

    if months > 1:
        o.write(f"Number of unique months: {months}")
        o.write(f"Net total: ${net_total:,}")
        o.write(f"Average change: ${delta_total/(months-1):,.2f}")
        o.write(f"Greatest Increase: {max_month} ${max_delta:,}")
        o.write(f"Greatest Decrease: {min_month} ${min_delta:,}")
    else:
        o.write("Dis no big data. Need moar data.")

