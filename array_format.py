# Format the arrays to ints and the values that we are looking at.

#!/usr/bin/python

def cont_format(cont_list, cont_rows, cont_columns):
	cont_format_list = [[0] * cont_columns for count in range(cont_rows)] 
	# Age of the participant
	for i in range(1, cont_rows + 1):
		cont_format_list[i - 1][0] = int(cont_list[i][2])
	# Gender of the participant
	for j in range(1, cont_rows + 1):
		cont_format_list[j - 1][1] = int(cont_list[j][3])
	# Rest of the data
	for k in range(1, cont_rows + 1):
		for l in range(2, 10):
			cont_format_list[k - 1][l] = int(cont_list[k][l + 3])

	print cont_format_list

	return cont_format_list
		
