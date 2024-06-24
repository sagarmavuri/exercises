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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
mobile_phone_prefixes = ['7', '8', '9']
list_codes = set() # to remove duplicates.
total_calls_from_to_bangalore = 0
total_calls_from_bangalore = 0

for call in calls:

    # call originated from Bangalore
    if call[0].find('(080)') == 0:
        total_calls_from_bangalore += 1
        if call[1].find('140') == 0:
            list_codes.add('140')
        elif call[1].find('(080)') == 0:
            list_codes.add('(080)')
            total_calls_from_to_bangalore += 1
        elif call[1].find('(') == 0: # rest of the area codes with (*)
            list_codes.add(call[1][:call[1].find(')') + 1])
        elif call[1][0] in mobile_phone_prefixes: # do we need this condition, all can go in 'else'?
            list_codes.add(call[1][:4]) # assuming first 4 digits are what needs to be stored

# sort
sorted_list_codes = sorted(list_codes)

print('The numbers called by people in Bangalore have codes:')
for code in sorted_list_codes:
  print(code)

# Part B
print(
    f'{round((total_calls_from_to_bangalore / total_calls_from_bangalore) * 100, 2)} '
    'percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'
)
