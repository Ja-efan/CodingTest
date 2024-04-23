# 43105
# https://school.programmers.co.kr/learn/courses/30/lessons/43105
# Dynamic Programming

def solution(triangle:list) -> int:
    """
    정수 삼각형 :
    삼각형의 정보가 담긴 배열 triangle이 주어질 때, 거쳐간 숫자의 최댓값을 반환하는 함수 

    Args : 
    - triangle : 삼각형의 정보가 담긴 정수 배열(list)
        높이는 1이상 500이하,
        삼각형을 이루는 숫자는 0이상 9,999이하 정수
     
    """
    summ = []
    for i in range(len(triangle)):
        height = []
        if i == 0:
            summ.append(triangle[i])
            continue 
        for j in range(len(triangle[i])):
            if j-1 < 0:
                height.append(summ[i-1][j] + triangle[i][j])
            elif j > len(summ[i-1])-1:
                height.append(summ[i-1][j-1] + triangle[i][j]) 
            else :
                height.append(max(summ[i-1][j], summ[i-1][j-1]) + triangle[i][j])
        summ.append(height)
    # print(summ)
    
    answer = max(summ[-1])
    
    return answer

# test case 
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])) # 30