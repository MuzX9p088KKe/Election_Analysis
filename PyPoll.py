# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
   # Read and print the header row.
    headers = next(file_reader)
    print(headers)

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

