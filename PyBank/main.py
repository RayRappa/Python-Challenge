import os
import csv
input_path = os.path.join('resources', 'budget_data.csv')
output_path = os.path.join('analysis', 'pnl_analysis.txt')
revenue_changes = []
total_months = 0
total_revenue = 0
previous_revenue = 0
revenue_change = 0
largest_increase = ["", 0]
largest_decrease = ["", 9999999999999999999999]
with open(input_path, 'r', encoding='utf8') as pnl_file:
    pnl_reader = csv.reader(pnl_file, delimiter=',')
    pnl_header = next(pnl_reader)
    for row in pnl_reader:
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])
        revenue_change = int(row[1]) - previous_revenue
        prev_revenue = int(row[1])
        if (revenue_change > largest_increase[1]):
            largest_increase[1] = revenue_change
            largest_increase[0] = row[0]
        if (revenue_change < largest_decrease[1]):
            largest_decrease[1] = revenue_change
            largest_decrease[0] = row[0]
        revenue_changes.append(int(row[1]))
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + "$" + str(total_revenue))
    print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes), 2)))
    print("Greatest Increase: " + str(largest_increase[0]) + " ($" +  str(largest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(largest_decrease[0]) + " ($" +  str(largest_decrease[1]) + ")")
with open(output_path, "w") as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("----------------------------")
    txt_file.write("\n")
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes), 2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(largest_increase[0]) + " ($" + str(largest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(largest_decrease[0]) + " ($" + str(largest_decrease[1]) + ")")