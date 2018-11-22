#main file for PyBank
import os
import csv


filename = "budget_data.csv"
monthlist = []
proflosslist = []
totMoney = 0
changeList = []

#open file and create list of months and list of profits/losses
#add up money in the profits/losses column in totMoney
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    for row in csvreader:
        monthlist.append(row[0])
        proflosslist.append(int(row[1]))
        totMoney += int(row[1])
        
numMonths = len(monthlist)

#create list of the change in profit between months
for x in range(1,(len(monthlist))):
    change = proflosslist[x] - proflosslist[x-1]
    changeList.append(change)

highest = 0
lowest = 0
highestmonth = ""
lowestmonth = ""

#figure out highest profits and lowest losses
for idx, changes in enumerate(changeList):
    if changes > highest:
        highest = changes
        highestmonth = monthlist[idx+1]
    if changes < lowest:
        lowest = changes
        lowestmonth = monthlist[idx+1]

avgChange = round((sum(changeList)/len(changeList)),2)

print("Financial Analysis \n--------------------------")
print(f"Total Months: {numMonths}")
print(f"Total: {totMoney}")
print(f"Average Change: ${avgChange}")
print(f"Greatest Increase in Profits: {highestmonth} (${highest})")
print(f"Greatest Decrease in Profits: {lowestmonth} (${lowest})")

file = open("PyBankResults.txt", 'w')

file.write("Financial Analysis \n--------------------------\n")
file.write(f"Total Months: {numMonths}\n")
file.write(f"Total: {totMoney}\n")
file.write(f"Average Change: ${avgChange}\n")
file.write(f"Greatest Increase in Profits: {highestmonth} (${highest})\n")
file.write(f"Greatest Decrease in Profits: {lowestmonth} (${lowest})\n")
