# 42587
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities:list, location:int) -> int:
    """
    프로세스 :
    현재 실행 대기 큐에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities와,
    몇 번째로 실행되는지 알고싶은 프로세스의 위치를 알려주는 location이 매개변수로 주어질 때,
    해당 프로세스가 몇 번째로 실행되는지 반환.

    Args :
    - priorities : 현재 실행 대키 큐에 있는 프로세스의 중요도가 순서대로 담긴 배열
        1 <= len(priorities) <= 100
        for all i which 0<= i <= 99, 1 <= priorities[i] <= 9
        각 원소는 우선순위를 나타내며 숫자가 클 수록 우선순위가 높다.

    - location : 몇 번째로 실행되는지 알고싶은 프로세스의 위치 (정수)
        0 <= location <= len(priorities)-1
    """
    # # SOLUTION 1 : 40.0 / 100.0
    # execute_queue = []
    # idx = 0
    # lenn = len(priorities)
    # while priorities:
    #     if idx == lenn:
    #         idx = 0
    #     current_max = max(priorities)
    #     print("현 시점 0순위 : ", current_max)
    #     p = priorities.pop(0)
    #     if p >= current_max:
    #         execute_queue.append(idx%lenn)
            
    #     else : 
    #         priorities.append(p)
    #     idx += 1
    
    # print(execute_queue)    

    # for i in range(len(execute_queue)):
    #     if execute_queue[i] == location :
    #         return i+1


    # SOLUTION 2 
    execute_queue = []
    process_tuples = []
    for i, p in enumerate(priorities):
        process_tuples.append((i,p))

    while process_tuples:
        current_max = max(priorities)
        (i,v) = process_tuples.pop(0)
        if v >= current_max:
            execute_queue.append(i)
            priorities[i] = 0
        else :
            process_tuples.append((i,v))

 

    return execute_queue.index(location) + 1

# test case 
print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
print(solution([2, 1, 2, 1, 2, 1, 2, 1, 2], 1)) # 6
print(solution([1,2,8,3,4],2)) # 1