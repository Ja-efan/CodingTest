# 43162
# https://school.programmers.co.kr/learn/courses/30/lessons/43162
# DFS & BFS

def solution(n:int, computers:list) -> int:
    """
    네트워크 :
    컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 주어질 때, 네트워크의 개수를 반환하는 함수 

    Args :
    - n : 컴퓨터의 개수 
        1<= n <= 200, 각 컴퓨터는 0부터 n-1인 정수로 표현 
    - computers : 연결에 대한 정보가 담긴 2차원 배열
        i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현
        computers[i][i]는 항상 1 
    """

    visited = [False] * n
    # print(visited)    
    answer = 0
    for i in range(n):
        if visited[i]:
            continue
        elif not visited[i]: 
            visited[i] = True
            answer += 1
        queue = [j for j in range(n) if computers[i][j] == 1]
        while queue:
            s = queue.pop(0)
            if i == s :
                continue
            visited[s] = True
            for k in range(n):
                if not visited[k] and computers[s][k] == 1:
                    queue.append(k) 
        
    return answer 


# test case 
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 1
print(solution(1, [[1]])) # 1
print(solution(4, [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]))  #2
print(solution(5, [[1, 0, 0, 0, 1], [0, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [1, 0, 0, 1, 1]])) # 1