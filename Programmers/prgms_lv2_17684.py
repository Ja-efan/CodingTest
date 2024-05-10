# https://school.programmers.co.kr/learn/courses/30/lessons/17684
# [3차] 압축

from string import ascii_uppercase
from collections import deque

def solution(msg:str) -> list :

    uppercase = list(ascii_uppercase)

    # 길이가 1인 모든 단어(대문자 알파벳)을 포함하는 사전 초기화
    # 사전 구성 -> key : value = WORD : index 
    upper_dict = { 
        uppercase[i]: i+1 for i in range(len(uppercase))
    }
    msg_deque = deque(msg)
    result = []
    # print(msg_deque)

    i = 0
    while msg_deque:
        w = msg[i]
        next = i+1
        if msg[i:] in upper_dict:
            result.append(upper_dict[msg[i:]])
            break
        while msg[i:next] in upper_dict.keys():
            w = msg[i:next]
            next +=1
        # w에 해당하는 사전의 색인 번호를 저장
        result.append(upper_dict[w])
        # msg = msg[next-1: ]
        [msg_deque.popleft() for _ in range(next-1-i)]
        # 입력에서 처리되지 않은 글자가 남아있다면 사전에 추가 
        upper_dict[msg[i:next]] = len(upper_dict) + 1
        i = next-1
            
    return result



# test case 
# print(solution('KAKAO')) # [11, 1, 27, 15]
print(solution('TOBEORNOTTOBEORTOBEORNOT')) # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
print(solution('ABABABABABABABAB')) # [1, 2, 27, 29, 28, 31, 30]