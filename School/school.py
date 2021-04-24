# 2주차 과제 사칙연산 결과 출력 (응급구조과 1학년 2021240067 최승희)

# a = int(input("첫번째 숫자 입력 : "))
# b = int(input("두번째 숫자 입력 : "))

# print(a, "+", b, "=", a+b)
# print(a, "-", b, "=", a-b)
# print(a, "*", b, "=", a*b)
# print(a, "/", b, "=", a/b)

# -----------------------------------------------------------

# print("hello...!")
# print('hello...?')
#
# my_string = "hello, ..!!"
# print(my_string)
#
# a = 100
# b = 20
# c = 'hello'
#
# print(a, b, c)
#
# print("100") # 문자
# print(100) # 숫자
# print('%d' % 100)    # d : decimal 십진수(정수)로 표현
# print('%f' % 100)    # f : float 실수
# print('100 + 100')    # 100+100 -> 문자
# print('%d' % (100 + 100))   # (100 + 100)  괄호를 십진수로 표현
# # print('%d' % (100, 200)) - 에러
#
# print('%d %d' % (100, 200))
# print('%d / %d = %d' % (100, 200, 0.5))     # 0.5가 정수0으로 표현됨 # 파이썬은 자신이 알아서 타입을 정함
# print('%d / %d = %f' % (100, 200, 0.5))     # %d, %f 이 형태대로 출력하갰다!
#
# print(a,"/", b, "=", a/b)
#
# print('%d %x %o' % (10, 10, 10)) # 나중에 설명
# print('%d' % (123))
# print('%05d' % (123)) #5개 칸 만들고 빈칸은 0으로
#
# print('%010d' % (123))
# print('%7.1f' % (3.141545)) # 7개 칸 만들고 소수점 1자리 까지
# print('%7.5f' % (3.141545)) # 7개 칸 만들고 소수점 5자리 까지
# print('%s' % 'Python') # %s : string 문자열 인식
# print('%10s' % 'Python') # 10개 칸 만들고 오른쪽으로 정렬(앞에 띄우고)
#
# print("{0:d} {1:5d} {0:05d}".format(123, 200, 300))
#
# print('hi!...\never\n')
#
#
# a = 2
# print(type(a))
#
# a_bin = bin(12)
# print(a_bin)
# a_oct = oct(a)
# print(a_oct)
# a_hex = hex(a)
# print(a_hex)
#
# # input_num = input('input num : ')
# # num = int(input_num)
# # print('%d, 0o%o, 0x%x' % (num, num, num))
# #
# # num_2 = int(input_num, 2)
# # num_10 = int(input_num, 10)
# # num_16 = int(input_num, 16)
# # 88
# # in_num = '55'
# # num = int(input_num)
# # print(num)
#
#
# a = True
# type(a)
# print(type(a))
#
# a = 100 > 10
# b = 50

# 기본타입 int / float / str / bool 변수는 타입에 따라 달라짐

# 연산자(operator) 사칙연산 : + - * / % ==


# a,b=5,3
# print(a)
# a,b,c=2,3,4
# print(a,b,c)
#
# float('12')
# print(float(12))
# str('안녕')
# s1 = str('안녕')
# print(s1)
#
# f1 = 123.45
# s1 = str(f1)
# print(s1)
# type(s1)
# print(type(s1))
#
# int = 1234
# s1 = 123
# print(int, s1 )

# print('------------5주차 과제------------')
# ## 변수 선언 부분 ##
# money, c500, c100, c50, c10 = 0, 0, 0, 0, 0

# ## 메인 코드 부분 ##
# money = int(input("교환할 돈은 얼마?"))
#
# c500 = money // 500
# money %= 500
#
# c100 = money // 100
# money %= 100
#
# c50 = money // 50
# money %= 50
#
# c10 = money // 10
# money %= 10
#
# print("\n 500원짜리 => %d개" % c500)
# print(" 100원짜리 => %d개" % c100)
# print(" 50원짜리 => %d개" % c50)
# print(" 10원짜리 => %d개" % c10)
# print(" 바꾸지 못한 잔돈 => %d개 \n" % money)

# s1, s2, s3 = "111", "111.11", "9999"
# print(int(s1) + 111.11)
# print(float(s2) + 111.11)
# print(int(s3) + 111.11)
#
# a = 100; a = a<<100; a = a>>100; print(a)


# 4장 연습문제 9번 #

