# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYxCRFA6iiEDFASu&categoryId=AYxCRFA6iiEDFASu&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=2&&&&&&&&&&&&&&&&&&
# 식료품 가게
# D3

def solution():
    t = int(input())
    for tc in range(1, t+1):
        N = int(input())
        product = list(map(int, input().split()))
        product.sort(reverse=True)  # 내림차순으로 정렬 (pop()연산 효율 위해서)
        discount_price = []  # 할인 가격을 담을 리스트
        while product:
            p = product.pop()  # 작은 가격부터 pop
            if int((4*p)/3) in product:  # 정상 가격이 존재한다면
                discount_price.append(p)  # p를 할인 가격 리스트에 추가
                product.pop(product.index(int((4*p)/3)))  # 정상 가격을 리스트에서 제거
        discount_price.sort()  # 할인 가격을 오름차순으로 정렬
        result = ''
        for dp in discount_price:  # 출력 조건에 맞게 변경
            result += str(dp) + " "

        print(f"#{tc} {result}")


solution()