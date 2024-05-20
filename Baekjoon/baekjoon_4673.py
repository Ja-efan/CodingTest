# https://www.acmicpc.net/problem/4673
# 셀프 넘버
# Silver V


def d(n):
    str_d = str(n)
    for i in range(len(str_d)):
        n += int(str_d[i])
    return n


def solution():
    lst = [0 for _ in range(10000)]

    for n in range(1, 10000+1):
        dn = d(n)
        if dn <= 10000:
            lst[dn-1] = 1
    
    for i, dn in enumerate(lst):
        if dn == 0 :
            print(i+1)


solution()

        
        
            

