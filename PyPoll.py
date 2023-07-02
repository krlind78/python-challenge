import os
import csv

election_data = os.path.join("Resources", "election_data.csv")


total_votes= 0
count_dict = {}
c_names = []
win_name = ""
win_per = 0


with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    
    
    

    for row in csvreader:

        total_votes += 1 

        if row[2] not in c_names:
            c_names.append(row[2])
            count_dict[row[2]] = 0

        count_dict[row[2]] = count_dict[row[2]] + 1

       
    for ele in count_dict:

        votes = count_dict[ele]
        per_votes = float(votes)/float(total_votes) * 100

        if per_votes > win_per:
            win_per = per_votes
            win_name = ele
    
    
        
        
        
with open("election_results.txt", "w") as txt_file:
    results = (f"\nElection Results\n"
               f"--------------------\n"
               f'Total Votes: {total_votes}\n'
               f'--------------------\n')
    print(results)
    txt_file.write(results)
    for ele in count_dict:

        votes = count_dict[ele]
        per_votes = float(votes)/float(total_votes) * 100

        if per_votes > win_per:
            win_per = per_votes
            win_name = ele
        can_info = (f"{ele}: {per_votes:.3f}% ({votes})\n")
        print(can_info)
        txt_file.write(can_info)

    winner = (
               f"--------------------\n"
               f'Winner: {win_name}\n'
               f'--------------------\n')
    print(winner)
    txt_file.write(winner) 
    


        
        

   
      
      








# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote




