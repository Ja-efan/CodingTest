# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AY2hjCWKbykDFATh&categoryId=AY2hjCWKbykDFATh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1
# 회문의 회문
# D3

# def is_palindrome(s) -> bool:
#     '''
#     길이가 홀수 N인 문자열 S가 회문이라는 것은 다음을 의미한다.
#     - S는 회문이다.
#     - S의 처음 (N-1)/2글자가 회문이다.
#     - S의 마지막 (N-1)/2글자가 회문이다.
#     '''
#     # cond 1 : S는 회문이다.
#     n = len(s)
#     if n == 1:
#         return True
    
#     if s == s[::-1]:
#         if is_palindrome(s[:(n-1)//2]) and is_palindrome(s[-(n-1)//2:]):
#             return True
#         else :
#             return False
#     else :
#         return False
    
def is_palindrome(s) -> bool:
    n = len(s)
    if n == 1:
        return True
    elif n == 2 :
        if s[0] == s[1]:
            return True
        else : 
            return False
        
    elif s == s[::-1]:
        if is_palindrome(s[:(n-1)//2]) and is_palindrome(s[-(n-1)//2:]):
            return True
        else :
            False
    else :
        return False
    
def solution_20019(): 

    t = int(input())        
    for tc in range(1, t+1):
        s = input()
        result = is_palindrome(s)
        if result :
            print(f"#{tc} YES")
        else :
            print(f"#{tc} NO")

solution_20019()