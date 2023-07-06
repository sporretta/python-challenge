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


#Assign lists to store the data for eeach candidate
Candidate=[]
Candidate_Dictionary={}
rowcount=0

#Reading using csv
with open(csvpath) as csvfile:
    election_data= csv.reader(csvfile, delimiter=",")
    

#Read header row
    csv_header= next(election_data)



#iterate through rows to append csv data to a list
    for row in election_data:
        #Add candidate each vote was for
        rowcount+=1
        if row[2] not in Candidate:
            Candidate.append(row[2]) 
            Candidate_Dictionary[row[2]]=0
        Candidate_Dictionary[row[2]]+=1
    #print(Candidate_Dictionary)

    Candidate_Percent = {key: round(val / rowcount*100,3) for key, val in Candidate_Dictionary.items()}
    #print(Candidate_Percent)
    Winner = max(Candidate_Dictionary, key=Candidate_Dictionary.get)
    #print(Winner)


    TotalVotes= "Total Votes: "+str(rowcount)  

#Store candidate details in own variables
 #Combined dictionary 

combined=[]
for k1,v1 in Candidate_Dictionary.items(): # the basic way
    combined = {}   
   
    for k2,v2 in Candidate_Percent.items():
        combined = k1+": "+str(v2)+"% "+"("+str(v1)+")"
        v2+=1
       

Output_Text=(f'Election Results\n'
f'-------------------------\n'
f'Total Votes: {rowcount}\n'
f'-------------------------\n'
f'{combined}\n'
f'-------------------------\n'
f'Winner: {Winner}\n'
f'-------------------------') 

print(Output_Text)

#Write output to text file
#output_path=os.path.join("Analysis/PyPollOutput.txt")

#with open(output_path,"w") as csvfile:

    #csvfile.write(Output_Text)