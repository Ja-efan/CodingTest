# 1845
# https://school.programmers.co.kr/learn/courses/30/lessons/1845
# Hash

def solution(nums:list) -> int:

    """
    폰켓몬 : 
    N 마리의 폰켓몬 중 N/2마리를 고를 때, 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아 그때의 폰켓몬 종류 번호의 개수를 반환

    Args :
    - nums : 폰켓몬의 종류가 담긴 1차원 배열(list)
             nums의 길이는 1이상 10,000 이하의 짝수
             폰켓몬의 종류 번호는 1이상 200,000 이하의 자연수로 표현
            
    Returns : 종류 번호의 개수를 반환 (int)
    """


    ponkemon = {
        p : 0 for p in nums
    }

    for p in nums:
        ponkemon[p] += 1
    
    # print(ponkemon)
    
    half = len(nums)//2
    if half <= len(ponkemon) :
        return half
    else : # half > len(ponkemon)
       return len(ponkemon)
    



# test case
print(solution([3,1,2,3]))