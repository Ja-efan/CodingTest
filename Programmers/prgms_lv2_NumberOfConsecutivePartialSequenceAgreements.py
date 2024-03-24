# 131701

def solution(elements):

    """
    연속 부분 수열 합의 개수 :
    원형 수열의 연속하는 부분 수열의 합으로 만들 수 있는 수의 개수를 반환

    Args :
    - elements : 원형 수열의 모든 원소 (list)

    Returns :
    - 원형 수열의 연속 부분 수열 합으로 만들 수 있는 수의 개수 
    """

    length = len(elements)
    summ_list = set()
    for i in range(1, length+1):
        for j in range(length):
            left = j
            right = j+i
            summ = 0
            if right > length:
                right -= length
                summ = sum(elements[left:]) + sum(elements[:right])
            else :summ = sum(elements[left:right])
            summ_list.add(summ)

    # print(set(sorted(summ_list)))
    return len(summ_list)

# print(solution([7,9,1,1,4]))