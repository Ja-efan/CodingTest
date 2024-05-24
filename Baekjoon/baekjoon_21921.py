# https://www.acmicpc.net/problem/21921
# 블로그
# Silver III

import sys
from collections import defaultdict, Counter

input = sys.stdin.readline
output = sys.stdout.write

def solution(): # time out

    N, X = map(int, input().split())
    visitors = list(map(int, input().split()))

    max_dict = defaultdict(int)
    max_visitors = 0
    
    for i in range(N-X+1):
        summ = sum(visitors[i:i+X])
        if max_visitors <= summ:
            max_dict[summ] += 1
            max_visitors = summ

    if max_visitors == 0:
        output("SAD")
    else :
        output(str(max_visitors)+'\n')
        output(str(max_dict[max_visitors]))
        
def solution2():

    import sys
    from collections import defaultdict, Counter

    input = sys.stdin.readline
    output = sys.stdout.write

    N, X = map(int, input().split())
    visitors = list(map(int, input().split()))

    accm = [visitors[0]]
    for v in visitors[1:]:
        accm.append(accm[-1]+v)

    X_visitors = []
    for i in range(X-1, N):
        if i == X-1 :
            X_visitors.append(accm[i])
        else :
            X_visitors.append(accm[i]-accm[i-X])
    
    max_visit = max(X_visitors)
    if max_visit == 0:
        output("SAD")
    else :
        count = Counter(X_visitors)
        output(str(max_visit) + '\n')
        output(str(count[max_visit]))

    

solution2()