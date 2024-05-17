# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYgEiwbKy48DFARP&categoryId=AYgEiwbKy48DFARP&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1&&&&&&&&&&
# 문자열문자열
# D3

def solution():
    t = int(input())  # 사용자 입력 : 테스트 케이스 개수
    for tc in range(1, t+1):
        n = int(input())  # 사용자 입력 : 문자열 길이 N
        s = input()  # 사용자 입력 : 문자열 S

        if n % 2 == 1:
            print(f"#{tc} No")  # 문자열 S의 길이가 홀수인 경우 불가능한 문자열
        else:
            half = n//2  # N/2
            if s[:half] == s[half:]:  # 앞 N/2 길이의 서브스트링과 뒤 N/2 길이의 서브스트링이 동일한 경우
                print(f"#{tc} Yes")
            else:  # 앞 N/2 길이의 서브스트링과 뒤 N/2 길이의 서브스트링이 서로 다른 경우
                print(f"#{tc} No")


solution()
