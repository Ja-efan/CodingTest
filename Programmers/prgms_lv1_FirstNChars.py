# 181907
# https://school.programmers.co.kr/learn/courses/30/lessons/181907

def solution(myString, n):
    """
    문자열의 앞의 n글자 : 
    문자열 myString의 앞에 n글자로 이루어진 문자열을 반환하는 함수 

    Args : 
    - myString : 1개 이상 1,000개 이하의 숫자와 알파벳으로 이루어진 문자열,
    - n : 정수

    Returns : myString의 앞 n글자로 이루어진 문자열

    """
    return myString[:n]

# test case 
print(solution("ProgrammersS123", 11))
print(solution("He1lOWOrld", 5))