def count():
    yield ""

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    i = 0

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
# store phone numbers as keys in dictionary
# to get rid of duplicates
phone_numbers = {}

for text in texts: 
    phone_numbers[text[0]] = ''
    phone_numbers[text[1]] = ''

for call in calls:
    phone_numbers[call[0]] = ''
    phone_numbers[call[1]] = ''

print(f'There are {len(phone_numbers)} different telephone numbers in the records.')

