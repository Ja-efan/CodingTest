# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1
# 달팽이 숫자

def solution_1954():
    n = int(input()) # a number of test case
    test_case = []
    for _ in range(n):
        test_case.append(int(input()))

    col_direction = [1,0,-1,0]
    row_direction = [0,1,0,-1]

    for i,n in enumerate(test_case):
        col = 0
        row = 0
        rotate = 0
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        for j in range(1, n**2+1):
            matrix[row][col] = j
            next_col = col + col_direction[rotate%4]
            next_row = row + row_direction[rotate%4]

            if next_col == n or next_col < 0 or next_row == n or next_row < 0 or matrix[next_row][next_col]!=0:
                rotate += 1
                col = col + col_direction[rotate%4]
                row = row + row_direction[rotate%4]
            else : 
                col = next_col
                row = next_row
            
        print(f"#{i+1}")
        for nums in matrix:
            for i in nums:
                print(i, end=" ")
            print()
            
solution_1954()