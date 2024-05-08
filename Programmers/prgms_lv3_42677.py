# https://school.programmers.co.kr/learn/courses/30/lessons/42627
# 디스크 컨트롤러

def solution(jobs:list) -> int :
    import heapq as hq
    hq.heapify(jobs)
    status = 0
    time = 0 
    print(jobs)
    queue = hq.heapify([])
    while jobs :
        if time == 0 :
            request_time, required_time = hq.heappop(jobs)
            time = required_time
        # 현 시점 (time)에 요청되어 있는 작업들 중 작업 소요시간이 가장 짧은 작업을 수행
        else : 
            a,b = hq.heappop(jobs)
            while time >= b :
                hq.heappush(queue, [b,a])
            print(queue)
        





# test case 

print(solution([[0, 3], [1, 9], [4, 6]])) # 9

# import heapq as hq
# a = [[0, 3], [1, 9], [4, 6]]
# hq.heapify(a)
# print((hq.heappop(a)[1]))