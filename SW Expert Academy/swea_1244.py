# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&problemLevel=4&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=1
# 최대 상금
# D3

def maximize_number(s, k):
    max_num = [0]

    def dfs(s, k):
        if k == 0:
            max_num[0] = max(max_num[0], int("".join(s)))
            return

        n = len(s)
        for i in range(n):
            for j in range(i + 1, n):
                s[i], s[j] = s[j], s[i]
                dfs(s, k - 1)
                s[i], s[j] = s[i], s[j]

    s_list = list(s)
    dfs(s_list, k)
    return max_num[0]


def solution():
    T = int(input())
    for t in range(1, T + 1):
        s, k = input().split()
        k = int(k)
        result = maximize_number(s, k)
        print(f"#{t} {result}")


solution()