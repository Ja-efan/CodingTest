# 12973

def solution(s:str) -> int:
    """
    Remove Pairs :
    짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다. 
    먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 
    그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다. 
    이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다. 
    문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요. 
    성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.

    Args : 
    - s : 알파벳 소문자로 구성된 문자열 (길이 최대 1,000,000)

    Return :
    - int : 0 or 1 
    """

    # 스택 사용 !!!!
    
    stack = []

    for c in s :
        if stack and stack[-1] == c:
            stack.pop()
            continue
        stack.append(c)

    return int(not stack)


        
            

  
# test case 
print(solution('baabaa'))
print(solution('cdcd'))
print(solution('aaabbabbababab'))