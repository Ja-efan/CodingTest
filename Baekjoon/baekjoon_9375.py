# https://www.acmicpc.net/problem/9375
# 패션왕 신해빈
# Silver III

def solution():
    t = int(input())
    for _ in range(1, t+1):
        n = int(input())
        closet = dict()  # defaultdict 사용 하지 않고 풀어보기
        for _ in range(n):
            cloth, category = input().split()
            if category in closet.keys():
                closet[category].append(cloth)
            else:
                closet[category] = [cloth]

        sum_ = 1
        for clothes in closet.values():
            sum_ *= len(clothes)+1  # +1? 아무것도 입지 않는 경우도 추가 해준다.

        sum_ -= 1  # 전부 다 입지 않는 경우 제외

        print(f"{sum_}")


solution()