import os
import csv

csv_path = os.path.join("PyPoll", "Resources", "election_data.csv")

votes_count = 0
candidate_one_count = 0
candidate_two_count = 0
candidate_three_count = 0
candidate_one_percent = 0
candidate_two_percent = 0
candidate_three_percent = 0

candidate_list = []

with open(csv_path, encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    
    for row in csv_reader:
        #Count total number of votes cast
        votes_count += 1
        # Gets complete list of candidates
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        #Count the number of votes for each candidate
        if row[2] == candidate_list[0]:
             candidate_one_count += 1   
        elif row[2] == candidate_list[1]:
            candidate_two_count += 1
        elif row[2] == candidate_list[2]:
            candidate_three_count += 1
            
    #Calculate percentage of votes each candidate received
    candidate_one_percent = round(candidate_one_count/votes_count * 100, 3)
    candidate_two_percent = round(candidate_two_count/votes_count * 100, 3)
    candidate_three_percent = round(candidate_three_count/votes_count * 100, 3)
        
    
    print("Election Results")
    print("----------------------")   
    print()
    print(f"Total number of votes: {votes_count}")
    print("----------------------")
    print()
    print(f"{candidate_list[0]}: {candidate_one_percent}% ({candidate_one_count})")
    print(f"{candidate_list[1]}: {candidate_two_percent}% ({candidate_two_count})")
    print(f"{candidate_list[2]}: {candidate_three_percent}% ({candidate_three_count})")
    print("----------------------")   
    print()
    
    #Check which candidate got the most votes
    if candidate_one_count > candidate_two_count and candidate_one_count > candidate_three_count:
        winner = candidate_list[0]
    elif candidate_two_count > candidate_one_count and candidate_two_count > candidate_three_count:
        winner = candidate_list[1]
    elif candidate_three_count > candidate_one_count and candidate_three_count > candidate_two_count:
        winner = candidate_list[2]

    print(f"Winner: {winner}")		
    print("----------------------")   
    

output_file = os.path.join("PyPoll", "analysis", "Results.txt")
    
with open(output_file, 'w') as txt_file:
    text = (
        f"Election Results\n"
        f"----------------------\n"
        f"\n"
        f"Total number of votes: {votes_count}\n"
        f"----------------------\n"
        f"\n"
        f"{candidate_list[0]}: {candidate_one_percent}% ({candidate_one_count})\n"
        f"{candidate_list[1]}: {candidate_two_percent}% ({candidate_two_count})\n"
        f"{candidate_list[2]}: {candidate_three_percent}% ({candidate_three_count})\n"
        f"----------------------\n" 
        f"\n"  
        f"Winner: {winner}\n"
        f"----------------------\n" 
    )
    txt_file.write(text)