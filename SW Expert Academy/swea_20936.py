# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AY9QUhl6cfQDFAVF&categoryId=AY9QUhl6cfQDFAVF&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 상자 정렬하기
# D4

def solution_20936():
    t = int(input()) # a number of test cases
    test_case = []
    for i in range(1,t+1):
        n = int(input())
        boxes = list(map(int, input().split()))
        boxes.append(0) # 빈 칸 추가
        test_case.append(boxes)
        
    for boxes in test_case:
        k = 0
        result = []
        E = n
        breaker = False
        while k <= 1500 : # 최대 작업 횟수 1500
            if E == n :
                for i in range(len(boxes)):
                    if i+1 != boxes[i]:
                        break
                    breaker = True
                if breaker == True:
                    break
                max_idx = boxes.index(n)
                boxes[E] = n
                boxes[max_idx] = 0
                result.append(max_idx+1)
                k += 1
                E = max_idx
            elif E == 0 :
                min_idx = boxes.index(1)
                boxes[E] = 1
                boxes[min_idx] = 0
                result.append(min_idx+1)
                k += 1
                E = min_idx
            else :
                left_max = max(boxes[:E])
                right_min = min(boxes[E+1:])
                if left_max > right_min:
                    max_idx = boxes.index(left_max)
                    boxes[E] = left_max
                    boxes[max_idx] = 0
                    result.append(max_idx+1)
                    k += 1
                    E = max_idx
                elif left_max < right_min:
                    min_idx = boxes.index(right_min)
                    boxes[E] = right_min
                    boxes[min_idx] = 0
                    result.append(min_idx+1)
                    k += 1
                    E = min_idx

        print(k)
        if result :
            print(*result, sep=" ")
        else :
            print()

def solution_20936_2():
    t = int(input())
    for tc in range(1, t+1):
        N = int(input())
        boxes = list(map(int, input().split()))
        # pos = [i for i in boxes] # position list
        # pos.append(N+1)
        boxes.append(N+1)
        E = N # empty position
        cnt = 0
        result = []
        for i in range(1, N+1):
            while boxes[i-1] != i:
                if E != i-1:
                    # 1. i-1번째 숫자(boxes[i-1])를 빈 칸으로 이동
                    boxes[E] = boxes[i-1]
                    result.append(i)
                # 2. 숫자 i를 i-1번 칸으로 이동
                i_idx = boxes.index(i)
                boxes[i-1] = boxes[i_idx]
                cnt += 1
                result.append(i_idx+1)
                # 3. 숫자 i가 있던 칸을 빈 곳으로 지정
                E = i_idx
                boxes[i_idx] = N+1

        print(cnt)
        print(*result, sep=" ")


def solution_3():


solution_3()





