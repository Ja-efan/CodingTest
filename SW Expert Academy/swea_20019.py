# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AY2hjCWKbykDFATh&categoryId=AY2hjCWKbykDFATh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1
# 회문의 회문
# D3

def solution_20019_2():
    """
    문제에 주어진 조건만 만족하면 된다.
    정말 회문의 회문 인지만 체크 하자!!
    """
    t = int(input())  # 사용자 입력
    for tc in range(1, t+1):
        s = input()  # 사용자 입력 문자열
        len_ = len(s)  # 문자열의 길이
        if s == s[::-1]:  # 문자열이 회문인 경우
            left = s[:(len_//2)]  # 문자열의 처음 (N-1)/2 글자
            right = s[(len_//2)+1:]  # 문자열의 마지막 (N-1)/2 글자
            if left == left[::-1] and right == right[::-1]:
                print(f"#{tc} YES")  # 둘다 회문인 경우 YES 출력
            else :
                print(f"#{tc} NO")  # 하나라도 회문이 아닌 경우 NO 출력
        else :
            print(f"#{tc} NO")  # 문자열 s가 회문이 아닌 경우 NO 출력


solution_20019_2()