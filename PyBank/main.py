#main file for PyBank
import os
import csv


filename = "budget_data.csv"
monthlist = []
proflosslist = []
totMoney = 0
changeList = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    for row in csvreader:
        monthlist.append(row[0])
        proflosslist.append(int(row[1]))
        totMoney += int(row[1])
        
numMonths = len(monthlist)

for x in range(1,(len(monthlist)-1)):
    change = proflosslist[x] - proflosslist[x-1]
    changeList.append(change)

highest = 0
lowest = 0
totchanges = 0
highestmonth = ""
lowestmonth = ""
for idx, changes in enumerate(changeList):
    if changes > highest:
        highest = changes
        highestmonth = monthlist[idx+1]
    if changes < lowest:
        lowest = changes
        lowestmonth = monthlist[idx+1]
    totchanges += changes

avgChange = round((totchanges/len(changeList)),2)

print("Financial Analysis \n--------------------------")
print(f"Total Months: {numMonths}")
print(f"Total: {totMoney}")
print(f"Average Change: ${avgChange}")
print(f"Greatest Increase in Profits: {highestmonth} (${highest})")
print(f"Greatest Decrease in Profits: {lowestmonth} (${lowest})")
