import pandas as pd

data = pd.read_csv('')

def parse_data():
	output = []
	for line in f:
		split_line = line.strip().split(',')
		split_line[10] = int(split_line[10])
		output.append(line.strip().split(','))
	return output

data = parse_data()
#print data
##How many different peopl can there be?

i = 0
for line in data:
	if i==0:
		output = line[0:10]
		i = 1
	else:
		output = output + line[0:10]
unique_player_types = set(output)

##print len(unique_player_types) ##97

for player_type in unique_player_types:
	print player_type

def is_in_line(player_type,line):
	if player_type in line:
		return 1
	else:
		return 0

final_data = []

for i in range(len(data)):
	for j in range(len(unique_player_types)):
		final_data[line][player_type] = is_in_line(unique_player_types[j],data[i])

print final_data