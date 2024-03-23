# 42885

def solution(people, limit):
    """
    Lifeboats : 
    무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 한다. 
    구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있다.

    구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 한다.
    
    Args : 
    - people : 사람들의 몸무게를 담은 리스트 (1명 이상 50,000명 이하 (각 사람의 몸무게는 40kg 이상 240kg 이하))
    - limit : 구명보트의 무게 제한 (구명보트의 무게제한은 40kg 이상 240kg 이하)

    Returns : 모든 사람을 구출하기 위해 필요한 구명보트의 개수의 최솟값
    """
    people = sorted(people) # 오름차순 정력
    # print(people)
    # print(people.pop()) # 남은 사람 중 가장 무거운 사람 Pop
    # print(people)

    # answer = 0
    # while people :
        
    #     if len(people) == 1:
    #         answer += 1
    #         break
            
    #     elif people.pop() + people[0] <= limit :
    #         people.pop(0)
    #         # people = people[1:] # people.pop(0) 보다 느림
    #         answer += 1
            
    #     else : 
    #         answer += 1 
        
    answer = 0
    left = 0 
    right = len(people)-1
    while left <= right:
        if people[left] + people[right] <= limit :
            right -= 1
            left += 1
            answer += 1
        else : 
            answer += 1
            right -= 1

    return answer 


print(solution([70,50,80,50], 100))
print(solution([70,50,80], 100)) 