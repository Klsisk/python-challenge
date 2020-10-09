#Modules
import csv
import os

#Set path for file
budget_data = os.path.join("Resources", "budget_data.csv")
new_data = os.path.join("Analysis", "budget_analysis.txt")

#Variables used
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0   

#Open and read csv file
with open(budget_data) as csv_file:
    
    #Split date at comma
    reader = csv.reader(csv_file)
    
    #Head the header row first
    header = next(reader)

    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])
        
    #Read through each row of data after the header
    for row in reader:
                
        #The total number of months included in the dataset, count up 1 for each loop
        total_months += 1
   
        #The net total amount of "Profit/Losses" over the entire period. Date in row [0] and Profit/Losses in row[1]
        total_net += int(row[1])  
        #Calculate change
        
        change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [change]
        month_of_change += [row[0]]

        #The greatest increase in profits (date and amount) over the entire period
        if change > greatest_increase[1]:
           greatest_increase[0] = row[0]
           greatest_increase[1] = change
        #Calculate the greatest decrease
        if change < greatest_decrease[1]:
           greatest_decrease[0] = row[0]
           greatest_decrease[1] = change

            
    #The average of the changes in "Profit/Losses" over the entire period 
    net_monthly_avg = sum(net_change_list) / len(net_change_list)

#Print out results
output = (
   f"Financial Analysis\n"
   f"----------------------------\n"
   f"Total Months: {total_months}\n"
   f"Total: ${total_net}\n"
   f"Average  Change: ${net_monthly_avg:.2f}\n"
   f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
   f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)

#Write to text path
with open(new_data, "w") as txt_file:
    txt_file.write(output)