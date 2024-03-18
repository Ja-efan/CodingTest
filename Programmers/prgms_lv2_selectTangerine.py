import numpy as np

def solution(k, tangerine):
    """
    tangerine 에서 k 개의 귤을 선택할 때, 크기를 최소로 선택
    사이즈 별로 개수를 세서, 정렬 후 큰 것 부터 선택해서 k를 맞춘다
    """
    answer = 0
    sizes = np.unique(tangerine) # 바구니에 담긴 귤의 크기 
    num_size = [0 for i in range(len(sizes))] # 사이즈 별 담긴 귤의 개수 
    # print(num_size) 
    # print(sizes)
    for i in tangerine:
        for j in range(len(sizes)):
            if i == sizes[j]:
                num_size[j] = num_size[j] + 1
    
    print(np.sort(num_size)[::-1])
    num_size = np.sort(num_size)[::-1]
    
    count = 0
    for i in num_size :
        if answer == k :
            break
        elif answer + i > k :
            continue
        answer = answer + i
        count = count + 1

        
    return count 