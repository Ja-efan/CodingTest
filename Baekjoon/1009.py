# https://www.acmicpc.net/problem/1009
# 분산처리 
# Bronze II

def distribution() : 
    """
    user input : 
    - t : 테스트 케이스의 개수 
    - 테스트 케이스에 대한 정수 a와 b (1 <= a < 100, 1 <= b < 1,000,000)
    """
    test_case = []
    t = int(input())
    for _ in range(t):
        a,b = map(int, input().split(' '))
        test_case.append((a,b))
    ones_dict = {
        1 : [1],
        2 : [2,4,8,6],
        3 : [3,9,7,1],
        4 : [4,6],
        5 : [5],
        6 : [6],
        7 : [7,9,3,1],
        8 : [8,4,2,6],
        9 : [9,1]
    }

    for ab in test_case :
        a,b = ab
        if a % 10 == 0 :
            print(10)
        else :
            ones = ones_dict[a%10]
            print(ones[(b % len(ones))-1])

distribution()