# 백준 문제풀이     BAEKJOON Problem Solving

#2438 별 찍기

#첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

# s.t. time : 1sec, memory : 128MB

n = int(input())

for i in range(n) :
    print("*"*(i+1))



# 백준 문제풀이     BAEKJOON Problem Solving

#2439 별 찍기 2

#첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
#하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

# s.t. time : 1sec, memory : 128MB

n = int(input())

for i in range(n) :
    print(("*"*(i+1)).rjust(n))





# 백준 문제풀이     BAEKJOON Problem Solving

#10818 최소, 최대

#N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

# s.t. time : 1sec, memory : 256MB

import sys

input = sys.stdin.readline

B = int(input())
C = list(map(int, input().split()))

print(min(C), max(C))




# 백준 문제풀이     BAEKJOON Problem Solving

#2562 최대값

# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 
# 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 예를 들어, 서로 다른 9개의 자연수
# 3, 29, 38, 12, 57, 74, 40, 85, 61
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

# s.t. time : 1sec, memory : 128MB

import sys

B = []

input = sys.stdin.readline

for i in range(9) :
    B.append(int(input()))
    
print(max(B))
print(B.index(max(B)) + 1)




# 백준 문제풀이     BAEKJOON Problem Solving

#2765 문자열 반복

#문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
#즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
#S에는 QR Code "alphanumeric" 문자만 들어있다.QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

# s.t. time : 1sec, memory : 128MB

import sys

T = int(input())

input = sys.stdin.readline

for i in range(T) :
    R, S = input().split()
    R = int(R)

    result = ""

    for j in S :
        result += j*R

    print(result)




# 백준 문제풀이     BAEKJOON Problem Solving

#1152 단어의 개수     the_number_of_word

#영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 
#이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오.
#단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

# s.t. time : 2sec, memory : 128MB

import sys

input = sys.stdin.readline
A = input().split()
A

print(len(A))