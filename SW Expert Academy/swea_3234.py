# 준환이의 양팔저울
# D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWAe7XSKfUUDFAUw

"""
풀이 설명 :
    1. 주어진 무게 추를 모두 사용해 구성할 수 있는 모든 순열을 만든다. (길이가 N -> nPn)
    2. 순열이 만들어진 시점마다 dfs를 이용해 left와 right를 구성한다.
    3. 이때 backtracking을 적용해, 가지치기를 해준다.
"""


def recursion(weights, right, left, idx, N, threshold):
    global cnt  # 가능한 모든 경우의 수
    if idx == N:  # 주어진 무게 추를 모두 left와 right에 나눈 상태
        cnt += 1  # 경우의 수 추가
        return
    if left > threshold:  # pruning : 왼쪽무게가 전체 무게의 절반 초과인 경우 이후 무게 추를 어디에 놓던지 L >= R 만족
        cnt += 2 ** (N - idx)  # 남은 무게 추는 left or right 고르기만 하면 됨
        return
    # left 추가
    recursion(weights, right, left + weights[idx], idx + 1, N, threshold)
    # left를 초과하지 않는 선에서 right 추가
    if right + weights[idx] <= left:
        recursion(weights, right + weights[idx], left, idx + 1, N, threshold)


def permutation(perm, rest, n, threshold):
    if len(perm) == n:  # 순열이 완성된 시점 -> 해당 순열로 왼쪽/오른쪽 구성하기 위한 재귀 함수 호출
        recursion(weights=perm, right=0, left=0, idx=0, N=n, threshold=threshold)  # 초기 상태로 재귀 함수 호출
        return  # 해당 순열로 만들 수 있는 모든 경우 만들고 return
    for i in range(len(rest)):
        permutation(perm + [rest[i]], rest[:i] + rest[i + 1:], n, threshold)  # 순열 구성을 위한 재귀 호출
    return


def main():
    T = int(input())  # test case 개수
    global cnt  #, N, threshold  # global variable 선언
    for tc in range(1, T + 1):
        # test case 마다 새로 초기화 해 주어야 하는 값들
        N = int(input())  # 무게 추 개수
        weights = list(map(int, input().split()))  # 무게 추 리스트
        threshold = sum(weights) // 2  # pruning을 위한 임계값
        init_perm = []  # perm 초기 값
        cnt = 0  # 각 test case 마다 cnt 초기화
        permutation(perm=init_perm, rest=weights, n=N, threshold=threshold)
        print(f"#{tc} {cnt}")


if __name__ == "__main__":
    # 아래 3 가지 변수는 주로 recursion() 함수에서 사용되는 변수들이다.
    # N과 threshold는 global 로 선언하기 전에 recursion()이 호출 될 때마다 새로 계산되는
    # function scope의 local variable 이었으나, 재귀 함수 특성 상 호출 수가 많아질 수록
    # 해당 변수 선언 및 초기화에 많은 시간이 들어가게 된다.
    # 따라서 해당 변수들을 global로 선언 한 뒤, main() 함수에서 각 test case 에 맞게 한 번만 계산 후
    # recursion()은 global variable을 바로 사용하면, 시간이 상당히 많이 줄어든다.

    # global variable 사용을 지양하고 싶다면 해당 변수들을 main() 내에서 선언 및 초기화 후
    # 해당 함수 호출 시 인자로 넘겨주면 될 것 같다.

    # 현재 코드는 global variable을 최소한으로 사용
    cnt = 0
    main()
