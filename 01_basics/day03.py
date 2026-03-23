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
if -10000 <= A and B <= 10000 :
    if A > B :
        a = ">"
    elif A < B :
        a = "<"
    else :
        a = "=="

else :
    pass

print(a)