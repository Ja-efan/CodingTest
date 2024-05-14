# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&problemLevel=4&contestProbId=AY6ci8cKecUDFAXt&categoryId=AY6ci8cKecUDFAXt&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1
# 서로소 그리드 
# D4

def solution_20731():

    def gcd(a,b) -> int:
        # 서로소인 경우 1, 아닌 경우 다른 수 반환
        if (a == 0 and b != 0) or (a != 0 and b == 0):
            return 1
        elif a == 0 and b == 0 :
            return 0
        
        for i in range(min(a,b), 0, -1): 
            if a % i == 0 and b % i == 0 : # 
                return i

    t = int(input())
    for tc in range(1, t+1):
        n = int(input())
        grid = []
        for _ in range(n):
            input_ = input()
            grid.append([c for c in input_])
        
        result = 'YES'
        visited = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            breaker = False
            for j in range(n):
                if visited[i][j] == 1 :
                    continue

                if i == j and grid[i][j] == '1': # i == j 인데, 서로소라고 하는 경우 
                    breaker = True
                    # result = "NO"
                    break
                elif gcd(i,j) == 1 and (grid[i][j] == '?' or grid[j][i] == '?'): # 서로소 인데 서로소가 아니라고 하는 경우 
                    breaker = True
                    # breaker = "NO"
                    break
                elif gcd(i,j) != 1 and (grid[i][j] == '1' or grid[j][i] == '1'):
                    breaker = True
                    # breaker = "NO"
                    break
                else :
                    visited[i][j] = 1
                    visited[j][i] = 1

            if breaker == True:
                result = 'NO'
                break
        
        print(f"#{tc} {result}")


solution_20731()