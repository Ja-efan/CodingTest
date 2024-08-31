# boj 2579
# 계단 오르기
# Silver III

"""
1. 계단은 한 번에 한 계단 씩 또는 두 계단씩 오를 수 있다.
 즉, 한 계단을 밟으면서 이어서 다음 계단이, 다음 다음 계단으로 오를 수 있다.

2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.

3. 마지막 도착 계단은 반드시 밟아야 한다.
    -> 반대로 내려가야 한다.
"""

def main():
    N = int(input())

    memo = [0 for _ in range(301)]  # N으로 주면 N이 3 미만일 경우 index error
    scores = [0 for _ in range(301)]
    for i in range(1, N+1):
        scores[i] = int(input())

    memo[1] = scores[1]
    memo[2] = scores[1] + scores[2]
    memo[3] = max(scores[1] + scores[3], scores[2] + scores[3])

    for i in range(4, N+1):
        memo[i] = max(scores[i-1] + scores[i] + memo[i-3],
                      memo[i-2] + scores[i])

    # print(memo)
    print(memo[N])
if __name__ == "__main__":
    main()