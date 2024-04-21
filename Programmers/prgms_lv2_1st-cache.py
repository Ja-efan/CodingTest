# 17680
# https://school.programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    """
    [1차] 캐시 : 
    DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램 작성

    Args :
    - cacheSize : 0이상 30이하의 정수 
    - cities : 도시 이름으로 이루어진 문자열 배열(list), len(cities) <= 100,000
        각 도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자로 구성, 대소문가 구분 x. 도시 이름은 최대 20자.

    Returns : 입력된 도시 이름 배열을 순서댇로 처리할 때, '총 실행시간' 출력 
    """

    cache = []
    time = 0
    if cacheSize == 0 :
        time = 5 * len(cities)
    else :
        for city in cities:
            city = city.lower()
            if city in cache: # cache hit !! -> time += 1
                time += 1
                if len(cache) == cacheSize :
                    cache.pop(cache.index(city))
                    cache.append(city)
            else : # chche miss -> tmie += 5
                time += 5
                if len(cache) == cacheSize :
                    cache.pop(0)
                    cache.append(city)
                else : 
                    cache.append(city)
    return time

# test case 
# 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) 
# 21
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])) # 21
# 60
print(solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) # 60
# 52
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) # 52
# 16
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"] )) # 16
# 25
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"] )) # 25

# 27 
print(solution(3, ["A", "B", "C", "A", "D", "G", "A"] ))