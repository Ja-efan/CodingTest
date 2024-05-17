# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5Pw_-KAdcDFAUq&categoryId=AV5Pw_-KAdcDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1&&&&&&&&&&
# 중간 평균값 구하기
# D2

def solution():
    t = int(input())
    for tc in range(1, t+1):
        lst = list(map(int, input().split()))

        lst.sort()  # 정렬
        lst = lst[1:-1]  # 최소값과 최대값을 제외한 리스트
        sum_ = 0
        for i in lst:
            sum_ += i  # 누적 합

        answer = round(sum_/len(lst))  # 평균 계산 및 반올림
        print(f"#{tc} {answer}")


solution()