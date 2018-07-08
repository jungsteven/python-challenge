#Modules
import os
import csv
from collections import defaultdict

#Open and read CSV file

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

columns = defaultdict(list) # each value in each column is appended to a list

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    
    for row in csvreader:
        for(k, v) in row.items(): #go over each column name and value
            columns[k].append(v) #append the value into the appropriate list, based on column name k

#Below was used to test if each column would appear as a list            
#print(columns['Date'])
#print(columns['Profit/Losses'])


print("Financial Analysis\n")
print("---------------------------------------------------------------\n")

Date_column = columns['Date'] #assigned to this variable to make it easier to read

print("Total Months: " + str(len(Date_column))) #To get total months, I took the lenght of the list

#assigned the total spend in profits/losses to the variable total_profit to make it easier type out
total_profit = columns['Profit/Losses']

#used list comprehension to convert the strings in 'Profit/Losses' to integers
total_profit = [int(i) for i in total_profit]

#now set total_profit to be the sum the column as integers
total_profit = sum(total_profit)

#Let's print the total spend
print("Total Profit: " + "$" + str(total_profit))


#-------------------------------------------------------------------------------------------------------------


#Now to find the greatest increase in profits over the entire period

#for the column profits/losses find the value with the largest difference, then print
#Re-assign variable to total_profit
total_profit = columns['Profit/Losses']
total_profit = [int(i) for i in total_profit]


#-------------------------------------------------------------------------------------------------------------

#Find the Average Change

average_change = []

for i in range(1, len(total_profit)): 
    average_change.append(total_profit[i] - total_profit[i-1]) 
    avg_rev_change = sum(average_change)/len(average_change)
    
print("Average Change: " + "$" + str(round(avg_rev_change ,2)))
    
    
#Find the Greatest increase and decrease in profits

max_rev_change = max(average_change)
min_rev_change = min(average_change)

max_rev_change_date = str(Date_column[average_change.index(max(average_change))])
min_rev_change_date = str(Date_column[average_change.index(min(average_change))])

print("Greatest Increase in Profits:", max_rev_change_date,"($", max_rev_change,")")
print("Greatest Decrease in Profits:", min_rev_change_date,"($", min_rev_change,")")