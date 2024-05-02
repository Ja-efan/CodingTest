# 12939
# https://school.programmers.co.kr/learn/courses/30/lessons/12939
# 최댓값과 최솟값

def solution(s):
    nums = list(map(int, s.split(" ")))
    # print(nums)
    minn = min(nums)
    maxx = max(nums)
    answer = str(minn) + " " + str(maxx)
    return answer 

# test case
print(solution("1 2 3 4")) # "1 4"
print(solution("-1 -2 -3 -4")) # "-4 -1"
print(solution("-1 -1")) # "-1-1"