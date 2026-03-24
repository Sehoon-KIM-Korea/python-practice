# 백준 문제풀이     BAEKJOON Problem Solving

#1000 A + B
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오. (0 < A, B < 10)
# Write a program that takes two integers A and B as input and outputs A+B.

import sys
A, B = map(int, sys.stdin.readline().split())
if 0 < A and B < 10 :
    print(A+B)
else :
    pass


# 백준 문제풀이     BAEKJOON Problem Solving

#1001 A - B
# 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오. (0 < A, B < 10)
# Write a program that takes two integers A and B as input and outputs A-B.

import sys
A, B = map(int, sys.stdin.readline().split())
if 0 < A and B < 10 :
    print(A-B)
else :
    pass


# 백준 문제풀이     BAEKJOON Problem Solving
# 두 수 비교하기     
#1330 두 수 비교하기 Comparing two numbers

#1330 두 수 비교하기
#두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
# s.t. time : 1sec, memory : 512MB

import sys
A, B = map(int, sys.stdin.readline().split())
if -10000 <= A <= 10000 and -10000 <= B <= 10000 :
    pass
    if A > B :
        a = ">"
    elif A < B :
        a = "<"
    else :
        a = "=="

else :
    a = ""

print(a)



# 백준 문제풀이     BAEKJOON Problem Solving
#9498 시험 성적     exam grade     
# 시험 점수를 입력받아 
# 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 
# 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
# s.t. time : 1sec, memory : 128MB

n = int(input())
n
if 90 <= n <= 100 :
    a = "A"
elif 80 <= n <= 89 : 
    a = "B"
elif 70 <= n <= 79 :
    a = "C"
elif 60 <= n <= 69 :
    a = "D"
else :
    a = "F"

print(a)



# 백준 문제풀이     BAEKJOON Problem Solving
#14681 사분면 고르기     choose quadrant

#흔한 수학 문제 중 하나는 주어진 점이 어느 사분면에 속하는지 알아내는 것이다. 
#사분면은 아래 그림처럼 1부터 4까지 번호를 갖는다. "Quadrant n"은 "제n사분면"이라는 뜻이다.
#예를 들어, 좌표가 (12, 5)인 점 A는 x좌표와 y좌표가 모두 양수이므로 제1사분면에 속한다.
# 점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면에 속한다.점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오.
# 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.

# s.t. time : 1sec, memory : 512MB

A = int(input())
B = int(input())

A
B

if A > 0 and B > 0 :
    a = 1
elif A > 0 and B < 0 :
    a = 4
elif A < 0 and B > 0 :
    a = 2
else :
    a = 3
print(a)



# 백준 문제풀이     BAEKJOON Problem Solving
#2468 윤년     leap year

#연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
# 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 
# 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 하지만, 2000년은 400의 배수이기 때문에 윤년이다.
# s.t. time : 1sec, memory : 128MB

n = int(input())
n

if n%4 == 0 and n%100 != 0:
    a = 1
elif n%400 == 0 :
    a = 1
else : 
    a = 0

print(a)
