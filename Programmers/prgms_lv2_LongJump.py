# 12914 

def solution(n:int) -> int :
    """
    멀리 뛰기 :
    효진이는 한번에 1칸 또는 2칸을 뛸 수 있다. 

    Args :
    - n : 효진이가 멀리뛰기에 사용될 칸의 수 (1<= n <= 2,000) 

    Returns : 끝에 도달하는 방법의 가짓수를 123434567로 나눈 나머지
    """
    one = 0
    two = 0

    solution_list =  []

    for i in range(n):
        if i == 0:
            solution_list.append(1)
        elif i == 1:
            solution_list.append(2)
        else :
            solution_list.append(solution_list[i-1] + solution_list[i-2])
    
    return solution_list[-1]%1234567


# test case
print(solution(4))
print(solution(3))