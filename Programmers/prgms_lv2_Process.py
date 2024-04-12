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


    # print(priorities)
    # print(priorities.pop(0)) # pop index 0
    # print(priorities)

    """
    IDEA 1 :
    1. 실행 대기 큐(Priorities)에서 idx 0을 pop
    2. 나머지 실행 대기 큐의 원소와 값 비교 
        2.1 pop원소보다 더 큰 값이 있다면 해당 원소를 큐에 append
        2.2 pop원소가 가장 큰 값이라면 1부터 반복
    """
    # print(priorities)
    location_list = [i for i in range(len(priorities))]
    # print(location_list)
    for i in range(len(priorities)):
        e = priorities[0]
        idx = location_list[0]

        for j in range(0, len(priorities)):
            if e < priorities[j]:
                priorities.append(priorities.pop(0))
                location_list.append(location_list.pop(0))
                break
            else:
                continue

    # print(priorities)
    # print(location_list)
   
    for i in range(len(location_list)):
        if location_list[i] == location:
            return i+1
        
    """ 
    IDEA 2 : using dictionary
    1. priorities를 dict로 변환 -> key = index : value = element
    2. dict를 Value, key 순서로 정렬 (둘다 내림차순)
    3. location에 해당하는 value를 가져옴 (location이 priorities에서의 index이므로 dict의 key가 됨)
    

    queue_dict = dict()
    for i, v in enumerate(priorities):
        queue_dict[i] = v

    queue_dict = dict(sorted(queue_dict.items(), key=lambda x : (x[1], x[0]), reverse=True))

    print(queue_dict)

    for i, (k, v) in enumerate(queue_dict.items()):
        if k == location:
            return i+1
    """


# test case 
# print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
