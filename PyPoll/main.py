import os
import csv


input_path = os.path.join('Resources\election_data.csv')
output_path = os.path.join('Analysis', 'poll_analysis.txt')


candidate_list = []
candidate_count = []
votes=[]
vote_pct = []

votes = 0


with open (input_path, 'r', encoding='utf8') as election_file:
    election_reader = csv_reader(election_file, delimiter=",")

election_header = next(election_reader)
for row in election_reader:
    
    votes=votes + 1




#Acomplete list of candidates who received votes 


# loop thru names and append name in a dictionary if not in list already


    if row[2] not in candidate_list:
        candidate_list.append(row[2])


#The percentage of votes each candidate won




#The total number of votes each candidate won

    for candidate in candidate_list:
        candidate_count.append(votes.count(candidate))
        vote_pct.append(round(votes.count(candidate)/votes*100,3))


#The winner of the election based on popular vote

winner = max(set(candidate_list), key=candidate_list.count)


# Print the results
print('Election Resuls')
print('-------------------------')
print(f'Total Votes: {votes}')
print('-------------------------')
for i in range(len(candidate_list)):
    print(f'{candidate_list[i]}: {vote_pct[i]}% ({candidate_count[i]})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

with open(output_path, "w") as txt_file:
    txt_file.write('Election Resuls')
    txt_file.write('\n-------------------------')
    txt_file.write(f'\nTotal Votes: {votes}')
    txt_file.write('\n-------------------------')
    for i in range(len(candidate_list)):
        txt_file.write(f'\n{candidate_list[i]}: {vote_pct[i]}% ({candidate_count[i]})')
    txt_file.write('\n-------------------------')
    txt_file.write(f'\nWinner: {winner}')
    txt_file.write('\n-------------------------')