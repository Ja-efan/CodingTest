# https://www.acmicpc.net/problem/5073
# 삼각형과 세 변
# Bronze III

def solution():
    while True:
        nums = list(map(int, input().split()))
        if nums[0] == nums[1] == nums[2] == 0 :
            break
        
        nums.sort()

        if nums[2] >= nums[0] + nums[1]:
            print("Invalid") 
        elif nums[0] == nums[1] == nums[2]:
            print("Equilateral")
        elif nums[0] == nums[1] or nums[0] == nums[1] or nums[1] == nums[2]:
            print("Isosceles")
        elif nums[0] != nums[1] != nums[2]:
            print("Scalene")

solution()
        