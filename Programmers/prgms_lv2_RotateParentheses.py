# 76502 

def solution(s:str):
    """
    괄호 회전하기 :
    대괄호, 중괄호, 소괄호로 이루어진 문자열 s가 매개변수로 주어진다. 
    이 s를 왼족으로 x 칸 만큼 회전시켰을 때, s가 올바른 괄호 문자열이 되게 하는 x의 개수를 반환

    Args :
    - s : 대괄호, 중괄호, 소괄호로 이루어진 문자열(str), 길이는 1이상 1,000이하

    Returns : answer(int)
    """

    parenthes_dict = {
        '(' : ')',
        "{" : "}",
        "[" : "]"
    }

    answer = 0
    # s_rotate_list = []
    for i in range(len(s)):
        s_rotate = s[i:] + s[:i]
        # s_rotate_list.append(s_rotate)

        stack = [s_rotate[0]]
        s_rotate = s_rotate[1:]
        
        for p in s_rotate:
            if not stack:
                stack.append(p)
            elif stack[-1] in parenthes_dict:
                if parenthes_dict[stack[-1]] == p:
                    stack.pop()
                else : 
                    stack.append(p)
                    
        
        if not stack :
            answer += 1
             
            
    return answer


print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
