# ch.2 : 계산기, 터틀 프로그램
# code02-01

# a = 100
# b = 50

# result = a + b
# print(a, "+", b, "=", result)
# result = a - b
# print(a, "-", b, "=", result)
# result = a * b
# print(a, "*", b, "=", result)
# result = a / b
# print(a, "/", b, "=", result)

# code02-02, 03, 04 : 계산기

# a = int(input("첫 번째 숫자를 입력하세요 : "))                     # input()은 문자열 취급 -> int() 이용해 정수로 변환
# b = int(input("두 번째 숫자를 입력하세요 : "))
#
# result = a + b
# print(a, "+", b, "=", result)
# result = a - b
# print(a, "-", b, "=", result)
# result = a * b
# print(a, "*", b, "=", result)
# result = a / b
# print(a, "/", b, "=", result)

# code02-05
#
# import turtle
#
# turtle.shape("turtle")
#
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(200)
# turtle.done()

# code02-06

import turtle

## 함수 선언 부분 ##

## 변수 선언 부분 ##
myT = None

## 메인 코드 부분 ##
myT = turtle.Turtle()
myT.shape('turtle')

for i in range(0,4) :
    myT.forward(200)
    myT.right(90)

turtle.done()

# code02-07

# code03-01



