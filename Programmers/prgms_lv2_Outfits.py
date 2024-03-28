# 42578
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    """
    의상 :
    의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 반환

    Args :
    - clothes : 의상 정보가 담긴 2차원 배열, 각 행은 [의상의 이름, 의상의 종류]로 구성되어 있음. 
                의상의 개수는 1개 이상 30개 이하 
                같은 이름의 의상은 존재하지 않음
                모든 원소는 문자열로 구성

    Returns : 서로 다른 옷의 조합의 수
    """
    cloth_dict = {
        k : [] for _,k in clothes
    }


    for cloth in clothes:
        cloth_dict[cloth[1]].append(cloth[0])
    print(cloth_dict)

    answer = 1
    for i in cloth_dict.values():
        answer *= len(i)+1

    return answer-1


# test case
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
