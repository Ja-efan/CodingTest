# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AYo-e9EKmGoDFAQI&categoryId=AYo-e9EKmGoDFAQI&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 등차수열 만들기
# D3

def solution():
    t = int(input())
    for tc in range(1, t+1):
        # answer = 0
        nums = list(map(int, input().split()))
        if 2*nums[1] == nums[0] + nums[2]:
            print(f"#{tc} {0.0}")
        elif 2*nums[1] > nums[0] + nums[2]:
            result = round((2*nums[1] - (nums[0] + nums[2])) / 2, 1)
            print(f"#{tc} {result}")
        elif 2*nums[1] < nums[0] + nums[2]:
            result = round((nums[0] + nums[2] - (2*nums[1]))/2, 1)
            print(f"#{tc} {result}")


solution()
