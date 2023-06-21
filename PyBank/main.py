import os
import csv

csv_path = os.path.join("PyBank", "Resources", "budget_data.csv")


# Variable Declarations:
month_counter = 0
net_change = 0
max_increase = 0
max_decrease = 0
prev_record = 0

prev_change = 0
rev_change = 0
rev_avg = 0

rev_change_list = []
increase_date = " "
decrease_date = " "

with open(csv_path, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header_row = next(csvreader)
    print(f'Header row is {header_row}')
    
    for row in csvreader:
    # Count the total number of rows of months in the file    
        month_counter += 1   
    # Add profit/losses for each row and store into net_change variable
        net_change = net_change + int(row[1])
    # Check the greatest increase and decrease in profits over the entire period 
        if int(row[1]) - prev_record > max_increase:
            max_increase = int(row[1]) - prev_record
            increase_date = str(row[0])
        
        if int(row[1]) - prev_record < max_decrease:
            max_decrease = int(row[1]) - prev_record
            decrease_date = str(row[0])
            
        prev_record = int(row[1])
        
    # Calculate average profit/losses changes over entire period
        rev_change = int(row[1]) - prev_change
        rev_change_list.append(rev_change)    
        prev_change = int(row[1])
  
    rev_avg = round((sum(rev_change_list) - 1088983) / int(len(rev_change_list)-1), 2)



print(f"There are {month_counter} months of data in this file")
print(f"The net total amount of Profits/Losses for this period is ${net_change}")
print(f"Greatest Increase in Profits: {increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${max_decrease})")   
print(f"Average Change: {rev_avg}")



output_path = os.path.join("Pybank", "analysis", "results.txt")

with open(output_path, 'w') as txt_file:
    text = (
        f"Financial Analysis\n"
        f"------------------------------\n"
        f"\n"
        f"Total Months: {month_counter}\n"
        f"\n"
        f"Total: ${net_change}\n"
        f"\n"
        f"Average Change: {rev_avg} \n"
        f"\n"
        f"Greatest Increase in Profits: {increase_date} (${max_increase})\n"
        f"\n"
        f"Greatest Decrease in Profits: {decrease_date} (${max_decrease})\n"
    )
    txt_file.write(text)

