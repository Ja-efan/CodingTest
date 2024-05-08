# https://school.programmers.co.kr/learn/courses/30/lessons/42626
# 더 맵게
import heapq

def solution(scoville:list, k:int) -> int :
    heapq.heapify(scoville)
    count = 0
    while len(scoville) >= 2:
        min_ = heapq.heappop(scoville)
        if min_ >= k :
            return count
        else :
            min_2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min_ + min_2*2)
            count += 1
        # print(scoville)
    if scoville[0] >= k :
        return count 
    else :
        return -1
# test case 
print(solution([1, 2, 3, 9, 10, 12],7)) # 2
print(solution([1,1,1,1,1], 20))