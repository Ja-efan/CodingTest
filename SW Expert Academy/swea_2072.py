# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1&problemLevel=2%2C3&&&&&&&&&
# 홀수만 더하기
# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.

def solution_2072():
    t = int(input()) # a number of test case 
    inputs = []
    for _ in range(t):
        input_ = map(int, input().split(" "))
        inputs.append(input_)
    
    for i,test_case in enumerate(inputs):
        odds = []
        for input_ in test_case:
            if input_ % 2 == 1:
                odds.append(input_)
        
        print(f"#{i+1} {sum(odds)}")


solution_2072()

