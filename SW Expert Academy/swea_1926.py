# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PTeo6AHUDFAUq&categoryId=AV5PTeo6AHUDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1
# 간단한 369게임
# D2

def solution():
    n = int(input())  # 사용자 입력
    clap = ['3', '6', '9']  # 박수 칠 숫자 들
    result = []  # 출력 결과 저장 리스트

    for i in range(1, n+1):
        s = str(i)  # 정수 i를 문자열로 변환
        cnt = 0  # 3,6,9 가 들어 가는 횟수
        for j in range(len(s)):  # 문자열 s의 길이만큼 반복
            if s[j] in clap:  # s에 3/6/9 가 존재하는 경우
                cnt += 1  # cnt + 1

        if cnt == 0:  # i에 3/6/9가 존재하지 않는 경우
            result.append(i)  # i 그대로 결과 리스트에 저장
        else:  # i에 3/6/9가 하나라도 존재하는 경우
            result.append('-'*cnt)  # 3/6/9가 존재하는 횟수만큼 '-'를 결과 리스트에 저장
    print(*result, sep=" ")  # 결과 저장 리스트를 한줄로 출력, 구분자는 공백


solution()  # 함수 실행