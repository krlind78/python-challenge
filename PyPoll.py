import os
import csv

election_data = os.path.join("Resources", "election_data.csv")


total_votes= 0
count_dict = {}
c_names = []
#candidates
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




# total_months = 0
# monthly_change = []
# net_change= []

# total_net = 0
# grt_inc_month=0
# grt_dec_month=0
# grt_inc_value=0
# grt_dec_value=0
# with open(budget_csv) as csvfile:
#      csvreader = csv.reader(csvfile, delimiter=",")

#      csv_header = next(csvreader)
#      #print(f"CSV Header: {csv_header}")
#      next_row = next(csvreader)
#      total_months+=1
#      total_net=int(next_row[1])
#      prior_val=int(next_row[1])

     
#      for each in csvreader:
#            total_months=total_months+1 
#            total_net+=int(each[1])
 
#            net_change.append(int(each[1])-prior_val) 
                 
#            if grt_inc_value < int(each[1])-prior_val:
#                grt_inc_month=each[0]
#                grt_inc_value=int(each[1])-prior_val
#            if grt_dec_value > int(each[1])-prior_val:
#                grt_dec_month=each[0]
#                grt_dec_value=int(each[1])-prior_val

#            prior_val= int(each[1])  

#      print(total_months, total_net, prior_val, net_change,grt_inc_value, grt_inc_month, grt_dec_value, grt_dec_month)

#      avg_change=(sum(net_change)/len(net_change))
     
    


# output_path = os.path.join("Output", "PyBank_output.txt")

# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w') as txtfile:

#     txtfile.write(f"Total Months: {total_months} \n")
#     txtfile.write(f"Total: {total_net} \n")
#     txtfile.write(f"Average change:{avg_change} \n")
#     txtfile.write(f"Greatest Increase:{grt_inc_month} ,({grt_inc_value}) \n")
#     txtfile.write(f"Greatest Decrease: {grt_dec_month} ,({grt_dec_value})\n")

    
    



     








# import os
# import csv
#print(f"CSV Header: {csv_header}")
              
# budget_csv = os.path.join("Starter_Code", "PyBank", "Resourses", "budget_data.csv")
#                                      <------ right here create 6 Variables to track your financial parameters (total months, change, net change, greatest increase, greatest decrease, total net) 

# Freebie:
# variable for total months = 0
# variable for monthly change = []
# variable for net change= []
# greatest_increase = ["", 0]
# greatest_decrease = ["", 9999999999999999999]
# variable for total net = 0
                                           
# with open(budget_csv) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#                                     <-1. create a variable and read in the header row 
                                    
#                                     <--- 2.cuse the variable for total months and Add +1 to months so when it loops it will count 
#                                     <--- 3.take the variable for total net and set it to += the Integer of the header (HINT: var[1] <---var is a stand in/filler word you would replace it with the variable you made in step 1)
#                                     <--- 4.create a variable for previous net and set it equal to Integer of the header

#                                    <--- 5.start you for loop  --- > For row in csvreader: 

#                                      <---- 6.inside of the loop: track the total 
#                                               - a. you do this by taking the code from step2 and copy and pasting it here 
#                                               - b. freebie +=int(row[1])     
#                                      <----- 7.track the net change here 
#                                              - a. take the variable you made for net_change and set it equal to int(row[1]) minus the variable for previous net (the one made in step 4)
#                                              - b. then call the variable for previous net again and set it to int(row[1])
#                                              - c. call the variable for net change and use += on the the variable you made in step 7a making sure its in square brackets







# import os
# import csv
              
# budget_csv = os.path.join("Starter_Code", "PyBank", "Resourses", "budget_data.csv")
#                                      <------ right here create 6 Variables to track your financial parameters (total months, change, net change, greatest increase, greatest decrease, total net) 

# Freebie:
# variable for total months = 0
# variable for monthly change = []
# variable for net change= []
# greatest_increase = ["", 0]
# greatest_decrease = ["", 9999999999999999999]
# variable for total net = 0
                                           
# with open(budget_csv) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#                                     <-1. create a variable and read in the header row 
                                    
#                                     <--- 2.cuse the variable for total months and Add +1 to months so when it loops it will count 
#                                     <--- 3.take the variable for total net and set it to += the Integer of the header (HINT: var[1] <---var is a stand in/filler word you would replace it with the variable you made in step 1)
#                                     <--- 4.create a variable for previous net and set it equal to Integer of the header

#                                    <--- 5.start you for loop  --- > For row in csvreader: 

#                                      <---- 6.inside of the loop: track the total 
#                                               - a. you do this by taking the code from step2 and copy and pasting it here 
#                                               - b. freebie +=int(row[1])     
#                                      <----- 7.track the net change here 
#                                              - a. take the variable you made for net_change and set it equal to int(row[1]) minus the variable for previous net (the one made in step 4)
#                                              - b. then call the variable for previous net again and set it to int(row[1])
#                                              - c. call the variable for net change and use += on the the variable you made in step 7a making sure its in square brackets
