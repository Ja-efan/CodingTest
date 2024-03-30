# 18177
# https://school.programmers.co.kr/learn/courses/30/lessons/181877

def solution(myString:str) -> str:

    """
    대문자로 바꾸기 : 
    주어진 문자열 myString을 대문자로 변환한 뒤 반환하는 함수

    Args :
    - myString : 1개 이상 100,000개 이하의 알파벳으로 이루어진 문자열
    
    Returns : myString의 모든 알파벳을 대문자로 변환한 문자열
    """
    return myString.upper()

# test case
print(solution('aBcDeFg'))
print(solution('AAAA'))