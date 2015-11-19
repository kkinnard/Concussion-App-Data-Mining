# Find correlation within CSV file data.

#!/usr/bin/python

import csv
import sys
import os

# Functions to edit the CSV files
from csv_format import *
from csv_analyze import *

# Import the CSV Files 'Concussion.csv' and 'Control.csv' in the CSV folder.
# Conc_list will be the list of the demographics for the concussed
# Cont_list will be the list of the demographics for the control

#matrices for the data in each CSV file
conc_rows = 94 # Start at 0.
conc_columns = 11
cont_rows = 485
cont_columns = 11

with open('CSV\ Files/Concussion.csv', 'rU') as f:
	conc_list = csv.reader(f)
	
with open('CSV\ Files/Control.csv', 'rU') as f:
	cont_list = csv.reader(f)
	
conc_rows = 94 # Start at 0.
conc_columns = 11
cont_rows = 485
cont_columns = 11

# Edit the input for day range and days symptoms lasted.
# The rest of the data is 1's and 0's.
age_format(Conc_list, conc_rows)
age_format(Cont_list, cont_rows)

days_format(Conc_list, conc_rows)
days_format(Cont_list, cont_rows)

#for row in ****_list:
	#for value in row:
		#print value
