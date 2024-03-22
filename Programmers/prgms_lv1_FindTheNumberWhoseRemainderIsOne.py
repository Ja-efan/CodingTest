# 87389

def solution(n:int) -> int:
    """
    나머지가 1이 되는 수 찾기 

    Args : 
    - n : 자연수 

    Returns : n을 x로 나눈 나머지가 1이 되도록 하는 가장 자연수 
    """
    for i in range(1,n):
        if n % i == 1:
            return i
        

# test case 
print(solution(10))
print(solution(12))