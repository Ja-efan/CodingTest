# 181893
# https://school.programmers.co.kr/learn/courses/30/lessons/181893

def solution(arr:list, query:list) -> list :
    """
    배열 조각하기 :
    query를 순회하면서 다음 작업을 반복한다.
    - 짝수 인덱스에서는 arr에서 query[i]번 인덱스를 제외하고 배열의 query[i]번 인덱스 뒷부분을 잘라서 버린다.
    - 홀수 인덱스에서는 arr에서 query[i]번 인덱스를 제외하고 배열의 query[i]번 인덱스 앞부분을 잘라서 버린다.
    위 작업을 마친 후 남은 arr의 부분 배열을 return 

    Args : 
    - arr : 각 원소가 0이상 100이하의 값을 갖는 정수이며, arr의 길이는 5이상 100,000이하 
    - query : 각 원소는 0이상이고 남아있는 arr의 길이보다 작으며, 길이는 1이상 min(50,arr의 길이/2)미만 

    Returns : 위의 작업을 수행한 뒤 남은 arr의 부분 배열
    """

    for i in range(len(query)):
        if i % 2 == 1: # 홀수 인덱스
            arr = arr[query[i]:]
            # print(arr)
        else : # 짝수 인덱스 
            arr = arr[:query[i]+1]
            # print(arr)
    
    return arr


# test case
print(solution([0,1,2,3,4,5], [4,1,2])) 