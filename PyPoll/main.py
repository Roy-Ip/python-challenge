# Modules
import os
import csv

# Set path for csv file
election_data_csv = os.path.join('Resources', 'election_data.csv')

# Function to perform electino result
def election_result(election_data):
    
    total_vote = 0                      # Variable to store total number of votes
    charles_vote = 0                    # Variable to store number of votes for Charles
    diana_vote = 0                      # Variable to store the number of votes for Diana
    raymon_vote = 0                     # Variable to store the number of votes for Raymon
    charles_percent = 0                 # Variable to store the percentage of votes for Charles
    diana_percent = 0                   # Variable to store the percentage of votes for Diana
    raymon_percent = 0                  # Variable to store the percentage of votes for Raymon
    candidate_percent = []              # Dictionary to store the percentage for each candidate      
    winner_candidate = []               # Varianbe to store the name of the winner candidate
    
    # Open csv file 
    with open(election_data, 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",")
            header = next(csvreader)            # Skip the header row

            # Loop through each row    
            for row in csvreader:
                total_vote = total_vote +1                      # Adding up the total number of votes

                if row[2] == "Charles Casper Stockham":
                        charles_vote = charles_vote + 1         # Adding up the number of votes for Charles 

                elif row[2] == "Diana DeGette":
                        diana_vote = diana_vote + 1             # Adding up the number of votes for Diana

                elif row[2] == "Raymon Anthony Doane":                 
                        raymon_vote = raymon_vote + 1           # Adding up the number of votes for Raymon
    

    # Calculate the percentage of votes for each candidate
    charles_percent = (charles_vote / total_vote) * 100
    diana_percent = (diana_vote / total_vote) * 100
    raymon_percent = (raymon_vote / total_vote) * 100

    # Store the percentage of votes for each candidate in a dictionary
    candidate_percent = {
                        "Charles Casper Stockham" : charles_percent,
                        "Diana DeGette" : diana_percent,
                        "Raymon Anthony Doane" : raymon_percent            
                        }
    
    # Find the winner candidate with the highest percentage of vote
    winner_candidate = max(candidate_percent, key=candidate_percent.get)

    # Return the election result
    return total_vote, charles_vote, diana_vote, raymon_vote, charles_percent, diana_percent, raymon_percent, candidate_percent, winner_candidate

# Get the financial analysis result from the function
total_vote, charles_vote, diana_vote, raymon_vote, charles_percent, diana_percent, raymon_percent, candidate_percent, winner_candidate = election_result(election_data_csv)

# Create a text summary of the election results
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

# Print the election result
print(election_result_text)

# Set path for output text file
output_path = os.path.join("Analysis", "Election Result.txt")

#  Open the output text file
with open(output_path, 'w') as txtfile:
    
    # Write the election result to a text file
    txtfile.write(election_result_text)






                


