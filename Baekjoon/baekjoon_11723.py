# https://www.acmicpc.net/problem/11723
# 집합
# Silver V

def solution():
    M = int(input())
    S = []
    for _ in range(M):
        cmd = input()
        oprtn = ""
        x = 0
        if len(cmd.split()) == 1:
            oprtn = cmd 
        else :
            oprtn, x = cmd.split()
            x = int(x)
        if oprtn == 'add':
            if x not in S:
                S.append(x)
        elif oprtn == 'remove':
            if x in S:
                S.remove(x)
        elif oprtn == 'check':
            if x in S:
                print(1)
            else :
                print(0)
        elif oprtn == 'toggle':
            if x not in S:
                S.append(x)
            else :
                S.remove(x)
        elif oprtn == 'all':
            S = list(range(1,21))
        elif oprtn == 'empty':
            S = []

def solution2():

    M = int(input())
    S = set()

    for _ in range(M):
        cmd = input().split()
        oprtn = ""
        x = 0
        if len(cmd) == 1:
            oprtn = cmd[0]
        else :
            oprtn = cmd[0]
            x = int(cmd[1])

        if cmd == 'add':
            S.add(x)
        elif cmd == 'remove':
            # remove()의 경우 원소가 없는 경우 KeyError 발생시킨다.
            S.discard(x)
        elif cmd == "check":
            if x in S:
                print(1)
            else :
                print(0)
        elif cmd == "toggle":
            if x in S:
                S.discard(x)
            else :
                S.add(x)
        elif cmd == "all":
            S = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
        elif cmd == "empty":
            S = set()


def solution3():
    import sys
    input = sys.stdin.readline
    # print = sys.stdout.write2

    m = int(input().rstrip())
    S = set()
    for _ in range(m):
        cmd = input().rstrip().split()
        # print(cmd)
        if cmd[0] == "add":
            S.add(int(cmd[1]))
        elif cmd[0] == 'remove':
            S.discard(int(cmd[1]))
        elif cmd[0] == 'check':
            x = int(cmd[1])
            if x in S:
                print(1)
            else :
                print(0)

        elif cmd[0] == 'toggle':
            x = int(cmd[1])
            if x in S:
                S.discard(x)
            else :
                S.add(x)
        elif cmd[0] == 'all':
            S = set(range(1,21))
        
        elif cmd[0] == 'empty':
            S = set()

solution3()
        