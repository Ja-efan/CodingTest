# https://www.acmicpc.net/problem/1037
# 약수
# Bronze I

def solution():
    num_of_factors = int(input())
    real_factors = list(map(int, input().split()))
    n = 0
    real_factors.sort()

    for i in range(num_of_factors):
        a = real_factors[i]
        for j in range(num_of_factors-1, -1,-1):
            b = real_factors[j]
            n = a*b

            result = 0
            for k in range(num_of_factors):
                result += n % real_factors[k]
            
            if result:
                continue

            else :
                print(n)
                return
                

solution()

