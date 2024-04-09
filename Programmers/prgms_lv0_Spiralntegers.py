# 181832
# https://school.programmers.co.kr/learn/courses/30/lessons/181832

def rotate_matrix(matrix:list)-> list: 
    """
    인자로 받은 2차원 행렬을 반시계 방향으로 회전 시켜 반환
    """
    rotate = []
    for i in range(len(matrix[0])):
        tmp = []
        for j in range(len(matrix[1])):
            tmp.append(matrix[j][i])
        rotate.insert(0,tmp)
    # print(rotate)
    return rotate


def solution(n:int)->list:
    """
    정수를 나선형으로 배치하기 :
    양의 정수 n이 매개변수로 주어진다.
    nxn배열에 1부터 n^2까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 반환

    Args :
    - n : 1이상 30이하 정수 
    
    Returns : 2차원 배열 (list)
    """

    # 행렬을 반시계로 돌리면서 값을 채워넣는다?
    v = 1
    # 0으로 채워진 n x n matrix
    matrix = [[0 for i in range(n)] for j in range(n)]

    col_direction = [0,1,0,-1] 
    row_direction = [1,0,-1,0] 
    turn = 0 # 몇 번째 turn인지 표시 
    col = 0
    row = 0

    for i in range(n**2):
        print(col, row)
        matrix[col][row] = v
        v+= 1
        next_col = col + col_direction[turn%4]
        next_row = row + row_direction[turn%4]

        if next_col == n or next_col < 0 or next_row == n or next_row < 0 or matrix[next_col][next_row] != 0 :
            turn += 1
            col = col + col_direction[turn%4]
            row = row + row_direction[turn%4]
        else : 
            col = next_col
            row = next_row
    
        
    return matrix




print(solution(3))