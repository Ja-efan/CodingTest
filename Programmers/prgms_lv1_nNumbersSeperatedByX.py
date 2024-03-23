# 12954

def solution(x,n) -> list:

    """
    x만큼 간격이 있는 n개의 숫자

    Args :
    - x : -10,000,000 이상 10,000,000 이하인 정수 
    - n : 1000이하의 정수 

    Returns : x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트 
    """

    answer = []
    for i in range(1,n+1):
        answer.append(i*x)

    return answer

# test case
print(solution(2,5))
print(solution(4,3))
print(solution(-4,2))