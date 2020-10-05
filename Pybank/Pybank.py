#Modules
import os
import csv

#Variables
net_change =[]

date = 0
row_count = 0
total_months = 0
current_profit = 0
previous_profit = 0

   
#Set path for file
budget_data = os.path.join('Resources', 'budget_data.csv')
                              
#Open and read csv file
with open(budget_data, "r") as csv_file:
    
    #Split date at comma
    reader = csv.reader(csv_file, delimiter=",")
    
    #Skip header row
    csv_header = next(reader)

    for row in reader:
      
       #The total number of months included in the dataset
       total_months = date + 1
   
       #The net total amount of "Profit/Losses" over the entire period
       total_profit_loss += int(row[1])  
            
       #The average of the changes in "Profit/Losses" over the entire period by creating a function
       def averageOfList(num):
           total_profit_loss = 0
           for t in num:
               total_profit_loss = total_profit_loss + t

           avg = total_profit_loss / len(num)
           return avg    

       
       
       #The greatest increase in profits (date and amount) over the entire period
       #three varibles  1. the current profit, 2. the previous, 3. previous profit -current profit 
       #
       #The greatest decrease in losses (date and amount) over the entire period

#Specify the path to write in
new_data = os.path.join("..", "output", "new.csv")

#Open and write to csv file
with open("new_data.csv", "w") as new_file:
    
    #Initialize csv.writer 
    csvwriter = csv.writer(new_file)         


    #Print out results
    print(f"Financial Analysis")
    print(f"--------------------------------------------")
    print(f"Total Months:", str{total_months})
    print(f"Total Revenue: $", str{total_profit_loss})
    print(f"Average Revenue: $", str{average_changes})
    print(f"Greatest Increase in Profits: {},{}")
    print(f"Greatest Decrease in Profits: {},{}")