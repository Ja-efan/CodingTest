
# def solution(s):
#     max_num = 0
#     min_num = int(s[0])
#     for i in range(0,len(s), 2):
#         if int(s[i]) > max_num:
#             max_num = int(s[i])
#         if int(s[i]) < min_num:
#             min_num = int(s[i])

#     return str(min_num) + ' ' + str(max_num)

def solution(s):
    
    arr = s.split(' ')

    max_num = max(arr)
    min_num = min(arr)
    return str(min_num) + " " + str(max_num)

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))