# https://www.acmicpc.net/problem/14501
# 퇴사
# Silver III

def solution():
    global result
    N = int(input())
    schedule = []  # [t,p]로 구성된 상담 일정 리스트, t: 상담 완료까지 걸리는 기간, p: 상담 금액
    for i in range(N):
        t, p = map(int, input().split())
        schedule.append([i+1, t + i, p])  # [상담 시작 일, 상담 종료 일, 금액]으로 구성
    memo = [0 for _ in range(N+1)]
    for i in range(N):
        for j in range(schedule[i][1],  N+1):
            if memo[j] < memo[i] + schedule[i][2]:
                memo[j] = memo[i] + schedule[i][2]
    print(memo)
    print(memo[-1])


if __name__ == "__main__":
    result = 0
    solution()
