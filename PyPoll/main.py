#Goal is to help small town modernize its vote counting process
#Create script that analyzes
#the votes and calculates total votes
#candiate names
#percentage of votes each candidate won
#total votes each candidate won
#winner of the election

#Import os module
import os

#import csv file
import csv
csvpath = os.path.join("Resources", "election_data.csv")


#Assign lists to store the data for each column
VoterID=[]
County=[]
Candidate=[]

#Reading using csv
with open(csvpath) as csvfile:
    election_data= csv.reader(csvfile, delimiter=",")
    

#Read header row
    csv_header= next(election_data)

#Set calculated variables to 0
    rowcount=0

#iterate through rows to append csv data to a list
    for row in election_data:
        #Add number of votes
        VoterID.append(row[0])
        #Add county each vote was from
        County.append(row[1])
        #Add candidate each vote was for
        Candidate.append(row[2]) 
        rowcount+=1

#Print Election Results header

print("Election Results")
print("------"*10)  
print("Total Votes"+str(rowcount))
print("------"*10) 