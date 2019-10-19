# 1. Create a list for the Counties
# 2. Create a dictionary where the county is the key and the votes cast for each county are the values
# 3. Create an empty string that will hold the county name that had the largest turnout
# 4. Declare a variable that represents the number of votes that a county received
# 5. Create three if statements to print out the voter turnout results similar to the results shown above
# 6. add results to output file
# 7. print results to command line

import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources\election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis2.txt")
# Initialize a total vote counter.
total_votes = 0
candidate_total_votes = 0
# 1. Create a list for the Counties
county_list = []
# County votes Dictionary
county_votes = {}

largest_turnout = ""
largest_count = 0
largest_percentage = 0

# Candidate Options
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total county vote count.
        total_votes += 1   
        # Add to the total candidate vote count.
        candidate_total_votes += 1  

        # Storing the county name from each row.
        county_name = row[1]
        # Storing the candidate name from each row
        candidate_name = row[2]

        # If the county does not match any existing county...
        if county_name not in county_list:
            # Add it to the list of candidates.
            county_list.append(county_name)
            # Begin tracking that county's vote count. 
            county_votes[county_name] = 0

        # Add a vote to that county's count.
        county_votes[county_name] += 1
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
# Print the candidate list.
# print(county_list)

# 2. Create a dictionary where the county is the key and the votes cast for each county are the values
# print(county_votes)

# 3. Create an empty string that will hold the county name that had the largest turnout

    with open(file_to_save, "w") as txt_file:
        election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)
        
        print(county_votes)
        # txt_file.write(str(county_votes))
        for county in county_votes:
            # txt_file.write(county)
            # 2. Retrieve vote count of a county.
            votes = county_votes[county]
            # 3. Calculate the percentage of votes.
            vote_percentage = int(votes) / int(total_votes) * 100
            # 4. Print the county name and percentage of votes.
            county_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
            # Print each candidate, their voter count, and percentage to the terminal.
            print(county_results)
            #  Save the candidate results to our text file.
            
            txt_file.write(county_results)
            
            # Determine winning highest vote count and county
            # Determine if the votes is greater than the winning count.
            if (votes > largest_count) and (vote_percentage > largest_percentage):
                # If true then set largest_count = votes and largest_percent =
                # vote_percentage.
                largest_count = votes
                largest_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
                largest_turnout = county
        county_turnout_summary = (
            f"-------------------------\n"
            f"Largest County Turnout: {largest_turnout}\n"
            f"-------------------------\n")
        
        print(county_turnout_summary)
        # Save the county with largest turnout name to the text file.
        txt_file.write(county_turnout_summary)
        for candidate in candidate_votes:
            # 2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate]
            # 3. Calculate the percentage of votes.
            vote_percentage = int(votes) / int(total_votes) * 100
            # 4. Print the candidate name and percentage of votes.
            candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        
        print(winning_candidate_summary)
        # Save the winning candidate's name to the text file.
        txt_file.write(winning_candidate_summary)

# ---------------
#Winnning Candidate Analysis & Summary
# ---------------
# 1. The total number of votes cast
# 2. A complete list of Candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
# ---------------
# 1. Initialize a total vote counter.
# total_votes = 0

# Open the election results and read the file.
#with open(file_to_load) as election_data:
    # file_reader = csv.reader(election_data)
    # Read the header row. 
    # headers = next(file_reader)
   
# Print each row in the CSV file.
#for row in file_reader:
    # Add to the total vote count.
    # candidate_total_votes += 1 
        
    # Print the candidate name from each row.
    # candidate_name = row[2]

    # if candidate_name not in candidate_options:
        # Add the candidate name to the candidate list.
        # candidate_options.append(candidate_name)

        # 2. Begin tracking that candidate's vote count. 
        # candidate_votes[candidate_name] = 0

    # Add a vote to that candidate's count.
    # candidate_votes[candidate_name] += 1
    # Save the results to our text file.
    
    #with open(file_to_save, "w") as txt_file:
    # election_results = (
    # f"\nElection Results\n"
    # f"-------------------------\n"
    # f"Total Votes: {total_votes:,}\n"
    # f"-------------------------\n")
    #print(election_results, end="")
    # Save the final vote count to the text file.
    # txt_file.write(election_results)

    # print(candidate_votes)
       
        