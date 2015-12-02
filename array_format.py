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
	
	return cont_format_list
	
def conc_format(conc_list, conc_rows, conc_columns):
	conc_format_list = [[0] * conc_columns for count in range(conc_rows)]
	#Age of the participant 
	for i in range(1, conc_rows + 1):
		conc_format_list[i - 1][0] = int(conc_list[i][2])
	#Gender of the participant
	for j in range(1, conc_rows + 1):
		conc_format_list[j - 1][1] = int(conc_list[j][4])
	#Rest of the data
	for k in range(1, conc_rows + 1):
		for l in range(2, 10):
			conc_format_list[k - 1][l] = int(conc_list[k][l + 3])

	return conc_format_list	
