# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZBIg6i6E1gDFAUu&contestProbId=AV5PpoFaAS4DFAUq&probBoxId=AZBNDpl6hGQDFAUu&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+Track+%28%EB%82%9C%EC%9D%B4%EB%8F%84+%EC%A4%91%29&problemBoxCnt=3
# 두 개의 숫자열
# D2
# SSAFY 12기 사전학습

def solution():
    T = int(input())

    for tc in range(1 ,T+1):
        N, M = map(int, input().split())

        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        
        len_A = len(A)
        len_B = len(B)

        if len_A > len_B:
            tmp = A
            A = B
            B = tmp 
            tmp = N
            N = M
            M = tmp
        
        result = 0

        for i in range(M):
            if i + N > M :
                break
            sum_ = 0
            for j in range(N):
                sum_ += A[j]*B[i+j]
            
            if result < sum_:
                result = sum_
        
        print(f"#{tc} {result}")


solution()