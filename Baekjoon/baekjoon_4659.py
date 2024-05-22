# https://www.acmicpc.net/problem/4659
# 비밀번호 발음하기 
# Silver V

from string import ascii_lowercase
import sys

input = sys.stdin.readline

def solution():
    """
    1. 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
    2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안된다.
    3. 같은 글자가 연속적으로 두번 오면 안되나, ee와 oo는 허용한다.
    """


    # lowercase = [i for i in ascii_lowercase]
    # print(lowercase)

    # 모음과 자음 
    vowels = ['a','e','i','o','u'] 
    consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

    while True:
        pw = input().rstrip()
        if pw == 'end':
            break
        
        # 모음 하나 이상 포함 
        cond1 = False
        for c in pw:
            if c in vowels:
                cond1 = True
                break

        # 모음이 3개 혹은 자음이 3개 연속으로 오면 안됨
        # 3개 연속으로 오는 경우 cond2는 False
        cond2 = True
        c, v = 0, 0
        # pre = ''
        for k in pw:

            if k in vowels:
                # pre = 'v'
                v += 1
                c = 0
            else :
                # pre = 'c'
                c += 1
                v = 0

            if c == 3 or v == 3:
                cond2 = False
                break

        # 같은 글자가 두번 연속으로 오면 안됨. (예외 > ee 와 oo)
        cond3 = True
        for i in range(len(pw)-1):
            if pw[i] == pw[i+1]:
                if pw[i] not in ['e','o']:
                    cond3 = False
                    break
                
        if cond1 and cond2 and cond3:
            print(f"<{pw}> is acceptable.")
        else :
            print(f"<{pw}> is not acceptable.")

    return

        
solution()