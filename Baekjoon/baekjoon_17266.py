# https://www.acmicpc.net/problem/17266
# 어두운 굴다리
# Silver IV

import sys

input = sys.stdin.readline

def solution():
    n = int(input().rstrip())  # 굴다리의 길이 
    m = int(input().rstrip())  # 설치할 수 있는 가로등의 개수
    loc = list(map(int, input().rstrip().split()))  # 설치할 수 있는 가로등의 위치 

    """
    1. 가장 왼쪽에 있는 가로등이 굴다리의 시작 부분까지 비추어야 한다.
    -> height >= loc[0]
    2. 가장 오른쪽에 있는 가로등이 굴다리의 끝 부분까지 비투어야 한다. 
    -> height >= (n-loc[-1])
    3. 1번과 2번 높이 중 큰 값이 height의 최솟값이 된다. (양 끝단을 비추기 위한 최소 높이)
    4. 가로등 간의 간격을 계산
    5. 최대 간격의 1/2가 height가 커버해야 할 범위
    6. 3번에서 구한 값과 5번에서 구한 값 중 더 큰 값을 최종 height로 취한다.
    """
    h_for_side = max(loc[0], n-loc[-1])

    max_distance = 0
    for i in range(m-1):
        distance = loc[i+1] - loc[i]
        if max_distance < distance:
            max_distance = distance
    
    # python의 round함수 동작 특성 때문에 0.1을 더해준 뒤 반올림 한다.
    half_max = round((max_distance/2)+0.1)

    height = max(half_max, h_for_side)

    print(height)


solution()


