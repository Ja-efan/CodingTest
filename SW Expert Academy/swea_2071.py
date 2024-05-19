# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AV5QRnJqA5cDFAUq&categoryId=AV5QRnJqA5cDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 평균값 구하기
# D1

def solution():
    t = int(input())

    for tc in range(1, t+1):
        nums = list(map(int, input().split()))
        summ = 0
        for n in nums:
            summ += n
        avg = summ / len(nums)
        avg = round(avg)
        print(f"#{tc} {avg}")

    return

solution()
