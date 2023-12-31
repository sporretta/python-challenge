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
   # print("Financial Analysis")
    #print("---------"*10)    

 #Set lists to hold data from csv
    Date=[]
    Profit=[]  

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
   
    
   # print("Total Months: " + str(rowcount))
    #print("Total: $" + str(TotalDollars))
    
#Use the values from the new profit list to find the change from month to month
    Change=[Profit[i+1]- Profit[i] for i in range (len(Profit)-1)]
    
 #Find change in date
    Date_Change=[Date [i+1] for i in range (len(Date)-1)]

 #Combine the lists
   # change_data=list(zip(Date_Change,Change))
    
   
#find the average change
    length=0
    for j in Change:
        length= length +1
    Average=round(sum(Change)/len(Change),2)

    #print("Average Change: $" + str(Average))

#Find the greatest increase in the list
#78th row
   # MaxInc_Date=Date_Change[78]
    MaxIncrease=max(Change)

    MaxIndex=Change.index(MaxIncrease)
    MaxInc_Date=Date_Change[MaxIndex]
   
    #print(f"The Greatest Increase in Profits: {MaxInc_Date} (${ MaxIncrease})")

#Find the greatest decrease
#48th row
    #MaxDec_Date=Date_Change[48]
    MaxDecrease=min(Change)
  
    MinIndex=Change.index(MaxDecrease)
    MaxDec_Date=Date_Change[MinIndex]


    #print(f"The Greatest decrease in Profits: {MaxDec_Date} (${MaxDecrease})")

Output_Text=(
f'Financial Analysis\n'
f'----------------------------\n'
f'Total Months: {rowcount}\n'
f'Total: ${TotalDollars}\n'
f'Average Change: ${Average}\n'
f'Greatest Increase in Profits: {MaxInc_Date} (${ MaxIncrease})\n'
f'Greatest Decrease in Profits: {MaxDec_Date} (${MaxDecrease})'
)
print(Output_Text)


#write results to text file
output_path=os.path.join("Analysis/PyBank_Output.txt")

with open(output_path,"w") as csvfile:

    csvfile.write(Output_Text)