# 64065
# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s:str) -> list:
    """
    튜플 :
    - 중복된 원소가 존재할 수 있다.
    - 순서가 있으며, 원소의 순서가 다르면 서로 다른 튜플이다.
    - 원소의 개수는 유한하다.

    원소의 개수가 n개이고, 중복된 원소가 없는 튜플 (a1,a2,a3,...,an)이 주어질 때, 이는 다음과 같이 집합 기호 {}를 이용해 표현 가능하다.
    - {{a1}, {a1, a2}, {a1,a2,a3}, {a1,a2,a3,...an}}

    이때, 집합은 원소의 순서가 바뀌어도 상관없으므로 아래 집합은 모두 같은 튜플을 나타낸다.
    - {{a1}, {a1,a2,a3}, {a1, a2}, {a1,a2,a3,...an}}
    - {{a1,a2,a3,...an}, {a1}, {a1,a2,a3}, {a1, a2}}
    - {{a1,a2,a3,,...an}, {a1}, {a2,a1,a3}, {a2, a1}}
    
    특정 튜플을 표현하는 집합이 담긴 문자열 s가 매개변수로 주어질때, s가 표현하는 튜플을 배열에 담아 반환.

    Args :
    - s : 튜플을 표현하는 집합이 담긴 문자열 

    Returns : s가 표현하는 튜플을 배열로 반환 
    
    """
    
    s = s[1:-1] # 맨 앞, 맨 뒤 중괄호 제거 

    s = s.replace('{', "")
    s = list(s.split("},"))
    s[-1] = s[-1].replace('}', "")

    # print(s)

    s_dict = {} # {length : list}
    # s_list = []
    tmp = ""
    length = len(s)
    for s_ in s:
        s_list = s_.split(',')
        # print(s_list)
        s_list = list(map(int, s_list))
        # print(s_list)
        s_dict[len(s_list)] = s_list
    
    s_dict = dict(sorted(s_dict.items())) # Key값을 기준으로 오름차순 정렬

    # print(s_dict)

    answer = [s_dict[1][0]]
    # print(answer)
    for k, v in s_dict.items():
        for e in v:
            if e in answer:
                continue   
            else : 
                answer.append(e)

  
    # print(s_list)


    return answer

    



# test case
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{20,111},{111}}"))