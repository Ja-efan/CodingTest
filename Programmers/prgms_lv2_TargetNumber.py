# 43165
# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# DFS & BFS

def solution(numbers:list, target:int) -> int:
    """
    타겟 넘버 :

    """
    curr = 0
    idx = 0

    def dfs(nums, target, curr, idx):
        if idx == len(nums) :
            if curr == target:
                return 1
            else : return 0
        return dfs(nums, target, curr+nums[idx], idx+1) \
            + dfs(nums, target, curr-nums[idx], idx+1)
    
    answer = dfs(nums=numbers, target=target, curr=curr, idx=idx)
    return answer 

# test case 
print(solution([1,1,1,1,1] , 3)) # 5
print(solution([4,1,2,1] , 4)) # 2
