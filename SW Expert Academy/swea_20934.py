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
        bell_pos = base.index('o')  # 현재 방울 위치

        if k == 0:  # 방울 소리가 들리지 않음 -> 이동 x
            print(f"#{tc} {bell_pos}")
            continue
        elif bell_pos == 1:  # 초기 위치가 가운데 컵인 경우
            if k % 2 == 0:  # 방울이 짝수번 울리면 제자리(가운데)로 돌아옴
                bell_pos = 1
            else:  # 방울이 홀수번 울리면 왼쪽 혹은 오른쪽 컵으로 이동, 가장 왼쪽 컵은 왼쪽 컵
                bell_pos = 0
        else:  # 초기 위치가 가운데가 아닌 경우
            if k % 2 == 0:  # 방울이 짝수번 울리면 방울이 제자리로 돌아오거나 반대편 컵에 위치
                bell_pos = 0  # 가장 왼쪽 컵은 왼쪽 컵
            else:  # 방울이 홀수번 울리면 가운데 컵에 위치하게 됨
                bell_pos = 1
        print(f"#{tc} {bell_pos}")


solution()
