# 70129

def solution(s:str)-> list :
    """
    RepeatBinaryConversion :
    
    '이진 변환'
    1. x의 모든 0을 제거
    2. x의 길이를 c라고 하면, x를 "c를 이진으로 표현한 문자열"로 바꾼다. 


    Args :
    - s : 0과 1로 이루어진 문자열

    Returns : s가 '1'이 될 때까지 계속해서 s에 이진 변환을 가했을 때, 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 리스트에 담아 반환 
    
    """

    answer = [0,0] # answer[0] : 이진 변환 횟수, answer[1] : 제거된 모든 0의 개수. 
    while s != '1':
        len_old = len(s)
        s_new = s.replace('0', '') # 0 제거
        # print(s_new)
        len_new = len(s_new)
        answer[1] += (len_old - len_new) # 제거된 0의 개수 추가 
        
        s = str(format(len_new, 'b'))
        answer[0] += 1

    return answer


# test case
print(solution("110010101001"))

print(solution("01110"))

print(solution("1111111"))
