# 12911

def int2binary(n:int, return_type='str') :
        
        binary = format(n, 'b')
        if return_type=='str': return binary
        elif return_type=='int' : return int(binary)
        

def solution(n: int) -> int:
    """
    Next Greater Number :
    - 자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의한다.
    - 1. n의 다음 큰 숫자는 n보다 큰 자연수.

    - 2. n의 다음 큰 숫자와 n은 이진수로 변환했을 때 1의 갯수가 같다.
    - 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수이다.

    Args : 
    - n : 1,000,000 이하의 자연수 

    Returns : next greater number of n
    """


    binary_n = int2binary(n, return_type='str')
    length_one = len(binary_n.replace('0', ''))
    # print(binary_n)
    # print(length_one)
    answer = 0
    next_n = n + 1

    while 1:
        binary_next_n = int2binary(next_n)
        if len(binary_next_n.replace('0', '')) == length_one:
            # print(next_n)
            # print(binary_next_n)
            # print(len(binary_n.replace('0', '')))
            answer = next_n
            break
        else : 
             next_n += 1

    return answer 
            

# test case 
print(solution(78))
    
    

