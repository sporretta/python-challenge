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
    
#Read every row of data after the header to find the total months and dollars
    for row in (budget_data):
        Date.append(row[0])
        Profit.append(row[1])
        rowcount+=1
        TotalDollars+= int(row[1])
        PChange=int(Profit[1])-int(Profit[0])
        ProfitChange.append(str(PChange))
    print("Total Months: " + str(rowcount))
    print("Total:" + str(TotalDollars))
    
#Create function to find the average change
def average(ProfitChange) :
    length=len(ProfitChange)
    total=0
    for change in ProfitChange:
        total+=change
    return total/length



