#Modules
import csv
import os

#Set path for file
election_data = os.path.join("Resources", "election_data.csv")
results_data = os.path.join("Analysis", "election_analysis.txt")

#Variables at start
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

#Open and read csv file
with open(election_data) as csv_file:
    
    #Split date at comma
    reader = csv.reader(csv_file)
    
    #Head the header row first
    header = next(reader)

    #Loop through the cvs file
    for row in reader:
        #The total number of votes included in the dataset, count up 1 for each loop
        total_votes = total_votes + 1
        

        #Use third column[2] for candidate.
        candidate = row[2]

        if candidate not in candidate_options:
            # Initialize candidate
            candidate_options.append(candidate) #ADDED LIST HERE and ABOVE
            candidate_votes[candidate] = 0
            
        else: 
            candidate_votes[candidate] = candidate_votes[candidate] + 1

with open(results_data, "w") as txt_file:
   
    # Print the final vote count (to terminal)
   election_results = (
       f"\n\nElection Results\n"
       f"-------------------------\n"
       f"Total Votes: {total_votes}\n"
       f"-------------------------\n")
   print(election_results, end="")

   #Save the final vote count to the text file
   txt_file.write(election_results)
   
   #Determine the winner by looping through the counts
   for candidate in candidate_votes:
       
       #Retrieve vote count and percentage
       votes = candidate_votes.get(candidate)
       vote_percentage = float(votes) / float(total_votes) * 100
       
       #Determine winning vote count and candidate
       if (votes > winning_count):
           winning_count = votes
           winning_candidate = candidate
       
       #Print each candidate's voter count and percentage (to terminal)
       voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
       print(voter_output, end="")
       
       #Save each candidate's voter count and percentage to text file
       txt_file.write(voter_output)
   
   #Print the winning candidate (to terminal)
   winning_candidate_summary = (
       f"-------------------------\n"
       f"Winner: {winning_candidate}\n"
       f"-------------------------\n")
   print(winning_candidate_summary)
   
   #Save the winning candidate's name to the text file
   txt_file.write(winning_candidate_summary)  