# modules
import os
import csv

# set path for file
csvpath = os.path.join('/Users/kaylopilato/python-challenge/python-challenge/PyBank/Resources/budget_data.csv')
print("Current Working Directory:", os.getcwd(), "\n")

# absolute path verification
absolute_csvpath = os.path.abspath(csvpath)
print("Absolute Path:", absolute_csvpath)

# set variables
total_months = 0
prev_rev = 0
rev_change = 0
rev = []
month_of_change = []
rev_change_list = []
great_in = ["", 0]
great_de = ["", 9999999999]
total_rev = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:

        #calculating totals, changes, increases, and decreases
        total_months += 1
        total_rev += int(row[1])
        rev_change = int(row[1]) - prev_rev
        prev_rev = int(row[1])
        month_of_change += [row[0]]

        if (rev_change > great_in[1]):
            great_in[0] = row[0]
            great_in[1] = rev_change

        if (rev_change < great_de[1]):
            great_de[0] = row[0]
            great_de[1] = rev_change

# find average revenue change
rev_change_list = rev_change_list + [rev_change]
sum = 0
for num in rev_change_list:
    sum += num
average = sum / len(rev_change_list)




# generate findings
output = (
    f"\nFinancial Analysis\n"
    f"-----------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_rev}\n"
    f"Average Change: ${average}\n"
    f"Greatest Increase in Profits: {great_in[0]} (${great_in[1]})\n"
    f"Greatest Decrease in Profits: {great_de[0]} (${great_de[1]})\n"
)

# print results
print(output)