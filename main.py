# Find correlation within CSV file data.

#!/usr/bin/python

from __future__ import with_statement 

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

<<<<<<< HEAD
with open('Control.csv', 'rU') as f:
	reader = csv.reader(f)
	conc_list = list(list(rec) for rec in csv.reader(f, delimiter=','))
	
with open('Control.csv', 'rU') as f:
	reader = csv.reader(f)
	cont_list = list(list(rec) for rec in csv.reader(f, delimiter=','))
=======
with open('Concussion.csv', 'rU') as f:
	conc_list = csv.reader(f)
	
with open('Control.csv', 'rU') as f:
	cont_list = csv.reader(f)
>>>>>>> e65c53e69477b6e6222d4ddd56cfcd04f1feb1d2
	

conc_rows = 94 # Start at 0.
conc_columns = 11
cont_rows = 485
cont_columns = 11

# Edit the input for day range and days symptoms lasted.
# The rest of the data is 1's and 0's.
age_format(conc_list, conc_rows)
age_format(cont_list, cont_rows)

days_format(conc_list, conc_rows)
days_format(cont_list, cont_rows)

conc_average = average_array(conc_list, conc_rows, conc_columns)
cont_average = average_array(cont_list, cont_rows, cont_columns)

<<<<<<< HEAD

=======
>>>>>>> e65c53e69477b6e6222d4ddd56cfcd04f1feb1d2
difference = percent_difference(conc_average, cont_average)
#Will return difference, where positive means higher incidence in Concussed thanthe control.

print difference
<<<<<<< HEAD

=======
>>>>>>> e65c53e69477b6e6222d4ddd56cfcd04f1feb1d2
