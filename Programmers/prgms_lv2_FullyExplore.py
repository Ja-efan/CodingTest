# 42842 
import numpy as np
import math
def solution(brown, yellow):
    """
    Fully Explore :

    Args :
    - brown : natural number between 8 and 5000
    - yellow : natural number between 1 and 2,000,000

    Returns : size of carpet -> [width, height]

    fyi. 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 길다.
    """
    # yellow_size = [yellow, 1]
    # brown_size = [yellow_size[0]+2, yellow_size[1]+2] # brown_size[0] * brown_size[1] - yellow_size[0]*yellow_size[1] = brown
    
    # yellow_divisors = []
    # for i in range(2, yellow//2+1):
    #     if yellow % i == 0:
    #         yellow_divisors.append(i)

    # # yellow_divisors.reverse()
        
    # check = False 

    # idx = 0
    # while not(check):
    #     if ((brown_size[0] * brown_size[1]) - (yellow_size[0]*yellow_size[1])) == brown:
    #         break
    #     yellow_size[0] = yellow // yellow_divisors[idx]
    #     yellow_size[1] += 1
    #     brown_size = [yellow_size[0]+2, yellow_size[1]+2]
    #     idx += 1

    # return brown_size

    a = 2
    b = (-4-brown)
    c = 2*(yellow+brown)
    D = b**2 - 4*a*c
    # print(D)

    x = (-b + math.sqrt(D)) / (2*a)
    y = (-b - math.sqrt(D)) / (2*a)
    # print(x, y)
    if x > y : 
        return [x,y]
    else : 
        return [y,x]

    # a = 1
    # b = - (brown / 2 + 2)
    # c = brown + yellow

    # D = b**2 - 4*a*c

    # x1 = (-b + math.sqrt(D)) / (2*a)
    # x2 = (-b - math.sqrt(D)) / (2*a)

    # answer = []
    # answer.append(x1)
    # answer.append(x2)


    # return answer

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))
