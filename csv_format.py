# Format the CSV data for ease in analysis.

#!/usr/bin/python

# Edits the input CSV file, putting the age into an age range, where less than 
# 16 is range 1, 17 to 19 is range 2, and greater than 20 is range 30.

def age_format(list, num_rows):
	for i in range(0, num_rows):
		if list[i][0] <= 16:
			list[i][0] = 1
		elif list[i][0] >= 17 and list[i][0] <= 19:
			list [i][0] = 2
		elif list[i][0] >= 20:
			list[i][0] = 3

# Edits the CSV file, putting the days into a range, with less than 5 being 1, 
# 6 to 10 being 2, 11 to 15 being 3, 16 to 20 being 4, and greater than 20 being
# 5
# Only needed for symptom data mining.

def days_format(list, num_rows):
	for i in range(0, num_rows):
		if list[i][1] <= 5:
			list[i][1] = 1
		elif list[i][1] <= 10 and list[i][1] >= 5:
			list[i][1] = 2
		elif list[i][1] <= 15 and list[i][1] >= 10:
			list[i][1] = 3
		elif list[i][1] <= 20 and list[i][1] >= 15:
			list[i][1] = 4
		elif list[i][1] > 20:
			list[i][1] = 5
