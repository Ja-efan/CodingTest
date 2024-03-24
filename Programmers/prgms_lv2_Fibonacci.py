# 12945 

def solution(n):
    """
    피보나치 수 :
    F(0) = 0, F(1) = 1 일 때, 1이상의 n에 대하여 F(n) = F(n-1) + F(n+1)가 적용되는 수.

    Args :
    - n : 2이상 100,000 이하인 자연수 

    Returns : 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567로 나눈 나머지를 리턴
    """

    """
    # recursion 시간초과?
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    
    else :
        return solution(n-1) + solution(n-2)
    """
    fib = [0,1]
    for i in range(2,n+1):
        fib.append(fib[i-1]+fib[i-2])

    print(fib)
    # print(len(fib))

    return fib[-1]%1234567


print(solution(3))
print(solution(5))