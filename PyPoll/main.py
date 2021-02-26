import os
import csv 

# Total number of months included in the data set

# Path to collect CSV data
current_directory = os.path.dirname(__file__)
poll_data = os.path.join(current_directory, 'Resources', 'election_data.csv')


# Read the CSV
with open(poll_data) as csv_file:
    poll = csv.reader(csv_file, delimiter=",")
    
    votes = 0
    correy_vote = 0
    Khan_vote = 0
    otooley_vote = 0
    li_vote = 0

    # Skip header row
    next(poll)

    for row in poll:
        # Total votes per candidate
        if row[2] == "Correy":
            correy_vote = correy_vote + 1
        if row[2] == "Khan":
            Khan_vote = Khan_vote + 1
        if row[2] == "O'Tooley":
            otooley_vote = otooley_vote + 1
        if row[2] == "Li":
            li_vote = li_vote + 1
        
        votes = votes + 1
        
        #Percentages
        correy_percent = float(correy_vote/votes)*100
        correy_percent = round(correy_percent, 3)
        Khan_percent = float(Khan_vote/votes)*100
        Khan_percent = round(Khan_percent, 3)
        otooley_percent = float(otooley_vote/votes)*100
        otooley_percent = round(otooley_percent, 3)
        li_percent = float(li_vote/votes)*100
        li_percent = round(li_percent, 3)

        final_votes = [correy_vote, Khan_vote, otooley_vote, li_vote]
        winner = max(final_votes)
        if winner == correy_vote:
            Elected = "Correy"
        elif winner == Khan_vote:
            Elected = "Khan"
        elif winner == otooley_vote:
            Elected = "O'Tooley"
        else:
            Elected = "Li"

    
    print(f"Election Results")
    print(f"--------------------")
    print(f"Total Votes: {votes}")
    print(f"--------------------")
    print(f"Correy: {correy_percent}% Total: {correy_vote}")
    print(f"Khan: {Khan_percent}% Total: {Khan_vote}")
    print(f"O'Tooley: {otooley_percent}% Total: {otooley_vote}")
    print(f"Li: {li_percent}% Total: {li_vote}")
    print(f"--------------------")
    print(f"Winner: {Elected}")
    print(f"--------------------")
    


#Total number of votes
#List of candidates who received votes
# percentage of votes each candidate won
# winner of election based on popular vote