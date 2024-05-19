# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AV5QLkdKAz4DFAUq&categoryId=AV5QLkdKAz4DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 연월일 달력
# D3

def solution():
    days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    months = range(1, 13)

    t = int(input())

    for tc in range(1, t+1):
        date = input()
        year = date[:4]
        month = date[4:6]
        day = date[6:]
        if int(month) in months:
            if int(day) in range(1, days[int(month)]+1):
                print(f"#{tc} {year}/{month}/{day}")
            else :
                print(f"#{tc} {-1}")
        else :
            print(f"#{tc} {-1}")


solution()


