# 92335
# https://school.programmers.co.kr/learn/courses/30/lessons/92335
# k진수에서 소수 개수 구하기 

def to_k(n, k)->str:
    if k == 10 : 
        return str(n)
    knum = ''
    while n :
        knum += (str(n%k))
        n //= k
    return knum[::-1]

def is_prime(n)->bool:
        if n == 1:
            return False
        """
        소수 판별 범위를 줄이는 게 관건인 듯 하다.
        """
        for i in range(2, int(n**0.5)+1): # range(2, (n//2)+1) 로 범위 지정시 timeout 
            if n % i == 0 :
                return False
        return True

def solution(n:int, k:int) -> int:
    
    answer = 0
    # n을 k진수로 변환 
    n2k = to_k(n, k) # str type
    # print(f"n2k : {n2k, type(n2k)}")
    nums = n2k.split('0')
    # print(nums)
    for s in nums:
        if len(s) and is_prime(int(s)):
            answer += 1

    return answer 

    

# test case
print(solution(437674,3)) # 3
print('-'*30)
print(solution(110011,10)) # 2