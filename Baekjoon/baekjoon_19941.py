# https://www.acmicpc.net/problem/19941
# 햄버거 분배
# Silver III


def solution():

    import sys
    # from collections import Counter 

    input = sys.stdin.readline
    output = sys.stdout.write

    N, K = map(int, input().split())
    lines = [c for c in input().rstrip()]

    for i in range(N):
        if lines[i] == 'H' :  # 햄버거인 경우
            for j in range(i-K, i+K+1):  # 반경 K 내에서 줄 사람을 찾는다.
                if j >= 0 and j < N and lines[j] == 'P':  # 범위를 벗어나지 않고, 사람인 경우 
                    lines[j] = 0  # 해당 사람에게 햄버거 전달 (0으로 값 변경)
                    break  # 햄버거 전달 완료
        else :
            continue

    zero_count = 0
    for c in lines:
        if c == 0:
            zero_count += 1

    output(str(zero_count))

    # Counter 사용이 더 느리다.
    # count = Counter(lines)
    # output(str(count[0]))


solution()