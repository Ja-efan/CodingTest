# 요리사
from itertools import combinations
"""
풀이 설명: 
    조합을 이용해서 하나의 요리에 들어가는 재료를 고른 뒤, 나머지 재료들로 다른 요리를 만든다.
    각각의 요리에 들어가는 재료들의 시너지를 더하고, 두 요리의 시너지 합의 차를 최소화 하는 재료 조합을 찾아낸다.
"""

def cook():
    N = int(input())  # 재료의 개수
    half_N = N // 2  # 하나의 음식에 들어가는 재료의 개수
    synergy = [list(map(int, input().split())) for _ in range(N)]
    min_diff = float('inf')  # 시너지 차이 초기 값 (최소값을 구해야 하므로 INF로 설정)
    # 1번 음식에 들어갈 재료 조합 리스트
    first_dish_ingredients_comb = list(combinations(list(range(0,N)), half_N))
    # 2번 음식에 들어갈 재료 조합 리스트
    second_dish_ingredients_comb = []
    for first_dish in first_dish_ingredients_comb:
        second_dish = []  # 2번 음식에 들어갈 재료 조합
        for ingredient in range(0, N):  # 모든 재료 순회
            if ingredient not in first_dish:  # 1번 음식 조합에 들어가 있지 않은 재료인 경우
                second_dish.append(ingredient)  # 2번 음식 조합에 추가
        second_dish_ingredients_comb.append(second_dish)  # 만들어진 2번 재료 조합을 리스트에 추가

    # 두 요리 각각에 들어가는 재료의 시너지를 계산하기 위해 순회
    for first, second in zip(first_dish_ingredients_comb, second_dish_ingredients_comb):
        first_synergy = 0  # 1번 음식에 들어가는 재료들의 시너지 합
        second_synergy = 0  # 2번 음식에 들어가는 재료들의 시너지 합

        # 두 음식에 들어가는 재료 조합 동시에 순회
        for first_ingredient_1, second_ingredient_1 in zip(first, second):
            # 똑같이 순회 (재료 간의 시너지 계산)
            for first_ingredient_2, second_ingredient_2 in zip(first, second):
                # 1번 음식 재료들의 시너지 누적
                first_synergy += synergy[first_ingredient_1][first_ingredient_2]
                # 2번 음식 재료들의 시너지 누적
                second_synergy += synergy[second_ingredient_1][second_ingredient_2]

        # 두 음식의 시너지 차이 (절대값)
        diff = abs(first_synergy - second_synergy)
        # 최소 차이값 갱신
        min_diff = min(min_diff, diff)

    # 결과 반환
    return min_diff


def main():
    T = int(input())
    for tc in range(1, T + 1):
        result = cook()
        print(f"#{tc} {result}")
    return


if __name__ == "__main__":
    import sys
    sys.stdin = open("./testcases/input_4012.txt")
    main()