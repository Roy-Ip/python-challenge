# Modules
import os 
import csv

# Set path for csv file
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# Function to perform financial analysis result
def financial_analysis(budget_data):
    total_month = 0             # Variable to store the total number of months
    net_total = 0               # Variable to store the net profit/loss
    profit_loss_list = []       # List to store profit/loss values
    month_list = []             # List to store the months

    # Open csv file
    with open(budget_data, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)        # Skip the header row

        for row in csvreader: 
            month = str(row[0])         # Get the month value
            profit_loss = int(row[1])   # Get the profit/loss value

            total_month = total_month + 1           # Adding up the total number of months
            net_total = net_total + profit_loss     # Adding up the total profit/loss

            profit_loss_list.append(profit_loss)    # Append profit/loss to the list
            month_list.append(month)                # Append months to the list

        # Calculate the changes in profit/loss between months
        change = [profit_loss_list[i + 1] - profit_loss_list[i] for i in range(len(profit_loss_list) - 1)]
        
        # Calculate the average change in profit/loss
        average_change = sum(change) / len(change)

        # Find the greatest increase and the greatest decrease in profit/loss
        greatest_increase = max(change)
        greatest_decrease = min(change)

        # Find the corresponding month with the greatest increase and the greatest decrease in profit/loss
        increase_month = month_list[change.index(greatest_increase) + 1] 
        decrease_month = month_list[change.index(greatest_decrease) + 1]

    # Return the finanical analysis result
    return total_month, net_total, average_change, increase_month, decrease_month, greatest_increase, greatest_decrease

# Get the financial analysis result from the function
total_month, net_total, average_change, increase_month, decrease_month, greatest_increase, greatest_decrease = financial_analysis(budget_data_csv)

# Create a text summary of the financial analysis results
analysis_result = f"""
Financial Analysis
--------------------------------------
Total Months: {total_month}
Total: ${net_total}
Average Change: ${round(average_change, 2)}
Greatest Increase in Profits: {increase_month} (${greatest_increase})
Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})"""

# Print the financial analysis result
print(analysis_result)

# Set path for output text file
output_path = os.path.join("Analysis", "Analysis Result.txt")

#  Open the output text file
with open(output_path, 'w') as txtfile:

    # Write the financial analysis result to a text file
    txtfile.write(analysis_result)

