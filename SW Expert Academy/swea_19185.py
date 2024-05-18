# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYzIZNkq-v4DFAQ9&categoryId=AYzIZNkq-v4DFAQ9&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1&&&&&&&&&&
# 육십갑자
# D3

def solution():
    t = int(input())
    for tc in range(1, t+1):
        N, M = map(int, input().split())
        s_lst = input().split()  # s1, s2, ... , sN
        t_lst = input().split()  # t1, t2, ... , tM
        Q = int(input())  # 1 <= Q <= 2000
        year_lst = []
        for _ in range(Q):
            Y = int(input())
            year_lst.append(Y)

        # 이름에 해당하는 Q개의 문자열을 입력 순서대로 출력
        result = ""
        for y in year_lst:
            s_idx = y % N  # mod로 인덱스 계산
            t_idx = y % M  # mod로 인덱스 계산
            s = s_lst[s_idx-1] + t_lst[t_idx-1]  # 두 문자열을 concat
            result += s + " "  # 출력을 위한 공백
        print(f"#{tc} {result}")


solution()