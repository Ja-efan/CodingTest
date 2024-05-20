# https://www.acmicpc.net/problem/4375
# 1
# Silver III

def solution():
    while True:
        try:
            n = input()

            n = int(n)
            m = 1
            i = 1
            while m % n != 0:
                m += 10**i
                i += 1
            answer = len(str(m))
            print(answer)
        except:
            break


solution()
        