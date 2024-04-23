# 120869
# https://school.programmers.co.kr/learn/courses/30/lessons/120869

def solution(spell:list, dic:list) -> int:
    """
    외계어 사전 :
    알파벳이 담긴 배열 spell과 외계어 사전 dic가 주어질 때, spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 
    dic에 존재한다면 1, 존재하지 않는다면 2를 Return.

    Args :
    - spell : 
    - dic : 

    * spell과 dic의 원소는 알파벳 소문자로만 이루어져 있다.

    """
    # from collections import Counter
    
    # counter_list = []
    # answer = 0
    # for word in dic :
    #     word_list = [c for c in word]
    #     word_count = Counter(word_list)
    #     counter_list.append(word_count)
    #     print(word_count)

    # for cl in counter_list:
    #     for count in cl.values():
    #         if count > 1 :
    #             return 2


    from itertools import permutations

    perm = list(permutations(spell, len(spell)))
    # print(perm)
    for p in perm:
        p = list(p)
        p = ''.join(p)
        if p in dic :
            return 1

    return 2

            



# test case 
print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"])) # 2
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"])) # 1
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"])) # 2