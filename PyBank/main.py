import os 
import csv

budget_data_csv = os.path.join('Resources', 'budget_data.csv')

def financial_analysis(budget_data):
    total_month = 0
    net_total = 0
    profit_loss_list = []
    month_list = []

    with open(budget_data, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)

        for row in csvreader: 
            month = str(row[0])
            profit_loss = int(row[1])

            total_month = total_month + 1
            net_total = net_total + profit_loss

            profit_loss_list.append(profit_loss)
            month_list.append(month)

        change = [profit_loss_list[i + 1] - profit_loss_list[i] for i in range(len(profit_loss_list) - 1)]
        average_change = sum(change) / len(change)

        greatest_increase = max(change)
        greatest_decrease = min(change)

        increase_month = month_list[change.index(greatest_increase) + 1] 
        decrease_month = month_list[change.index(greatest_decrease) + 1]

    return total_month, net_total, average_change, increase_month, decrease_month, greatest_increase, greatest_decrease
    
total_month, net_total, average_change, increase_month, decrease_month, greatest_increase, greatest_decrease = financial_analysis(budget_data_csv)


analysis_result = f"""
Financial Analysis
--------------------------------------
Total Months: {total_month}
Total: ${net_total}
Average Change: ${round(average_change, 2)}
Greatest Increase in Profits: {increase_month} (${greatest_increase})
Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})"""


print(analysis_result)


output_path = os.path.join("Analysis", "Analysis Result.txt")

with open(output_path, 'w') as txtfile:

    txtfile.write(analysis_result)

