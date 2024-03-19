# for i in range(1,11):
#     total = 0 
#     while total < 20:
#         total += i
#         print(f"{total} += {i}") 
#         if total == 20:
#             break
#         i += 1


n = 15
answer = 1
for i in range(1, n//2+1):
    print('-' * 20)
    total = 0
    for j in range(i, n//2+2):
        print(f'j : {j}')
        total += j
        print(f'total {total}')
        if total == n :
            answer += 1
            print('ckeck')
            break
        elif total > n : 
            break
    

print(f'answer : {answer}')