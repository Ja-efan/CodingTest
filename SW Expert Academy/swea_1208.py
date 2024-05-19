# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# Flatten
# D3

def solution():
    t = 10
    for tc in range(1, t+1):
        dumps = int(input())
        boxes = list(map(int, input().split()))

        if max(boxes) - min(boxes) <= 1:
            print(f"#{tc} {max(boxes) - min(boxes)}")
            continue
        # diff = 100
        while dumps:
            if max(boxes) - min(boxes) <= 1:
                print(f"#{tc} {max(boxes) - min(boxes)}")
                break
            max_idx = boxes.index(max(boxes))
            min_idx = boxes.index(min(boxes))
            boxes[max_idx] -= 1
            boxes[min_idx] += 1

            dumps -= 1
        print(f"#{tc} {max(boxes) - min(boxes)}")


solution()