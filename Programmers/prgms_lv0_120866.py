# https://school.programmers.co.kr/learn/courses/30/lessons/120866
# 안전지대
import numpy as np

def solution(board:list) -> int:
    n = len(board)
    new_board = [[0 for _ in range(n)] for _ in range(n)]
    danger = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0), (1,1)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0 :
                continue
            for move in danger:
                k, l = move 
                new_board[i][j] = 1
                if i+k < 0 or i+k > n-1 or j+l < 0 or j+l > n-1 :
                    continue
                new_board[i+k][j+l] = 1
    
    # print(np.stack(new_board, axis=1))
    summ = 0 
    for row in new_board:
        summ += sum(row)
        # print(summ)
    answer =  n**2 - summ
    return answer 

# test case 
# print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])) # 16 
# print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]])) # 13 
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]])) # 0
            
