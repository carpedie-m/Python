# import re
#
# input_str = input('input #s :')
# number_str = re.findall("-?\d+", input_str)
#
# Debugging: bool = True
# if Debugging:
#     print(f'input_str = {input_str}')
#     print(f'number_str = {number_str}, count = {len(number_str)}')
#
# #for문
# num_list = list()
# for num in number_str:
#     num_list.append(int(num))
# if Debugging:
#     print(f'num_list = {num_list}')

# a = [11, 12, 13, 14]
# print(len(a))
#
# cnt = 0
# while True:
#     if cnt % 2:
#         break
#     cnt += 1
# print(cnt)

#
# my_list = [ x*x for x in range(4) if not x % 2]
#
# # print( sum(my_list) )
# num = 6
#
# if num % 2:
#
#     check = True
#
# else:
#
#     check = False
#
# if check:
#
#     print(num // 5)
#
# else:
#
#     print(num % 5)


even_sum = 0
num = 1

while num <= 100:
    if num % 2:
        even_sum += num
    num += 1

print(even_sum)

