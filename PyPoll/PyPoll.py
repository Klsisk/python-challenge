#Modules
import os
import csv

voter_id = 0

#Set path for file
election_data = os.path.join('Resources', 'election_data.csv')

#Open and read csv file
with open(election_data, "r") as csv_file:
    
    #Split date at comma
    reader = csv.reader(csv_file, delimiter=",")
    
    #Skip header row
    csv_header = next(reader)

    #The total number of votes cast
    total_votes = voter_id + 1

    #A complete list of candidates who received votes

    #The total number of votes each candidate won

    #The winner of the election based on popular vote