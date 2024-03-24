# 12980 점프와 순간이동

def solution(n:int)-> int:
    """
    Jumping and Teleporting : 

    Args : 
    - n : 가야하는 거리 (1이상 10억 이하의 자연수)

    Returns : 도착지점 까지 가는데 필요한 최소한의 건전지 사용량

    """

    jump = 0
    teleport = 0
    while n != 0:
        # print(n)
        a,b = divmod(n,2)
        if b == 0:
            teleport += 1
        else :
            jump += 1
            teleport += 1
        n = n//2
        

    # print(teleport)
    # print(jump) 
    return jump
    
        
# solution(6)

print(solution(5))
print(solution(6))
solution(5000)