

def solution(A, B):
    """
    Args :
    - A : list of natural numbers
    - B : list of natural numbers 

    Returns : int 
    ##################################

    A의 최솟값과 B의 최댓값을 곱해서 더한다.
    한 번 곱해진 수는 리스트에서 제거
    """
    answer = 0
    length =  len(A)
    A = sorted(A, reverse=True)
    B = sorted(B)
    # print(A)
    # print(B)

    # print(A.pop())
    # print(B.pop())
    for i in range(length):
        # min_A = A.pop()
        # max_B = B.pop()
        answer += A.pop() * B.pop()

        # A.remove(min_A)
        # B.remove(max_B)
        # print(answer)   
        # print(A)
        # print(B)

    return answer 

# test case
print(solution([1,4,2], [5,4,4]))