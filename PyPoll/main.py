# modules
import os
import csv

# set path to file
csvpath = os.path.join('/Users/kaylopilato/python-challenge/python-challenge/PyPoll/Resources/election_data.csv')
print("Current Working Directory:", os.getcwd(), "\n")

# absolute path verification
absolute_csvpath = os.path.abspath(csvpath)
print("Absolute Path:", absolute_csvpath)