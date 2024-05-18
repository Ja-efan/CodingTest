# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1&&&&&&&&&&
# 파리 퇴치
# D2

def solution():
    t = int(input())
    for tc in range(1, t+1):
        N, M = map(int, input().split())
        flies = []
        for _ in range(N):
            flies.append(list(map(int, input().split())))

        max_ = 0
        for i in range(N-M+1):  # 혀용 가능한 범위
            for j in range(N-M+1):
                sum_ = 0  # 파리 수
                for k in range(M):  # 파리채 범위
                    for l in range(M):
                        sum_ += flies[i+k][j+l]  # 파리 수 합산
                max_ = max(max_, sum_)  # 최대 파리수 업데이트

        print(f"#{tc} {max_}")  # 결과 출력


solution()