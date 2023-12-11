
import os
import csv


file_path = os.path.join("Resources", "election_data.csv") 

print("ELECTION RESULTS")

print("--------------------------------")

candidate_1 = "Charles Casper Stockham"
candidate_2 = "Diana DeGette"
candidate_3 = "Raymon Anthony Doane"
the_winner =  "" 
winner = False

with open(file_path) as poll_csv:
    csv_reader = csv.reader(poll_csv, delimiter=",")
    header = next(csv_reader)

    data_list = []
    votes = 0
    candidate_votes_1 = 0
    candidate_votes_2 = 0
    candidate_votes_3 = 0
    for row in csv_reader:
        data_list.append(row[0])
        votes = votes + 1

        if row[2] == candidate_1:
            candidate_votes_1 = candidate_votes_1 + 1
        elif row[2] == candidate_2:
            candidate_votes_2 = candidate_votes_2 + 1
        elif row[2] == candidate_3: 
            candidate_votes_3 = candidate_votes_3 + 1
    perc_1 = round(candidate_votes_1 / votes * 100, 2)
    perc_2 = round(candidate_votes_2 / votes * 100, 2)
    perc_3 = round(candidate_votes_3 / votes * 100, 2)
    if candidate_votes_1 > candidate_votes_2 + candidate_votes_3:
        winner = True
        if winner == True:
            the_winner = candidate_1
    elif candidate_votes_2 > candidate_votes_3 + candidate_votes_1:
        winner = True
        if winner == True:
            the_winner = candidate_2
    elif candidate_votes_3 > candidate_votes_1 + candidate_votes_2:
        winner = True
        if winner == True:
            the_winner = candidate_3

print(f"Total votes: {votes}")
print("--------------------------------")
print(f"{candidate_1}: {perc_1}% ({candidate_votes_1})")
print(f"{candidate_2}: {perc_2}% ({candidate_votes_2})")
print(f"{candidate_3}: {perc_3}% ({candidate_votes_3})")
print("--------------------------------")
print("Winner: " + the_winner)
print("--------------------------------")