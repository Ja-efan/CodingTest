# 181920
# https://school.programmers.co.kr/learn/courses/30/lessons/181920

def solution(start_num, end_num):

    """
    # solution 1
    answer = []
    for i in range(start_num, end_num+1):
        answer.append(i)
    return answer
    """

    # solution 2 : list comprehension
    return [i for i in range(start_num, end_num+1)]