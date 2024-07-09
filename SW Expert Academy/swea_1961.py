# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZBIg6i6E1gDFAUu&contestProbId=AV5Pq-OKAVYDFAUq&probBoxId=AZBNDpl6hGQDFAUu&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+Track+%28%EB%82%9C%EC%9D%B4%EB%8F%84+%EC%A4%91%29&problemBoxCnt=3
# 숫자 배열 회전
# D2
# SSAFY 12기 사전학습 

def solution():
    T = int(input())

    for tc in range(1, T+1):
        N = int(input())
        grid = []
        def is_able(y,x):
            if 0 <= y and y < N and 0 <= x and x < N : return True
            return False 
        

        for _ in range(N):
            grid.append(list(map(int, input().split())))

        result = []
        # 90도 회전 
        result.append(turn_90(grid, N))

        # 180도 회전
        result.append(turn_90(result[-1], N))
        
        # 270도 회전
        result.append(turn_90(result[-1], N))

        # 출력 구문 
        print_result = [[] for _ in range(N)]
        for res in result:
            for i in range(N):
                print_result[i].append("".join(res[i]))
        
        print(f"#{tc}")
        for p_res in print_result:
            print(" ".join(p_res))

            
def turn_90(matrix:list, N:int)->list:
    """
    NxN 행렬에서 i번째 행은 N-i번째 열로 이동한다. 
    ex) [[1,2,3], [4,5,6], [7,8,9]]에서 90도 회전을 하게 되면 
        [[7,4,1], [7,5,2], [9,6,3]]이 된다.
    
    """
    
    result = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            new_i = j
            new_j = (N-1) - i
            result[new_i][new_j] = str(matrix[i][j])
    
    # print(matrix)
    # print(result)

    return result 


# # turn_90() test case 
# turn_90([[1,2,3], [4,5,6], [7,8,9]], 3)
# turn_90([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]], 4)


solution()