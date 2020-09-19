import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")

with open(budget_csv,'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    Total_Profit = 0
    Profit_Delta = []
    Date_List = []
    Previous = 0
    for row in csv_reader:
        Date = row[0]
        Profit_Loss = int(row[1])
        Total_Profit = Total_Profit + Profit_Loss
        # Delta = current - previous
        Profit_Delta.append(Profit_Loss - Previous)
        Previous = Profit_Loss
        Date_List.append(Date)

    Maximum_Delta = max(Profit_Delta)
    Max_Delta_Index = Profit_Delta.index(Maximum_Delta) 
    C_Max_Date = Date_List[(Max_Delta_Index)]
    Minimum_Delta = min(Profit_Delta)
    Min_Delta_Index = Profit_Delta.index(Minimum_Delta)
    C_Min_Date = Date_List[(Min_Delta_Index)]
    Number_Of_Months = len(Date_List)
    Average_Change = round(sum(Profit_Delta[1:87]) / (Number_Of_Months - 1),2)
 
    print(f"Total Months: {Number_Of_Months}"),
    print(f"Total: ${Total_Profit}"),
    print(f"Average: ${Average_Change}"),
    print(f"Greatest Increase in Profits: {C_Max_Date} (${Maximum_Delta})"),
    print(f"Greatest Decrease in Profits: {C_Min_Date} (${Minimum_Delta})"),

    output_path = os.path.join('Analysis','analysis.txt')
    with open(output_path, 'w') as txtfile:
        txtwriter = csv.writer(txtfile, delimiter=",")

        txtwriter.writerow([(f"Total Months: {Number_Of_Months}")])
        txtwriter.writerow([(f"Total: ${Total_Profit}")])
        txtwriter.writerow([(f"Average: ${Average_Change}")])
        txtwriter.writerow([(f"Greatest Increase in Profits: {C_Max_Date} (${Maximum_Delta})")])
        txtwriter.writerow([(f"Greatest Decrease in Profits: {C_Min_Date} (${Minimum_Delta})")])






 
    

        


