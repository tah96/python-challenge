import csv
import os

file_path = os.path.join('Resources', 'election_data.csv')

with open(file_path,'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    VID_List = []
    Candidates_List_Unique= []
    Votes_Khan= []
    Votes_Correy = []
    Votes_Li = []
    Votes_Tooley= []
    for row in csv_reader:
        Voter_ID = row[0]
        County = row[1]
        Candidate = row[2]
        VID_List.append(Voter_ID)
        if Candidate not in Candidates_List_Unique:
            Candidates_List_Unique.append(Candidate)
        if Candidate == 'Khan':
            Votes_Khan.append(Voter_ID)
        elif Candidate == 'Correy':
            Votes_Correy.append(Voter_ID)
        elif Candidate == 'Li':
            Votes_Li.append(Voter_ID)
        else: 
            Votes_Tooley.append(Voter_ID)

    Winner = []
    if max(len(Votes_Khan),len(Votes_Correy),len(Votes_Li),len(Votes_Tooley)) == len(Votes_Khan):
        Winner.append(Candidates_List_Unique[0])
    elif max(len(Votes_Khan),len(Votes_Correy),len(Votes_Li),len(Votes_Tooley)) == len(Votes_Correy):
        Winner.append(Candidates_List_Unique[1])
    elif max(len(Votes_Khan),len(Votes_Correy),len(Votes_Li),len(Votes_Tooley)) == len(Votes_Li):
        Winner.append(Candidates_List_Unique[2])
    else:
        Winner.append(Candidates_List_Unique[3])
    
    Total_Voters = len(VID_List)

    print("")
    print("Election Results")
    print("---------------------------")
    print(f"Total Votes: {Total_Voters}")
    print("___________________________")
    print(f"{Candidates_List_Unique[0]}: {round(((len(Votes_Khan)/Total_Voters)*100),2)}% ({len(Votes_Khan)})")
    print(f"{Candidates_List_Unique[1]}: {round(((len(Votes_Correy)/Total_Voters)*100),2)}% ({len(Votes_Correy)})")
    print(f"{Candidates_List_Unique[2]}: {round(((len(Votes_Li)/Total_Voters)*100),2)}% ({len(Votes_Li)})")
    print(f"{Candidates_List_Unique[3]}: {round(((len(Votes_Tooley)/Total_Voters)*100),2)}% ({len(Votes_Tooley)})")
    print("---------------------------")
    print(f"Winner: {Winner[0]}")
    print("--------------------------")
    print("")

    output_path = os.path.join('analysis','analysis.txt')
    with open(output_path, 'w') as txtfile:
        txtwriter = csv.writer(txtfile, delimiter=",")

        txtwriter.writerow([("")])
        txtwriter.writerow([("Election Results")])
        txtwriter.writerow([("------------------")])
        txtwriter.writerow([(f"Total Votes: {Total_Voters}")])
        txtwriter.writerow([("___________________________")])
        txtwriter.writerow([(f"{Candidates_List_Unique[0]}: {round(((len(Votes_Khan)/Total_Voters)*100),2)}% ({len(Votes_Khan)})")])
        txtwriter.writerow([(f"{Candidates_List_Unique[1]}: {round(((len(Votes_Correy)/Total_Voters)*100),2)}% ({len(Votes_Correy)})")])
        txtwriter.writerow([(f"{Candidates_List_Unique[2]}: {round(((len(Votes_Li)/Total_Voters)*100),2)}% ({len(Votes_Li)})")])
        txtwriter.writerow([(f"{Candidates_List_Unique[3]}: {round(((len(Votes_Tooley)/Total_Voters)*100),2)}% ({len(Votes_Tooley)})")])
        txtwriter.writerow([("---------------------------")])
        txtwriter.writerow([(f"Winner: {Winner[0]}")])
        txtwriter.writerow([("--------------------------")])
        txtwriter.writerow([("")])
    
        