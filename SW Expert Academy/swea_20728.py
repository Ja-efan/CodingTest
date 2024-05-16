# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&problemLevel=4&contestProbId=AY6cg0MKeVkDFAXt&categoryId=AY6cg0MKeVkDFAXt&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1
# 공평한 분배 2
# D3

def solution_20728():
    t = int(input())  # 사용자 입력
    for tc in range(1, t+1):  # 각 테스트 케이스
        n, k = map(int, input().split())  # 사용자 입력 n:주머니 개수, k:나눠 줄 주머니 개수
        candies = list(map(int, input().split()))  # 주머니 속 사탕 개수를 나타내는 n개의 정수
        candies = sorted(candies, reverse=True)  # 내림차순 정렬
        diff_list = []  # 차이를 담을 리스트
        for i in range(0,n-k+1):  # 0번 idx부터 n-k번 idx까지 반복
            max_candies = candies[i:i+k][0]  # [i:i+k] 중 가장 큰 값
            min_candies = candies[i:i+k][-1]  # [i:i+k] 중 가장 작은 값
            diff_list.append(max_candies-min_candies)  # 가장 큰 값과 가장 작은 값의 차이
        
        print(f"#{tc} {min(diff_list)}")  # 차이의 최솟값을 출력


solution_20728()