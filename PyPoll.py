# Data I need to retrieve 
# 1 Open the data file.

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
<<<<<<< HEAD
#Initialize a total vote counter.
total_votes=0
#declare a new list statment for candidate
candidate_options = []
#Declare the empty dictionary.
candidate_votes = {}
#fining the winner and seting variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
# Read the file object with the reader function.
  file_reader = csv.reader(election_data)
  # Read the header row.
  headers = next(file_reader)
  
  #Print each row in the CSV file. 
  for row in file_reader:
#2. Add to the total vote count.
    total_votes += 1
# Print the candidate name from each row.
    candidate_name= row[2]
# If the candidate does not match any existing candidate...
    if candidate_name not in candidate_options:
      # Add it to the list of candidates.
      candidate_options.append(candidate_name)
      #Begin tracking the candidate's vote count
      candidate_votes[candidate_name] = 0
    candidate_votes[candidate_name] += 1
# print(candidate_votes)

for candidate_name in candidate_votes:
# 2. Retrieve vote count of a candidate
  votes = candidate_votes[candidate_name]
# 3. Calculate the percentage of votes.
  vote_percentage = float(votes) / float(total_votes) * 100
# 4. Print the candidate name and percentage of votes.
  candidate_votes[candidate_name] += 1
  # print(f"{candidate_name}: received {vote_percentage}% of the vote.")

  print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


  # Determine winning vote count and candidate
  # 1. Determine if the votes are greater than the winning count.
  if (votes > winning_count) and (vote_percentage > winning_percentage):
  # 2.If true then set winning_count = votes and winning_percent =vote_percentage.
    winning_count = votes
    winning_percentage = vote_percentage
  # 3. Set the winning_candidate equal to the candidate's name.
    winning_candidate = candidate_name
    
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
=======

# Open the election results and read the file.
with open(file_to_load) as election_data:
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
  # Print the header row.
    headers = next(file_reader)
    print(headers)

# # Print each row in the CSV file.
#  for row in file_reader:
#     print(row)
>>>>>>> 7aaf67b2b365a4e367e65ccbb31ee115b26afd74

# 2 Write down the names of all the candidates.
# 3 Add a vote count for each candidate.
# 4 Get the total votes for each candidate.
# 5 Get the total votes cast for the election.