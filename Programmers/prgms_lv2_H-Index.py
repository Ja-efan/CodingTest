# 42747
# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    """
    H-Index :
    과학자의 생산성과 영향력을 나타내는 지표.
    어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고, 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index

    Args :
    - ciatations : 어느 과학자가 발표한 논문의 인용 횟수를 담은 배열(List), 길이는 1 이상 1,000이하, 논문 별 인용 횟수는 0이상 10,000이하

    Returns : 해당 과학자의 H-Index
    """

    # solution 1
    # import numpy as np

    h_list = []
    # set_citations = sorted(set(citations)) # h 후보들
    # print(set_citations)
    max_citations = max(citations)
    for h in range(max_citations+1):
        over_h = 0

        for i in citations:
            if i >= h : over_h += 1
        
        under_c = len(citations) - over_h
        # print(f"{h} -> {over_h}, {under_c}")
        # print(over_h)
        if over_h >= h and under_c<= h:
            h_list.append(h)

        # print(h_list)
    return max(h_list)


# test case 
print(solution([3,0,6,1,6,2,2]))
print(solution([0,1,5,5,6,3,0,0]))

"""
아래 케이스의 경우 H-Index는 1이 아닌 2가 된다. 
'h번 이상된 논문'에서 h가 의미하는 숫자가 꼭 발표한 논문들의 인용 횟수일 필요는 없다.
"""
print(solution([1,10,20]))