# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AYcllbDqUVgDFASR&categoryId=AYcllbDqUVgDFASR&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2
# 원 안의 점
# D3

def solution():

    t = int(input())
    for tc in range(1, t+1):
        n = int(input())

        """
        반지름이 n인 원 안에 포함되는 격자점(좌표 x,y가 모두 정수)의 개수
        x**2 + y**2 <= n**2
        q1*4(1사분면 좌표 * 4) + 4*n(축에 있는 좌표) + 1(원점) 
        """
        cnt = 0
        for x in range(1, n+1):
            for y in range(1, n+1):
                if x**2 + y**2 <= n**2:
                    cnt += 1
        cnt = cnt * 4  # 총 4개 사분면
        cnt += 4*n
        cnt += 1  # 원점 추가
        print(f"#{tc} {cnt}")


solution()