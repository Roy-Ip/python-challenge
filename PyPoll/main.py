import os
import csv

election_data_csv = os.path.join('Resources', 'election_data.csv')

def election_result(election_data):
    total_vote = 0
    charles_vote = 0
    diana_vote = 0
    raymon_vote = 0
    charles_percent = 0
    diana_percent = 0
    raymon_percent = 0
    candidate_percent = []
    winner_candidate = []
    
    with open(election_data, 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",")
            header = next(csvreader)

            for row in csvreader:
                total_vote = total_vote +1

                if row[2] == "Charles Casper Stockham":
                        charles_vote = charles_vote + 1

                elif row[2] == "Diana DeGette":
                        diana_vote = diana_vote + 1

                elif row[2] == "Raymon Anthony Doane":
                        raymon_vote = raymon_vote + 1
    

    charles_percent = (charles_vote / total_vote) * 100
    diana_percent = (diana_vote / total_vote) * 100
    raymon_percent = (raymon_vote / total_vote) * 100

    candidate_percent = {
                        "Charles Casper Stockham" : charles_percent,
                        "Diana DeGette" : diana_percent,
                        "Raymon Anthony Doane" : raymon_percent            
                        }
    
    winner_candidate = max(candidate_percent, key=candidate_percent.get)


    return total_vote, charles_vote, diana_vote, raymon_vote, charles_percent, diana_percent, raymon_percent, candidate_percent, winner_candidate

total_vote, charles_vote, diana_vote, raymon_vote, charles_percent, diana_percent, raymon_percent, candidate_percent, winner_candidate = election_result(election_data_csv)


election_result_text = f"""
Election Results
-------------------------------------------
Total Votes: {total_vote}
-------------------------------------------
Charles Casper Stockham: {charles_percent:.3f}% ({charles_vote})
Diana DeGette: {diana_percent:.3f}% ({diana_vote})
Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_vote})
-------------------------------------------
Winner: {winner_candidate}
-------------------------------------------"""

print(election_result_text)


output_path = os.path.join("Analysis", "Election Result.txt")

with open(output_path, 'w') as txtfile:

    txtfile.write(election_result_text)






                


