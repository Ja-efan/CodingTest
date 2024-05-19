# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AYtrCJQaDb4DFAR-&categoryId=AYtrCJQaDb4DFAR-&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 팰린드롬 문제
# D3
def is_palindrome(s)->bool:
    if s == s[::-1]:
        return True
    else :
        return False


def solution():
    t = int(input())
    for tc in range(1, t + 1):
        N, M = map(int, input().split())  # 1 <= N <= 100, 1 <= M <= 50
        strings = []
        for _ in range(N):
            strings.append(input())
        cnt_palindrome = 0
        cnt = 0
        for i in range(N):
            s1 = strings[i]
            if is_palindrome(s1):
                cnt_palindrome += 1
                continue
            for j in range(N):
                s2 = strings[j]
                if not is_palindrome(s2) and s1 == s2[::-1]:
                    cnt += 1

        answer = 0
        if cnt_palindrome:
            answer = M + M*cnt
        else:
            answer = M*cnt

        print(f"#{tc} {answer}")


solution()
