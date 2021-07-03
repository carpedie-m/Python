### allow negative interger number
import re

input_str = input('input #s :')
number_str = re.findall("-?\d+", input_str)

Debugging: bool = True
if Debugging:
	print(f' input_str = {input_str}')
	print(f' numbers_str = {number_str}, count = {len(number_str)}')

# for-statement
"""
num_list = list()
for num in number_str:
	num_list.append(int(num))
if Debugging:
	print(f' num_list = {num_list}')
"""

# list comprehension
num_list = [int(num_str) for num_str in number_str]
if Debugging:
	print(f' num_list = {num_list}')

print(f' sum : {sum(num_list)}')
print(f' max : {max(num_list)}')
print(f' min : {min(num_list)}')
