"""
A와 B로 이루어진 길이 N 문자열
B는 두번만 등장
사전 배열 (내림차순)
K 번째 문자열의 2번째 B위치
2진수로 출력
- 'A'를 N-2개 셋팅
-
"""

from itertools import combinations
def solution(n, k):
    # position of 'B'
    b_poses = list(combinations(range(n), 2))
    string_list = []
    while b_poses:
        b_pos = b_poses.pop()
        s = ['A' for _ in range(n-1)]
        s.insert(b_pos[0], 'B')
        s.insert(b_pos[1], 'B')
        s = "".join(s)
        string_list.append(s)

    string_list.sort()

    kth_string = string_list[k-1]
    first_b_index = kth_string.index('B')
    second_b_index = kth_string.index('B', first_b_index+1)
    answer = []
    while second_b_index:
        answer.append(second_b_index % 2)
        second_b_index = second_b_index // 2
    answer = answer[::-1]

    print(answer)




solution(10,23)




