#
# initialization
#
print("\nStep 1. Initialization...")
num_list = list()
sum:int = 0
num:int = 10

for _ in range(num):
	num_list.append(0)
print(f' num_list = {num_list}')
print(f' {sum = }, {num = }')

#
# processing input values
#
print("\nStep 2. Input values...")
for idx in range(len(num_list)):
	if idx == 0:
		pfx = "st"
	elif idx == 1:
		pfx = "nd"
	elif idx == 2:
		pfx = "rd"
	else:
		pfx = "th"
	input_string = f' type {idx+1}{pfx} integer : '

	while True:
		input_text = input(input_string)
		input_data = " ".join(input_text.split())
		if input_data.isdecimal() == False:
			print(f' ... {input_data} is not integer, try again ....')
			continue
		else:
			break

	num_list[idx] = int(input_data)

print(f'\n num_list = {num_list}')

#
# summation = for-statement
#
print("\nStep 3. Calculating ...")
'''
# for-statement 
sum = 0
print("\n # using for-statement")
for idx in range(len(num_list)):
	sum += num_list[idx]
print(f' Result : {sum = }\n')
'''

# while-statement #1
print("\n # using while-statement 1")
'''
idx, sum  = 0, 0
while 
	sum += num_list[idx]

print(f' Result : {sum = }\n')
'''


## while-statement #2
print("\n # using while-statement 2")

idx, sum  = 0, 0
while True:
		if idx < len(num_list):
				sum += num_list[idx]
		else:
				break
		idx = idx + 1
print(f' Result : {sum = }\n')


##  while-statement #3
print("\n # using while-statement 3")
'''
idx, sum  = 0, 0
while True:

	idx = idx + 1
	if 
		break
print(f' Result : {sum = }\n')
'''
