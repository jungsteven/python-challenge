#import necessary modules

import os
import csv
from collections import defaultdict

#Open and read CSV file

election_csv = os.path.join("..", "Resources", "election_data.csv")

columns = defaultdict(list) # each value in each column is appended to a list

with open(election_csv, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    
    for row in csvreader:
        for(k, v) in row.items(): 
            columns[k].append(v) 
			
#--------------------------------------------------------------------------------------			
			
#Assigning variables for each column

Voter_column = columns['Voter ID'] #assigned to this variable to make it easier to read
candidate_column = columns['Candidate']
county_column = columns['County']


#Assigning variables from each candidate count

Khan_votes = candidate_column.count("Khan")
Correy_votes = candidate_column.count("Correy")
Li_votes = candidate_column.count("Li")
Tooley_votes = candidate_column.count("O'Tooley")

#--------------------------------------------------------------------------------------

#To calculate voter percentages for each candidate

Khan_perc = (int(candidate_column.count("Khan")) / int(len(Voter_column))) * 100
Correy_perc = (int(candidate_column.count("Correy")) / int(len(Voter_column))) * 100
Li_perc = (int(candidate_column.count("Li")) / int(len(Voter_column))) * 100
Tooley_perc = (int(candidate_column.count("O'Tooley")) / int(len(Voter_column))) * 100

Khan_perc = round(Khan_perc, 2)
Correy_perc = round(Correy_perc, 2)
Li_perc = round(Li_perc, 2)
Tooley_perc = round(Tooley_perc, 2)


#-------------------------------------------------------------------------------------------------------------------------
#Output

print("ELECTION RESULTS\n")
print("---------------------------")

print("Total Votes: " + str(len(Voter_column)))

print("---------------------------")

print("Khan: " + str(Khan_votes) + " " + "[" + str(Khan_perc) + "%]")
print("Correy: " + str(Correy_votes) + " " + "[" + str(Correy_perc) + "%]")
print("Li: " + str(Li_votes) + " " + "[" + str(Li_perc) + "%]")
print("O'Tooley: " + str(Tooley_votes) + " " + "[" + str(Tooley_perc) + "%]")

print("---------------------------")

#-------------------------------------------------------------------------------------------------------------------------

#Conditionals to output winner of elections

if int(Khan_votes) > int(Correy_votes) and int(Khan_votes) > int(Li_votes) and int(Khan_votes) > int(Tooley_votes):
    print("Winner: Khan")
    
elif int(Correy_votes) > int(Khan_votes) and int(Correy_votes) > int(Li_votes) and int(Correy_votes) > int(Tooley_votes):
    print("Winner: Correy")
    
elif int(Li_votes) > int(Khan_votes) and int(Li_votes) > int(Correy_votes) and int(Li_votes) > int(Tooley_votes):
    print("Winner: Li")
    
elif int(Tooley_votes) > int(Khan_votes) and int(Tooley_votes) > int(Correy_votes) and int(Tooley_votes) > int(Li_votes):
    print("Winner: O'Tooley")
       
print("---------------------------")


#-------------------------------------------------------------------------------------------------------------------------
