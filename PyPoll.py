# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# 2. Candidate Options
candidate_options = []

# 3. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
  
  # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

                # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            
             # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count. Must be out of IF statement
        candidate_votes[candidate_name] += 1
      
# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

# To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
# # Print the candidate list.
# print(candidate_options)

# # 4. Print the total votes.
# print(total_votes)

# # Print the candidate vote dictionary.
# print(candidate_votes)

# Write down the names of all the candidates.

# Add a vote count for each candidate.

# Get the total votes for each candidate.

# Get the total votes cast for the election.


# Open the data file.
    # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
    
#     # Open the election results and read the file.
# #election_data = open(file_to_load, 'r') - The with statement opens the file and ensures proper acquisition or release of any data without having to close the file, to ensure that the data isn't lost or corrupted.
# with open(file_to_load) as election_data:
#         # To do: perform analysis. Indent as "with" ends with as colon
#     print(election_data)





# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("Analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")

# # Close the file
# outfile.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# # Write three counties to the file. Method 1:
#     txt_file.write("Arapahoe, ")
#     txt_file.write("Denver, ")
#     txt_file.write("Jefferson, ")

# # Write three counties to the file. Method 2:
#      txt_file.write("Arapahoe, Denver, Jefferson")

 # Write three counties to the file. New line each method
     txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

