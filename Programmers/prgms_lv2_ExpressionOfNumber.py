# 12924

def solution(n:int) -> int:
    """
    Expression of Number : 
    자연수 n이 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 반환
    
    Args :
    - n : 자연수 
    
    Returns : 연속된 자연수들로 n을 표현하는 방법의 수 

    Example :
    n = 15 -> 1+2+3+4+5 & 4+5+6 & 7+8 & 15 -> return 4
    """

    answer = 1
    for i in range(1, n//2+1):
        # print('-' * 20)
        total = 0
        for j in range(i, n//2+2):
            # print(f'j : {j}')
            total += j
            # print(f'total {total}')
            if total == n :
                answer += 1
                # print('ckeck')
                break
            elif total > n : 
                break
            
    return answer 



# test case 
print(solution(12))
print(solution(15))