#Goal is to help small town modernize its vote counting process
#Create script that analyzes the votes
#calculates total votes
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


#Create list for unique candidate names
Names=[]

#Print the Candidate names
for rep in Candidate:
    if rep not in Names:
        Names.append(rep)    

#Count the votes for each name
Name1=Names[0]
Name2=Names[1]
Name3=Names[2]
Name1_Count=0
Name2_Count=0
Name3_Count=0

for name in Candidate:
    if name==Name1:
        Name1_Count+=1
    if name==Name2:
        Name2_Count+=1
    if name==Name3:
        Name3_Count+=1

#find percentage of total votes for each

n1_percent=round(Name1_Count/rowcount * 100,3)
n2_percent=round(Name2_Count/rowcount * 100,3)
n3_percent=round(Name3_Count/rowcount * 100,3)


#print candidate summary

print(Names[0] + ": " + str(n1_percent) + " %" + " ("+ str(Name1_Count) + ")")
print(Names[1] + ": " + str(n2_percent) + " %" + " ("+ str(Name2_Count) + ")")
print(Names[2] + ": " + str(n3_percent) + " %" + " ("+ str(Name3_Count) + ")")
print("------"*10) 

#Find the winner of the election

if Name1_Count>Name2_Count:
    if Name1_Count>Name3_Count:
        print("Winner: " + Names[0])   
elif Name2_Count>Name3_Count:
    print("Winner: " + Names[1]) 
elif Name3_Count>Name2_Count:
    print("Winner: " + Names[2])    
print("------"*10)     