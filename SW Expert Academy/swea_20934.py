# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AY9QTGqqcckDFAVF&categoryId=AY9QTGqqcckDFAVF&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 20934. 방울 마술
# D3

def solution():
    """
    '컵을 한 번 섞는다.' -> 인접한 두 컵의 위치를 교환 한다.
    동전 앞면 : 왼쪽 컵 <-> 가운데 컵
    동전 뒷면 : 오른쪽 컵 <-> 가운데 컵
    컵을 섞을 때 방울이 한 번 울림.
    방울이 K번 울렸다.
    현재 방울이 있을 확률이 가장 높은 컵의 위치는? (여러 개 있다면 가장 왼쪽 위치)
    """
    t = int(input())
    for tc in range(1, t+1):
        base, k = input().split()
        k = int(k)
        base = [i for i in base]
        bell_pos = base.index('o') # 현재 방울 위치
        # print(k)
        # print(base)
        # print(bell_pos)
        if k == 0 :
            print(f"#{tc} {bell_pos}")
            continue
        elif bell_pos == 1:
            if k % 2 == 0 :
                bell_pos = 1
            else :
                bell_pos = 0
        else:
            if k % 2 == 0: # k is even.
                bell_pos = 0
            else :
                bell_pos = 1
        print(f"#{tc} {bell_pos}")
solution()