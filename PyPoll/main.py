# modules
import os
import csv

# set path to file
csvpath = os.path.join('./PyPoll/Resources/election_data.csv')
print("Current Working Directory:", os.getcwd(), "\n")

# absolute path verification
absolute_csvpath = os.path.abspath(csvpath)
print("Absolute Path:", absolute_csvpath)

# Set the first value 
total_votes = 0
votes_per_candidate = {}
candidate_list = []
votes_list = []
percent_of_votes = []
winner = ""
winner_votes = 0
summary_of_results = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv.header = next(csvreader)

    for row in csvreader:

        # Find the total number of votes
        total_votes = total_votes + 1
        
        # Make sure 2nd row header is set
        candidate = row[2]
        
        # Add 1 each time a candidate's name is on the list...
        if candidate in candidate_list:
            votes_per_candidate[candidate] = votes_per_candidate[candidate] + 1

        else:
            candidate_list.append(candidate)
            votes_per_candidate[candidate] = 1

        # Start looping through each candidates info for summary
    for key, value in votes_per_candidate.items():
        votes_list.append(value)
        votes = votes_per_candidate[candidate]
        percent_voted = round((int(value) / total_votes * 100), 3)
        percent_of_votes.append(percent_voted)

        # Find winner by comparing count of each candidate
        if (value > winner_votes):
            winner_votes = value
            winner = key
    
    # Combine each list into 1 list
    summary_of_results = zip(candidate_list, percent_of_votes, votes_list)
    summary_of_results = list(summary_of_results)

     # Print to make sure everything is right
    output = "Election Results\n"
    output +="---------------------------------------------\n"
    output +=f'Total Votes :  {total_votes}\n'
    output +="---------------------------------------------\n"
    for item in summary_of_results:
            output +=f"{item[0]}: {item[1]}% ({item[2]})\n"
    output +="---------------------------------------------\n"
    output +=f'Winner : {winner}\n'
    output +="---------------------------------------------\n"

    print(output)

with open('./PyPoll/Analysis/pypoll_analysis.txt', 'w') as text_file: 
     text_file.write(output)