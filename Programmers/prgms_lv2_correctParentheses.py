def solution (s:str)-> bool:
    """
    Args :
    - s : '(' 혹은 ')' 로만 이루어진 문자열

    Returns : 올바른 괄호인지 True or False
    """


    open = 0
    close = 0
    for p in s :
        if p == '(' : open += 1
        elif p == ')' and open == 0: return False
        elif p == ')' and open != 0: open -= 1
    if open == 0 : return True
    else : return False


# test case
print(solution("()()"))
print(solution("(())()"	))
print(solution(")()("))
print(solution("(()("))