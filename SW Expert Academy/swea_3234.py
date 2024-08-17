# 준환이의 양팔저울
# D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWAe7XSKfUUDFAUw


def recursion(idx, right, left, perm, bp):
    global cnt
    if idx == bp:
        return
    for weight in perm:
        if weight not in right:
            if sum(right) + weight < sum(left):
                cnt += 1
                right.append(weight)
                new_left = [w for w in perm if w not in right]
                recursion(idx=idx+1, right=right, left=new_left, perm=perm, bp=bp)
                right.pop()

def permutation(weights, perm):
    if len(perm) == len(weights):  # 순열이 완성된 시점 -> 해당 순열로 왼쪽 오른쪽 구성해야 함
        right = []
        left = [w for w in perm]
        recursion(idx=0, right=right, left=left, perm=perm, bp=len(weights))
        return
    for i in range(len(weights)):
        if i not in perm:
            perm.append(i)
            permutation(weights, perm)
            perm.pop()
    return


def main():
    T = int(input())  # test case 개수
    global cnt
    for tc in range(1, T+1):
        N = int(input())  # 무게 추 개수
        weights = list(map(int, input().split()))
        perm = []
        cnt = 0
        permutation(weights, perm)
        print(f"#{tc} {cnt}")


if __name__ == "__main__":
    cnt = 0
    main()