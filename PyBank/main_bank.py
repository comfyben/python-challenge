
import os
import csv


bank_path = os.path.join("Resources", "budget_data.csv")

print("FINANCIAL ANALYSIS")
print("-------------------------")

with open(bank_path) as bankfile:
    bankreader = csv.reader(bankfile, delimiter=",")
    bankheader = next(bankreader)

    month_list = []
    pl_list = []
    change_list = []
    month_count = 0
    profit_total = 0
    firstloop = True
    prev_row = 1088983
    for row in bankreader:
        month_list.append(row[0])
        pl_list.append(row[1])
        month_count = month_count + 1
        profit_total = profit_total + int(row[1])
        if firstloop == True:
            firstloop = False
            profit_change = 0
        elif int(row[1]) > 0:
            if prev_row > 0:
                profit_change = int(row[1]) - prev_row
                prev_row = int(row[1])
            elif prev_row < 0:
                profit_change = int(row[1]) + (prev_row * -1)
                prev_row = int(row[1])
        elif int(row[1]) < 0:
            if prev_row > 0:
                profit_change = int(row[1]) +(prev_row * -1)
                prev_row = int(row[1])
            elif prev_row < 0:
                profit_change = int(row[1]) - prev_row
                prev_row = int(row[1])
    
        
        change_list.append(profit_change)

change_total = sum(change_list)
       
profit_avg = change_total/month_count
max_increase = max(change_list)
min_decrease = min(change_list)
j = 0
for i in change_list:
    j = j + 1
    if i == max_increase:
        month_high = month_list[j - 1]


k = 0
for l in change_list:
    k = k + 1
    if l == min_decrease:
        month_low = month_list[k - 1]
        
print(f"Total Months: {month_count}")
print(f"Total: ${profit_total}")
print(f"Average Change: ${round(profit_avg, 2)}")
print(f"Greatest Increase in Profits: {month_high} ({max_increase})" )
print(f"Greatest Decrease in Profits: {month_low} ({min_decrease})")

