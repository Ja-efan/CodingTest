# 181896
# https://school.programmers.co.kr/learn/courses/30/lessons/181896
# 첫 번째로 나오는 음수 

def solution(num_list):
    """
    첫 번째로 나오는 음수 :
    정수 리스트 num_list에 대해서, 첫 번째로 나오는 음수의 인덱스를 Return.
    음수가 없다면 -1을 Return.
    """
    answer = 0
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1


# test case 
print(solution([12, 4, 15, 46, 38, -2, 15])) # 5
print(solution([13, 22, 53, 24, 15, 6])) # -1