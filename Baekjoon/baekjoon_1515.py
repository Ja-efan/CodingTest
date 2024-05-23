# https://www.acmicpc.net/problem/1515
# 수 이어 쓰기
# Silver III


import sys
from collections import deque
input = sys.stdin.readline
output = sys.stdout.write  

def solution():
    num = input().rstrip()
    num_dq = deque(num)


    test_n = 0
    
    while num_dq:
        test_n += 1
        test_n_str = str(test_n)
        # pop_cnt = 0
        for i in range(len(test_n_str)):
            if not num_dq:
                break
            if test_n_str[i] == num_dq[0]:
                num_dq.popleft()
        
    print(test_n)
    
solution()



    
            
