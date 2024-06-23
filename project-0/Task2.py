"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# keep the total time spent in dictionary.
# this will also avoid having duplicates
durations = {}

# variables to store max seconds.
telephone_number_max_duration = int(calls[0][3])
telephone_number_max = calls[0][0]

for call in calls:

    if call[0] not in durations.keys():
        durations[call[0]] = int(call[3])
    else:
        durations[call[0]] += int(call[3])
    
    if durations[call[0]] > telephone_number_max_duration:
        telephone_number_max_duration = durations[call[0]]
        telephone_number_max = call[0]
    
    if call[1] not in durations.keys():
        durations[call[1]] = int(call[3])
    else:
        durations[call[1]] += int(call[3])
    
    if durations[call[1]] > telephone_number_max_duration:
        telephone_number_max_duration = durations[call[1]]
        telephone_number_max = call[1]

print(f'{telephone_number_max} spent the longest time, {telephone_number_max_duration} seconds, on the phone during September 2016.')

