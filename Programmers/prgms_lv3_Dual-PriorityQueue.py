# https://school.programmers.co.kr/learn/courses/30/lessons/42628
# 42628

def solution(operations: list) -> list :
    """
    이중우선순위큐 :
    이중 우선순위 큐가 할 연산 operations가 주어질 때, 모든 연산을 처리한 후 큐가 비어있으면 [0,0]
    비어있지 않으면 [최댓값, 최솟값]을 반환하는 함수 

    Args : 
    - operations : 1 이상 1,000,000 이하의 길이를 갖는 문자열 배열(list)
        각 원소는 큐가 수행할 연산을 나타냄
        원소는 "명령어 데이터" 형식으로 주어지며, -최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제 
        빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시 

    Returns : 
    """

    qu = []
    while operations:
        oprt = operations.pop(0)
        cmd, data = oprt.split(" ")
        if cmd == "I":
            qu.append(int(data))
        else : # cmd == "D"
            if not qu:
                continue
            elif data == "1":
                qu.pop(qu.index(max(qu)))
            else :
                qu.pop(qu.index(min(qu)))

    if qu :
        return [max(qu), min(qu)]
    else :
        return [0,0]


# test case 
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])) # [0,0]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])) # [333,-45]
        