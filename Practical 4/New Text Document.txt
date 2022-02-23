# Name: NISHANT KOTADIA
# ID: 20CS029

import sys


N = int(input())           # Total number of run entered by user

runs = [int(i) for i in input().split(' ')]    # Create array

# Checking if the runs entered by the user is equal to the total number of runs.
if len(runs) != N:
    sys.exit()

sorted_runs = list(set(sorted(runs)))             # storing the runs

print(sorted_runs[-2])       # print runners up score
