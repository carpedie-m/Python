### allow negative interger number
import re

#input_str = input('input #s :')
#list_str = re.findall("-?\d+", input_str)
input_str = "12 3123 1d 23d2 3dwe d21 es2 -3 -4- -400 -3 1093 30 -231"
list_str = input_str.split()

num_list = list()
for ele in list_str:
    if ele.isdecimal():
        num_list.append(int(ele))
    else:   # non-decimal
        neg = re.findall(r'^-?\d+$', ele)
        if neg: # negative
            num_list.append(int(neg[0]))

print(list_str)
print(num_list)
hap = 0
for num in num_list:
    hap = hap + num

print(f' sum = {hap}')

print(sum(num_list))
