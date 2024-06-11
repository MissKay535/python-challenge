# modules
import os 
import csv

# set path for file
csvpath = os.path.join("/Users/kaylopilato/python-challenge/python-challenge/PyBank/Resources/budget_data.csv")
print("Current Working Directory:", os.getcwd(), "\n")

# construct path to csv file
csvpath = os.path.join("..", "Resourese", "budget_data.csv")

# print constructed path
print("Constructed Path:", csvpath, '\n')

# absolute path verification
absolute_csvpath = os.path.abspath(csvpath)
print("Absolute Path:", absolute_csvpath)