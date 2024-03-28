# 12949 
# https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2) -> list:
    """
    행렬의 곱셈 :
    두 개의 2차원 행렬을 입력받아, 두 행렬의 곱을 반환하는 함수

    Args : 
    - arr1 : 2 dimensional matrix
    - arr2 : 2 dimensional matrix

    Returns : 
    - 2 dimensional matrix 
    """

    # # solution 1 
    # # using Numpy
    # import numpy as np

    # answer = np.dot(arr1, arr2)
    # answer = answer.tolist()

    # return answer


    # solution 2 
    # without Numpy

    row_1 = len(arr1)
    col_1 = len(arr1[0])

    answer = []
    for i in range(len(arr1)):
        
        col = []
        for j in range(len(arr2[0])):
            mul = 0
            for k in range(len(arr1[0])):
                mul += arr1[i][k] * arr2[k][j]
            col.append(mul)
        answer.append(col)
            
            
    return answer





# test case
case1_1 = [[1, 4], [3, 2], [4, 1]]
case1_2 = [[3, 3], [3, 3]]
case2_1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
case2_2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]


print(solution(case1_1, case1_2))
# print(solution(case2_1, case2_2))


