import os
import csv

budget_data_path = os.path.join("budget_data.csv")

with open(budget_data_path, mode="r") as budget_data:
    csvreader = csv.reader(budget_data)
    month_count = 0; net_total = 0; average_change = 0
    greatest_increase = 0 ; greatest_decrease = 0
    greatest_increase_row = str() ; greatest_decrease_row = str()
    previous_value = 0 ; average_change = 0
    next(csvreader)

    for row in csvreader:
        month_count += 1
        if month_count is not 1:
            average_change += previous_value - int(row[1])
        net_total += int(row[1])
        previous_value = int(row[1])
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_row = row
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_row = row

    print("Financial Analysis")
    print("-" * 30)
    print(f"Total Months: {month_count}")
    print(f"Total: ${net_total}")
    print("Average Change: $%.2f" % (average_change / (month_count - 1)))
    print(f"Greatest Increase in Profits: {greatest_increase_row[0]} ${greatest_increase_row[1]}")
    print(f"Greatest Decrease in Profits: {greatest_decrease_row[0]} ${greatest_decrease_row[1]}")

with open(os.path.join("budget_results.txt"), mode="w") as budget_results:
    budget_results.write("Financial Analysis\n")
    budget_results.write(("-" * 30) + "\n")
    budget_results.write(f"Total Months: {month_count} \n")
    budget_results.write(f"Total: ${net_total} \n")
    budget_results.write("Average Change: $%.2f\n" % (average_change / (month_count - 1)))
    budget_results.write(f"Greatest Increase in Profits: {greatest_increase_row[0]} ${greatest_increase_row[1]}\n")
    budget_results.write(f"Greatest Decrease in Profits: {greatest_decrease_row[0]} ${greatest_decrease_row[1]}\n")
    budget_results.close()