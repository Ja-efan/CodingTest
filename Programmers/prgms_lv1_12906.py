# https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 같은 숫자는 싫어 

def solution(arr:list) -> list:

    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] == result[-1]:
            continue
        result.append(arr[i])
    return result


# test case
print(solution([1,1,3,3,0,1,1])) # [1,3,0,1]
print(solution([4,4,4,3,3])) # [4,3]