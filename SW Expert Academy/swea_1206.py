# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&problemLevel=4&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=1
# [S/W 문제해결 기본] 1일차 - View

def solution_1206():
    
    test_cases = []
    for _ in range(3):
        n = int(input())
        test_cases.append(list(map(int, input().split(" "))))
    
    for i, tc in enumerate(test_cases):
        views = 0
        for j in range(2, len(tc)-2):
            height = tc[j]
            """
            왼쪽(j-2, j-1) 중에 max값 
            오른쪽(j+1, j+2) 중에 max값
            """
            left = max(tc[j-2], tc[j-1])
            right = max(tc[j+1], tc[j+2])
            # 왼쪽 혹은 오른쪽 건물의 높이가 같거나 더 높은 경우 
            if left >= height or right >= height:
                continue
            
            views += height - max(left, right)
        print(f"#{i+1} {views}")


def solution_1206_2(): # n번째 테스트 케이스 출력이 n+1번째 입력으로 들어가서 틀린다.
    # 사용자 입력
    t = int(input())
    for tc in range(1, t+1):
        views = 0
        buildings = list(map(int, input().split()))

        for i in range(2, len(buildings)-2):
            height = buildings[i]
            left = max(buildings[i-2], buildings[i-1])
            right = max(buildings[i+1], buildings[i+2])
            if left >= height or right >= height:
                continue
            views += height - max(left, right)
        print(f"#{tc} {views}")


solution_1206()



            
                
