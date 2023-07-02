import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")


total_months = 0
net_change= []
total_net = 0
grt_inc_month=0
grt_dec_month=0
grt_inc_value=0
grt_dec_value=0
with open(budget_csv) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")

     csv_header = next(csvreader)
     
     next_row = next(csvreader)
     total_months+=1
     total_net=int(next_row[1])
     prior_val=int(next_row[1])

     
     for each in csvreader:
           total_months=total_months+1 
           total_net+=int(each[1])
 
           net_change.append(int(each[1])-prior_val) 
                 
           if grt_inc_value < int(each[1])-prior_val:
               grt_inc_month=each[0]
               grt_inc_value=int(each[1])-prior_val
           if grt_dec_value > int(each[1])-prior_val:
               grt_dec_month=each[0]
               grt_dec_value=int(each[1])-prior_val

           prior_val= int(each[1])  

     print(total_months, total_net, prior_val, net_change,grt_inc_value, grt_inc_month, grt_dec_value, grt_dec_month)

     avg_change=(sum(net_change)/len(net_change))
     
    


output_path = os.path.join("Output", "PyBank_output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    txtfile.write(f"Total Months: {total_months} \n")
    txtfile.write(f"Total: {total_net} \n")
    txtfile.write(f"Average change:{avg_change} \n")
    txtfile.write(f"Greatest Increase:{grt_inc_month} ,({grt_inc_value}) \n")
    txtfile.write(f"Greatest Decrease: {grt_dec_month} ,({grt_dec_value})\n")

    
    



     








