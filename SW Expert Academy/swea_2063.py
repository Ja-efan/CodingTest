# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZBIg6i6E1gDFAUu&contestProbId=AV5QPsXKA2UDFAUq&probBoxId=AZBNDpl6hGUDFAUu&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+Track+%28%EB%82%9C%EC%9D%B4%EB%8F%84+%ED%95%98%29&problemBoxCnt=3
# 중간값 찾기
# D1
# SSAFY 12기 사전학습 (난이도 하)

def solution():
    N = int(input())

    nums = list(map(int, input().split()))

    nums.sort()

    print(nums[N//2])

solution()