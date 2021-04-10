import os
import csv

#load and output files
Pypoll = os.path.join('Resources', 'PyPoll_Resources_election_data.csv')
output_path = os.path.join('Analysis', 'PypollHW.txt')
#set up variables and lists


# percent_votes = []

winner_winner = []

# person_name = []

#read csv file

with open(Pypoll, 'r') as csvfile:
	total_num_votes = 0
	person_list = []
	total_num_votes = 0
	person_list = []
	total_num_votes_person = []
	unique_name = []
	csvreader = csv.reader(csvfile)
	header = next(csvreader)


		# print(line)

	for each in csvreader:
		total_num_votes += 1
			# total_num_votes_unique = each[0]
		if unique_name.count(each[2]) == 0:
			unique_name.append(each[2])
			total_num_votes_person.append(1)
		else:
			candidate = unique_name.index(each[2])
			total_num_votes_person[candidate] += 1
		results = [x/total_num_votes for x in total_num_votes_person]
		percent_votes = ["{0:.3%}".format(round((z) ,3)) for z in results]

	winner = 0
	index_total  = 0
	output = 'Election Results\n'
	for line in unique_name: 
		# print(line)
		index1 = unique_name.index(line)
		if winner < total_num_votes_person[index_total]:
			winner = total_num_votes_person[index_total]
			index2 = total_num_votes_person.index(winner)

		# output = (f'Election Results\n'
		output = output + f'{unique_name[index_total]} {total_num_votes_person[index_total]} {percent_votes[index_total]}\n'
			
		index_total = index_total + 1
	output = output + f"------------------------------\n"
	output = output + f"Total Votes: {total_num_votes}\n"
	output = output + f"Winner :{unique_name[index2]}"

	# print(f'{unique_name[index2]}')


			


# output = (f"{unique_name[index1]} {total_num_votes_person[index1]} {percent_votes[index1]}\n"
# 	f"{unique_name[index2]} {total_num_votes_person[index2]} {percent_votes[index2]}\n"
# 	f"{unique_name[index3]} {total_num_votes_person[index3]} {percent_votes[index3]}\n"
# 	f"{unique_name[index4]} {total_num_votes_person[index4]} {percent_votes[index4]}\n")

# 	f"Election Results\n"
# 	f"------------------------------\n"
# 	f"Total Votes: {total_num_votes}\n"
	
# 	f"Winner :{unique_name[index2]}")

print(output)

with open(output_path, "w") as txt_file:
	txt_file.write(output)