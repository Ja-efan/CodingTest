# 준환이의 양팔저울
# D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWAe7XSKfUUDFAUw

from itertools import permutations


def recursion(weights, right, left, idx):
    global cnt
    # N = len(weights)
    # threshold = sum(weights)
    if idx == N:
        # print(left, right)
        cnt += 1
        return
    if left > threshold:
        cnt += 2 ** (N - idx)
        return
    # 왼쪽에 추가
    # left[idx] = weights[idx]
    recursion(weights, right, left + weights[idx], idx + 1)
    # left[idx] = 0
    # 오른쪽에 추가
    # if sum(right) + weights[idx] <= sum(left):
    if right + weights[idx] <= left:
        # right[idx] = weights[idx]
        recursion(weights, right + weights[idx], left, idx + 1)
        # right[idx] = 0


def permutation(perm, rest):
    if len(perm) == N:  # 순열이 완성된 시점 -> 해당 순열로 왼쪽/오른쪽 구성
        # right = [0 for _ in range(len(weights))]
        # left = [0 for _ in range(len(weights))]
        # right, left = 0, 0
        recursion(weights=perm, right=0, left=0, idx=0)
        return
    for i in range(len(rest)):
        # perm.append(rest[i])
        permutation(perm + [rest[i]], rest[:i] + rest[i + 1:])
        # perm.pop()
    return


def main():
    T = int(input())  # test case 개수
    global cnt, N, threshold  # global variable 선언
    for tc in range(1, T + 1):
        N = int(input())  # 무게 추 개수
        weights = list(map(int, input().split()))
        threshold = sum(weights) // 2
        # perm = []
        cnt = 0
        permutation(perm=[], rest=weights)
        # for perm in permutations(weights, N):
        #     recursion(perm, right=0, left=0, idx=0)
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
    cnt = 0
    N = 0
    threshold = 0
    main()
