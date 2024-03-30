# 181936 
# https://school.programmers.co.kr/learn/courses/30/lessons/181936

def solution(number:int, n:int, m:int) -> int:
    """
    공배수 :
    number가 n과 m의 공배수 인지 확인

    Args :
    - number
    - n
    - m

    Returns : 공배수라면 1, 아니라면 0 반환
    """
    if number % n == 0 and number % m == 0:
        return 1
    else : return 0


print(solution(60,2,3))
print(solution(55,10,5))