# Bottom-Up: Tabulation
def fibonacci_BU(n:int) -> int:
    
    # tabulation을 위한 list 정의
    dp = list()
    # 기저 상태 n=0 -> 0, n=1 -> 1
    dp.append(0)
    dp.append(1)

    for i in range(2, n+1):
        # 점화식 정의 : F(n) = F(n-1) + F(n-2)
        x = dp[i-1] + dp[i-2]
        # 결과 저장 
        dp.append(x)

    return dp[n]


# Top-Down : Memoization
def fibonacci_TD(n:int) -> int:
    # 기저 상태 n=0 -> 0, n=1 -> 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fibonacci_TD(n-1) + fibonacci_TD(n-2)


# test case 
# n = 10 -> 55
print(fibonacci_TD(10)) 
print(fibonacci_BU(10)) 

# n = 5 -> 5
print(fibonacci_TD(5)) 
print(fibonacci_BU(5))  
