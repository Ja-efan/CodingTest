# https://www.acmicpc.net/problem/1026
# 보물
# Silver IV

def solution():
    # 사용자 입력
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 리스트 곱 함수
    def list_mult(lst1:list, lst2:list) -> int:
        len_ = len(lst1)  # 인자(리스트) 길이
        sum_ = 0  # 결과 값
        for i in range(len_):
            sum_ += lst1[i] * lst2[i]  # i 번째 인덱스 원소끼리 곱셈 후 sum_에 합산
        return sum_

    a_sorted = sorted(a)  # 리스트 a를 오름차순으로 정렬
    b_sorted = sorted(b, reverse=True)  # 리스트 b를 내림차순으로 정렬

    answer = list_mult(a_sorted, b_sorted)  # 두 리스트 곱셈

    print(answer)  # 결과 출력


def solution2():
    # heap 이용 솔루션
    import heapq as hq

    # 사용자 입력
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    neg_b = [-i for i in b]  # 최대 힙으로 사용하기 위해 음수로 변환
    hq.heapify(a)  # heap으로 변경
    hq.heapify(neg_b) # heap으로 변경

    sum_ = 0
    while a:  # a에 원소가 있는 동안 반복
        sum_ += (hq.heappop(a)*(-hq.heappop(neg_b)))  # a의 최소값과 b의 최대값을 곱한 후 합산

    print(sum_)  # 결과 출력


solution2()





