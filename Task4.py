"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

texts_receivers = [ n[1] for n in texts ]
texts_senders = [ n[0] for n in texts ]
calls_receivers = [ n[1] for n in calls ]

list_of_numbers = set()
for call in calls:
    caller = call[0]
    if caller in calls_receivers or caller in texts_senders or caller in texts_receivers:
        continue
    list_of_numbers.add(caller)

# sort
sorted_list = sorted(list_of_numbers)

print('These numbers coule be telemarketers: ')
for n in sorted_list:
    print(n)
