#main file for PyPoll
import os
import csv

filename = "election_data.csv"

numVotes = 0
candidates = []
index=""

match = False

#open csv and compile all candidate votes into a list "candidates"
#also tally how many votes were submitted with an iterator numVotes
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    for row in csvreader:
        numVotes+=1
        candidates.append(row[2])

#add the first candidate to the unique candidates list
uniqueCand = []
uniqueCand.append(candidates[0])

#sort only unique candidates into the "uniqueCand" list
for candidate in candidates:
    for each in uniqueCand:
        if each == candidate:
            match=True
            break
    if match==True:
        match=False
        continue
    else:
        uniqueCand.append(candidate)

#calculate how many votes each one got
voterList=[]
for each in uniqueCand:
    voterList.append(0)

for idx,each in enumerate(uniqueCand):
    for candidate in candidates:
        if candidate==each:
            voterList[idx]+=1

#Calculate each candidate's percent won + number of votes won
percentList = []

for votes in voterList:
    percent = round(((votes/numVotes)*100),2)
    percentList.append(percent)

#Find out who's the winner
highest = 0
for idx,votes in enumerate(voterList):
    if int(votes) > highest:
        highest = int(votes)
        index = idx
winner = uniqueCand[index]

#winner: winner
#Percent won list: percentList
#Total votes: numVotes
#List of each candidate's votes: voterList
#candidates: uniqueCand

print(f"Election Results\n-----------------\nTotal Votes:{numVotes}")
print(f"-----------------")
for idx,candidate in enumerate(uniqueCand):
    print(f"{candidate}: {percentList[idx]}% ({voterList[idx]})")
print(f"-----------------\nWinner: {winner}")
print("-----------------")

file = open("PyPollResults.txt", 'w')

file.write(f"Election Results\n-----------------\n")
file.write(f"Total Votes: {numVotes}\n-----------------\n")
for idx,candidate in enumerate(uniqueCand):
    file.write(f"{candidate}: {percentList[idx]}% ({voterList[idx]})\n")
file.write(f"-----------------\nWinner: {winner}\n")
file.write("-----------------")
