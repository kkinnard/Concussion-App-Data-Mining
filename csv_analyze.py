# Analyze the arrays.

#!/usr/bin/python

def average_array(list, num_rows, num_columns):
	sum = [0] * num_columns
	average = [0] * num_columns
	# Sum up all the values for that particular category
	for i in range(0, num_columns):
		for j in range(0, num_rows):
			sum[i] = sum[i] + list[j][i]
	# Find the average for each of these categories
  	for k in range(0, num_columns):
		average[i] = sum[i] / num_columns

	return average	

def percent_difference(list1, list2, num_columns):
	difference = [0] * num_columns
	#Find the difference between the control and the concussed
	for i in range(0, num_columns):
		difference[i] = list1[i] - list2[i]
	
	return difference