# money, c50000, c10000, c5000, c1000, c500, c100, c50, c10 = 0,0,0,0,0,0,0,0,0
#
# money = int(input("교환할 돈은 얼마?"))
# c50000 = money // 50000
# money %= 50000
# c10000 = money // 10000
# money %= 10000
# c5000 = money // 5000
# money %= 5000
# c1000 = money // 1000
# money %= 1000
# c500 = money // 500
# money %= 500
# c100 = money // 100
# money %= 100
# c50 = money // 50
# money %= 50
# c10 = money // 10
# money %= 10
#
# print("\n 50000원 => %d개" % c50000)
# print(" 10000원 => %d개" % c10000)
# print(" 5000원 => %d개" % c5000)
# print(" 1000원 => %d개" % c1000)
# print(" 500원 => %d개" % c500)
# print(" 100원 => %d개" % c100)
# print(" 50원 => %d개" % c50)
# print(" 10원 => %d개" % c10)
# print(" 바꾸지 못한 잔 => %d원" % money)




# a = 2
# if a < 100:
#     print("a is less than 100")
#     print("참이면 이 문장도 보이겠죠?")
# else:
#     print("입력 숫자가 100보다 작습니다.")



#if_else문#
# in_str = input("숫자입력하셈")
#
# in_num = int(in_str)
#
# if in_num < 100:
#     print(f'{in_num} is less than 100')
# else:
#     print(f'{in_num} is greater than 100')


#입력 숫자 짝수 홀수 판별#

# in_str = input("숫자 적어봐 : ")
#
# in_num = int(in_str)
#
# if (in_num % 2) == 0:               #3 % 2 => 1 == 0 => False
#     print(f'{in_num} is even')
# else:
#     print(f'{in_num} is odd')
#
# if (in_num % 2) == 0:               #3 % 2 => 1 (not 0) => True
#     print(f'{in_num} is odd')
# else:
#     print(f'{in_num} is even')
#
# if not (in_num % 2):                #3 % 2 => 1, not(1) = False
#     print(f'{in_num} is even')
# else:
#     print(f'{in_num} is odd')



#if~else~if~else 문 : 중첩 if문
# a = 99
# if a < 100:
#     if a > 50:
#         print(f'{a} is less than 100 vut greater than 50')
#     else:
#         print("50보다 작네")
# else:
#     print("100보다 작네")

#if elif else 문
#
# score = int(input("점수를 입력하세요. : "))
#
# if score >= 90 :
#     print("A")
# elif score >= 80 :
#     print("B")
# elif score >= 70 :
#     print("C")
# elif score >= 60 :
#     print("D")
# else:
#     print("F")
#
# print("네 학점이란다.^^")

#
# score = 55
#
# if score >=60:
#     print("합격")
# elif score >=40 :
#     print("불합격인데 과락아님")
# else:
#     print("불합격 과락")
#
# # 5장 연습문제 7번 - 주사위 여러 개 동시에 던지기
# import random
#
# # 전역 변수 선언 부분
# dice1, dice2, dice3 = [0] * 3
#

# 메인 코드 부분
# if __name__=="__main__":
#     while True :
#
#         dice1 = random.randrange(1,7)
#         dice2 = random.randrange(1,7)
#
#         print("A의 주사위 숫자는 %d입니다." % dice1)
#         print("B의 주사위 숫자는 %d입니다." % dice2)
#
#
#         if dice1 == dice2:
#             print('비겼습니다.')
#
#         elif dice1 > dice2 :
#             print("a가 이겼습니다.")
#
#         else:
#             print("b가 이겼습니다.")
#
#         break


# 구구단

#
# num = int(input("input number (2 - 9) : "))
#
# for i in range(1,94):
#     print(f'{num} * {i} = {num * i}')

# 중첨 For 문

# count = 0
#
# for a in range(0, 4):
#     for b in range(0, 3):
#         count = count + 1
#         print(f'a = {a}, b = {b}, count = {count}')
#     print("***")
#

# 구구단 출력
# for dan in range(2, 10):
#     print(f'단 = {dan}')
#     for i in range(1, 10):
#         print(f'{dan} * {i} = {dan * i} ')
#     print("***************")

# code06-13.py
# 8주에 할것

# 6장 5번 문제
num = int(input("단을 입력하세요 : "))

for i in range(9, 0, -1):
    print(f'{num} * {i} = {num * i}')

