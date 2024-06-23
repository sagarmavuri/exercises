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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
first_record_text = texts[0]
last_record_calls = calls[len(calls) - 1]

print(f'{first_record_text[0]} texts {first_record_text[1]} at time {first_record_text[2]}')
print(f'{last_record_calls[0]} calls {last_record_calls[1]} at time {last_record_calls[2]}, lasting {last_record_calls[3]} seconds')

