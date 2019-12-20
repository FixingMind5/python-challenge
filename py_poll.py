import os
import csv

election_data_path = os.path.join("election_data.csv")

votes_splited = {
    "Khan": 0,
    "Correy": 0,
    "Li": 0,
    "O'Tooley": 0
}

with open(election_data_path, mode="r") as election_data:
    csvreader = csv.reader(election_data)
    votes_count = 0
    # votes_splited = [khan_votes, correy_votes, li_votes, tooley_votes]
    greatest_votes_for_candidate = 0; winner_candidate = str()

    next(csvreader)

    for row in csvreader:
        votes_count += 1
        if row[2] == "Khan":
            votes_splited["Khan"] += 1
        elif row[2] == "Correy":
            votes_splited["Correy"] += 1
        elif row[2] == "Li":
            votes_splited["Li"] += 1
        elif row[2] == "O'Tooley":
            votes_splited["O'Tooley"] += 1
        else:
            pass
    
print("Election Result")
print("-" * 30)
print(f"Total votes: {votes_count}")
print("-" * 30)
print("Khan: {}% ({})".format(round(votes_splited["Khan"] * 100 / votes_count, 4), votes_splited["Khan"]))
print("Correy: {}% ({})".format(round(votes_splited["Correy"] * 100 / votes_count, 4), votes_splited["Correy"]))
print("Li: {}% ({})".format(round(votes_splited["Li"] * 100 / votes_count, 4), votes_splited["Li"]))
print("O'Tooley: {}% ({})".format(round(votes_splited["O'Tooley"] * 100 / votes_count, 4), votes_splited["O'Tooley"]))
for key in votes_splited:
    if greatest_votes_for_candidate < votes_splited[key]:
        greatest_votes_for_candidate = votes_splited[key]
        winner_candidate = key

print("-" * 30)
print(f"Winner: {winner_candidate}")
print("-" * 30)

with open(os.path.join("poll_results.txt"), mode="w") as f:
    f.writelines([
        "Election Result\n",
        ("-" * 30) + "\n",
        f"Total votes: {votes_count}\n",
        ("-" * 30) + "\n",
        "Khan: " + str(round(votes_splited["Khan"] * 100 / votes_count, 4)) + "% (" + str(votes_splited["Khan"]) + ")\n",
        "Correy: " + str(round(votes_splited["Correy"] * 100 / votes_count, 4)) + "% (" + str(votes_splited["Correy"]) + ")\n",
        "Li: " + str(round(votes_splited["Li"] * 100 / votes_count, 4)) + "% (" + str(votes_splited["Li"]) + ")\n",
        "O'Tooley: " + str(round(votes_splited["O'Tooley"] * 100 / votes_count, 4)) + "% (" + str(votes_splited["O'Tooley"]) + ")\n",
        ("-" * 30) + "\n",
        f"Winner: {winner_candidate} \n",
        ("-" * 30) + "\n",
    ])