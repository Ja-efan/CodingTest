# 181910
# https://school.programmers.co.kr/learn/courses/30/lessons/181910

def solution(myString:str, n:int) -> str:
    """
    문자열의 뒤의 n글자 : 
    주어진 문자열의 뒤의 n글자로 이루어진 문자열을 반환

    Args : 
    - myString : 숫자와 알파벳으로 이루어진 문자열
    - n : 1이상 myString의 길이 이하의 정수

    Returns : 길이가 n인 문자열
    """ 

    return myString[-n:]

# test case 
print(solution("ProgrammerS123", 11))
print(solution("He110W0r1d", 5))