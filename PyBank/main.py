#Create a script that looks at Budget data to draw summaries on a company's budget
#The goal is to calculate the following:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period


#Import os module
import os

#import csv file
import csv
csvpath = os.path.join("Resources", "budget_data.csv")


#Reading using csv
with open(csvpath) as csvfile:
    budget_data= csv.reader(csvfile, delimiter=",")
    

#Read header row
    csv_header= next(budget_data)

#Print Analysis header
    print("Financial Analysis")
    print("---------"*10)    

 #Set lists to hold data from csv
    Date=[]
    Profit=[]  
    ProfitChange=[]
#Define row count and dollar value baseline values
    rowcount=0    
    TotalDollars=0
    Change=0

#Read every row of data after the header to find the total months and dollars
    for row in (budget_data):
        Date.append(row[0])
        Profit.append(int(row[1]))
        rowcount+=1
        TotalDollars+= int(row[1])
        #ProfitChange.append((int(row[1]+1)-(row[1])))

    print("Total Months: " + str(rowcount))
    print("Total:" + str(TotalDollars))
    
#Use the values from the new profit list to find the change from month to month
    Change=[Profit[i+1]-Profit[i] for i in range (len(Profit)-1)]
    
#add the changes to profit change list
    ProfitChange.append(Change)
  
 
#find the average change
    length=0
    #for j in ProfitChange:
        #length= length +1
    #print(length)
    #Average=sum(ProfitChange)/len(ProfitChange)
    #print("The total Annual Profit Change is" + Average)

#Find the greatest increase in the list
    MaxIncrease=[ProfitChange[i+1]+ProfitChange[i] for i in range (len(ProfitChange)-1)]

    print(f"The Greatest Increase is :{ MaxIncrease}")

#Find the greatest decrease
    MinChange=ProfitChange[0]
    for i in ProfitChange:
        if i < MinChange:
            i=MinChange
    print(f"The Greatest decrease in : ({MinChange})")