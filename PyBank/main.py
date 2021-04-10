import os
import csv

#load and output files
Bank = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join("Resources", "PythonHW.txt")

#track the variables
Total_Months = 0
TotalM = []
Net_PLchange = []
Great_Increase =["", 0]
Great_Decreas = ["", 99]
Total_net = 0

#read csv file
with open(Bank, 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	header = next(csvreader)

	Line = next(csvreader)
	Total_net += int(Line[1])
	Total_Months += 1
	last_net = int(Line[1])
	
	for row in csvreader:
		#Total
		Total_net += int(row[1])
		Total_Months += 1
		#Track net
		net_change = int(row[1]) - last_net
		last_net = int(row[1])
		Net_PLchange += [net_change]
		TotalM += [row[0]]

		if net_change > Great_Increase[1]:
			Great_Increase[0] = row[0]
			Great_Increase[1] = net_change

		if net_change < Great_Decreas[1]:
			Great_Decreas[0] = row[0]
			Great_Decreas[1] = net_change
#Average PL
Average_PL = sum(Net_PLchange) / len(Net_PLchange)
		
# print (Total_PL)
# print (TotalM)
	

output = (
   f"Fin Analysis\n"
   f"----------------------------\n"
   f"Total Months: {Total_Months}\n"
   f"Total: ${Total_net}\n"
   f"Average  Change: ${Average_PL:.2f}\n"
   f"Greatest Increase in Profits: {Great_Increase[0]} (${Great_Increase[1]})\n"
   f"Greatest Decrease in Profits: {Great_Decreas[0]} (${Great_Decreas[1]})\n")
# Print the output (to terminal)
print(output)
# Export the results to text file
with open(output_path, "w") as txt_file:
   txt_file.write(output)
