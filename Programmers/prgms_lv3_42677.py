# https://school.programmers.co.kr/learn/courses/30/lessons/42627
# 디스크 컨트롤러

def solution(jobs:list) -> int :
    import heapq as hq
    hq.heapify(jobs)
    len_ = len(jobs)
    time = 0 
    print(jobs)
    queue = []
    while jobs :
        # 맨 처음 작업은 가장 먼저 도착한 작업이 수행 됨.
        # 동시에 도착한 작업이 여러개인 경우 수행 시간이 짧은 것 부터 수행 됨.
        # if time == 0 :
        #     request_time, required_time = hq.heappop(jobs)
        #     time = request_time + required_time
        # # 현 시점 (time)에 요청되어 있는 작업들을 수행 시간이 짧은 순서대로 heap에 저장
        # else : 
        #     a,b = hq.heappop(jobs)
        #     while time >= a :
        #         hq.heappush(queue, [b,a])
        #         a,b = hq.heappop(jobs)

            
        #     print(queue)
        if time == 0 :
            request_time, required_time = hq.heappop(jobs)
            time += required_time
        a, b = hq.heappop(jobs)
        while time >= a :
            hq.heappush(queue, [b,a])
            if not jobs or jobs[0][0] > time :
                break
        request_time, required_time = hq.heappop(queue)
        time += (time - request_time) + required_time

    print(time)
    print(time // len_)
        

        





# test case 
print(solution([[7, 8], [3, 5], [9, 6]])) # 9
print(solution([[0, 3], [1, 9], [2, 6]])) # 9

# import heapq as hq
# a = [[0, 3], [1, 9], [4, 6]]
# hq.heapify(a)
# print((hq.heappop(a)[1]))