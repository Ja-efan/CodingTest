H, M= map(int,input().split())

if H>0 :
    result = (H*60+M)-45
else:
    result = (24*60+M)-45

H = result//60
M = result%60
print(H , M)

# 입력값 0 45 ~ 0 59 까지 출력이 틀림
