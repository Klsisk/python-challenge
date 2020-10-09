#Modules
import csv
import os

#Set path for file
election_data = os.path.join('Resources', 'election_data.csv')
results_data = os.path.join("Analysis", "election_analysis.txt")

#Variables at start
total_votes = 0
candidate_options = []
winner_votes = 0

#Open and read csv file
with open(election_data) as csv_file:
    
    #Split date at comma
    reader = csv.reader(csv_file)
    
    #Head the header row first
    header = next(reader)

    #Create a dictionary from the cvs file
    election = {}

    #Loop through the cvs file
    for row in reader:
        #The total number of votes included in the dataset, count up 1 for each loop
        total_votes += 1
        #Use third column[2] for candidate.
        candidate = row[2]

        if candidate not in election:
            # Initialize candidate
            election[candidate] = 0
            candidate_options.append(candidate) #ADDED LIST HERE and ABOVE

            #Add 1 to candidate's vote count
            election[candidate] += 1

    percentage = {}

    #Create a list for percentage of votes each candidate won
    for candidate, vote_count in election.items():
        percentage[candidate] = round(100 * vote_count / total_votes, 2)  
    
    #Retrieve vote count and percentage
    votes = election[candidate]
    vote_percentage = float(votes) / float(total_votes) * 100
    candidate_results = (
        f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#Identify the winner
if votes > winner_votes:
    winner_votes = votes
    winner = candidate_name

 #Print out results
output = (
f"\nElection Results\n"
f"--------------------------------------------\n"
f"Total Votes: {total_votes}\n"
f"--------------------------------------------\n"
for person, vote_count in candidate_votes.items()
    f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"
f"--------------------------------------------\n"
f"Winner:  {winner}\n"
f"--------------------------------------------\n"
)   

print(output)

#Write to text path
with open(results_data, "w") as txt_file:
    txt_file.write(output)    