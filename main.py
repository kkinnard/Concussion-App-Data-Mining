# Find correlation within CSV file data.

#!/usr/bin/python

# Functions to edit the CSV files
from csv_format import *
from csv_analyze import *

# Import the CSV Files 'Concussion.csv' and 'Control.csv' in the CSV folder.
# Conc_list will be the list of the demographics for the concussed
# Cont_list will be the list of the demographics for the control

import csv
import sys
import os

with open('Concussion.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:

with open('Control.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:


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


