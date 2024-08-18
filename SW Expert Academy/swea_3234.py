# 준환이의 양팔저울
# D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWAe7XSKfUUDFAUw

def recursion(weights, right, left, idx):
    global cnt
    if idx == len(weights):
        # print(left, right)
        cnt += 1
        return
    # 왼쪽에 추가
    # left[idx] = weights[idx]
    recursion(weights, right, left+weights[idx], idx + 1)
    # left[idx] = 0
    # 오른쪽에 추가
    # if sum(right) + weights[idx] <= sum(left):
    if right + weights[idx] <= left:
        # right[idx] = weights[idx]
        recursion(weights, right+weights[idx], left, idx + 1)
        # right[idx] = 0


def permutation(weights, perm):
    if len(perm) == len(weights):  # 순열이 완성된 시점 -> 해당 순열로 왼쪽 오른쪽 구성해야 함
        # right = [0 for _ in range(len(weights))]
        # left = [0 for _ in range(len(weights))]
        right, left = 0, 0
        # print(f"perm: {perm}")
        recursion(weights=perm, right=right, left=left, idx=0)
        # print("-" * 100)
        return
    for i in range(len(weights)):
        if weights[i] not in perm:
            perm.append(weights[i])
            permutation(weights, perm)
            perm.pop()
    return


def main():
    T = int(input())  # test case 개수
    global cnt
    for tc in range(1, T + 1):
        N = int(input())  # 무게 추 개수
        weights = list(map(int, input().split()))
        perm = []
        cnt = 0
        permutation(weights, perm)
        print(f"#{tc} {cnt}")


if __name__ == "__main__":
    cnt = 0
    main()
