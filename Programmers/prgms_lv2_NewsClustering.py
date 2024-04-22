# 17677
# https://school.programmers.co.kr/learn/courses/30/lessons/17677

import itertools 
def solution(str1:str, str2:str) -> int:
    """
    뉴스 클러스터링 :

    Args : 
    - str1 : 길이 2 이상 1,000 이하의 문자열
    - str2 : 길이 2 이상 1,000 이하의 문자열

    Returns : 두 문자열의 자카드 유사도,
        유사도 값은 0에서 1사이의 실수이므로, 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력
    """

    multi_set1 = []
    for i in range(len(str1)-1):
        tmp = str1[i:i+2]
        if not tmp.isalpha(): 
            continue
        multi_set1.append(tmp.lower())

    multi_set2 = []
    for i in range(len(str2)-1):
        tmp = str2[i:i+2]
        if not tmp.isalpha():
            continue
        multi_set2.append(tmp.lower())

    multi_set1 = sorted(multi_set1)
    multi_set2 = sorted(multi_set2)

    # print("multi_set1 & multi_set2")
    # print(multi_set1, multi_set2)

    intersection_list = []
    union_list = []
    while multi_set1:
        e = multi_set1.pop(0)
        if e in multi_set2:
            e2 = multi_set2.pop(multi_set2.index(e))
            intersection_list.append(e)
        union_list.append(e)

    if multi_set2:
        for e in multi_set2:
            union_list.append(e)

    # print(intersection_list)
    # print(union_list)
        
    if not union_list and not intersection_list:
        return 65536
    else :
        jaccard = len(intersection_list) / len(union_list)
        return int(jaccard * 65536)
    

# test case 
print(solution('FRANCE', 'french')) # 16384

print(solution('handshake', 'shake hands')) # 65536

print(solution('aa1+aa2','AAAA12')) # 43690

print(solution('E=M*C^2', 'e=m*c^2')) # 65536