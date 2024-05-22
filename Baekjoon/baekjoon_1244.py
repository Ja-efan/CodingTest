# https://www.acmicpc.net/problem/1244
# 스위치 켜고 끄기
# Silver IV

import sys

input = sys.stdin.readline
# print = sys.stdout.write

def solution():
    n = int(input().rstrip())  # 스위치 개수
    switches = list(map(int, input().rstrip().split())) # 스위치의 상태 (list)
    students = int(input().rstrip())

    for s in range(students):
        gender, num = map(int, input().rstrip().split())   

        if gender == 1:  # 남학생
            for i in range(n):
                if (i+1) % num == 0 :  # 받은 수의 배수인 경우 
                    switches[i] = switches[i]^1
        else : # gender == 2 여학생
            j = 0 
            while True:
                j += 1
                if (num-1-j < 0) or (num-1+j)==n:
                    j -= 1
                    break
                elif switches[num-1-j] != switches[num-1+j]:
                    j -= 1
                    break

            for k in range(num-1-j, num-1+j+1):
                """
                num = 3 j = 2 -> range(0, 5)
                """
                switches[k] = switches[k]^1

    # 출력 구문 
    for i in range(1, n+1):
        print(switches[i-1], end=' ')
        if i % 20 == 0:
            print()


solution()
            
            

                