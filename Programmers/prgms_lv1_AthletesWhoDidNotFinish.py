# 42576
# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# Hash

def solution(participant:list, completion:list) -> str:

    """
    완주하지 못한 선수 :
    마라톤을 완주하지 못한 선수의 이름을 반환하는 함수 (잔인해,,,)

    Args : 
    - participant : 마라톤에 참가한 선수들의 이름이 담긴 배열(list)
                    1명 이상 100,000명 이하 
                    참가자의 이름은 1개 이상 20개 이하의 소문자로 구성
                    동명이인 존재 할 수 있음

    - completion : 완주한 선수들의 이름이 담긴 배열(list)
                   participant의 길이보다 1 작다.


    Returns : 완주 하지 못한 선수의 이름(str)
    """

    # # solution 1 : using dictionary
    # runner = {
    #     name : 0 for name in participant
    # }
    # for name in participant:
    #     runner[name] += 1
    
    # for name in completion:
    #     if name in runner.keys():
    #         runner[name] -= 1


    # for k, v in runner.items():
    #     if v == 1 :
    #         return k



    # # solution 2 : using stack 
    # # 효율성 all timed out
    # participant = sorted(participant)
    # completion = sorted(completion)
    # for name in completion:
    #     if name in participant:
    #         participant.remove(name)

    # return participant[0]

    # solution 3 : sorting
    # idea : participant와 completion을 동일하게 정렬하면 다른 부분이 생김을 이용
    # completion에 대해서만 1회 순회하므로 O(n)
        
    completion = sorted(completion)
    participant = sorted(participant)

    for i in range(len(completion)):
        if completion[i] != participant[i]: # 참가자와 완주자의 이름이 같지 않은 경우 해당 참가자는 완주 하지 못한 것이므로 참가자의 이름 반환
            return participant[i] 
    
    return participant[len(participant)-1] # completion의 모든 이름을 순회한 경우 -> 마지막 참가자가 완주하지 못한 선수!!

# test case
print(solution(["leo", "kiki", "eden", "eden"], ["leo","eden", "kiki"]))