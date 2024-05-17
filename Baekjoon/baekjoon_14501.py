# https://www.acmicpc.net/problem/14501
# 퇴사
# Silver III

def solution():
    n = int(input())
    schedule = []  # (상담기간, 금액)의 튜플로 구성된 상담 일정 리스트
    for i in range(n):
        schedule.append(tuple(map(int, input().split())))
    pop_list = []
    new_schedule = []
    check = [0 for _ in range(n)]
    for i in range(n):
        t = schedule[i][0]
        p = schedule[i][1]
        start = i
        end = i + t - 1
        if end > n-1:
            pop_list.append(i)
            continue
        new_schedule.append([start, end, p])
    # print(new_schedule)
    new_schedule.sort(key=lambda x: (x[2], x[0]))
    # print(new_schedule)
    pay = 0
    while new_schedule:
        cs = new_schedule.pop()
        start = cs[0]
        end = cs[1]
        p = cs[2]
        if sum(check[start:end + 1]):
            continue
        for i in range(start, end+1):
            check[i] = 1
        pay += p

    print(pay)


solution()