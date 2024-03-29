# 147354
# https://school.programmers.co.kr/learn/courses/30/lessons/147354
# Hash

def cal_si(i:int ,data:list) -> int:
    si = 0
    for val in data:
        si += (val % i)
    return si



def solution(data, col, row_begin, row_end):
    """
    테이블 해시 함수 : 
    주어진 테이블(data)에 대한 해시 값을 계산하여 반환한다.

    테이블 해시 함수 정의 
        1. 해시 함수는 col, row_begin, row_end를 입력으로 받는다.
        2. 데이터의 튜플을 col번째 컬럼의 값을 기준으로 오름차순 정렬을 하되, 만약 그 값이 동일하면 기본키인 첫 번재 컬럼의 값을 기준으로 내림차순 정렬한다.
        3. 정렬된 데이터에서 S_i를 i번째 행의 튜플에 대해 각 컬럼의 값을 i로 나눈 나머지들의 합으로 정의한다.
        4. row_begin <= i <= row_end를 만족하는 모든 S_i를 누적하여 bitwise XOR 한 값을 해시 값으로서 반환한다.

    Args : 
    - data 
    - col
    - row_begin
    - row_end

    Returns : hash of table(data)
    """
    
    # # 기본키(첫 컬럼)를 key로, row를 value로 하는 딕셔너리
    # # -> row[0] : row
    # _dict = {
    #     row[0] : row for row in data 
    # }

    rows = sorted(data, key=lambda x:(x[col-1], -x[0])) # 꼭 dict로 만들지 않았어도 될 것 같다.

    # col번째 컬럼 값 기준 오름차순 정렬, 값이 같다면 기본키 값 기준 내림차순 정렬 -> 딕셔너리 다중조건 정렬
    # _dict = dict(sorted(_dict.items(), key = lambda x : ( x[1][col-1], -x[0] )))
    # print(_dict)

    # rows = list(_dict.values())
    # print(rows)
    sis = []
    for i in range(row_begin-1, row_end):
        # print(i)
        si = cal_si(i+1, rows[i])
        sis.append(si)

    answer = sis[0]
    for si in sis[1:]:
        answer = answer^si

    return answer
    # print(sis)
        


# test case
# print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3))

    

