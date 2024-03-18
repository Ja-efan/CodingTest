import numpy as np

def solution(k, tangerine):
    
    """
    solution(k, tangerine):


    Args :
    - k : 고르고자 하는 귤의 개수 
    - tangerine : 귤의 사이즈를 담고 있는 리스트

    Returns :
    - int : k개의 귤을 고르기 위한 귤 사이즈의 최소 개수
    """

    size_counts = {} # dict 생성 
    for size in tangerine:
        if size in size_counts:
            size_counts[size] += 1
        else : 
            size_counts[size] = 1
    
    # print(size_counts)

    size_counts = sorted(size_counts.items(), key=lambda x:x[1], reverse=True)

    # print(size_counts)

    total_selected = 0
    distinct_sizes = 0
    for size, count in size_counts:
        if total_selected + count <= k:
            total_selected += count
            distinct_sizes += 1
        else: # total_selcted + count > k 
            distinct_sizes += 1
            break
        if total_selected == k :
            break

    return distinct_sizes


# # test case
# tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
# k = 5
# print(solution(k,tangerine))