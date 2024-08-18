# 최소공배수
# Bronze I
# https://www.acmicpc.net/problem/1934


def gcd(a, b):
    if a > b:
        while b:
            c = a % b
            a = b
            b = c
        return a
    elif b > a:
        while a:
            c = b % a
            b = a
            a = c
        return b
    else:  # a == b
        return a


def main():
    T = int(input())  # 테스트 케이스 개수
    for tc in range(1, T+1):
        A, B = map(int, input().split())
        print(A*B // gcd(A, B))


if __name__ == "__main__":
    main()