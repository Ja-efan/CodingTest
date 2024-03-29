# 42577
# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# Hash

def solution(phone_book:list) -> bool:

    """
    전화번호 목록 :
    한 번호가 다른 번호의 접두어인 경우가 있는지 확인한다.

    Args :
    - phone_book : 전화번호를 담은 배열(list)

    Returns : 다른 번혼의 접두어인 경우가 있는 경우 False를 없다면 True를 반환
    """

    # # solution 1 
    # # 효율성 3,4번 time out
    # answer = True

    # idx = 0
    # while answer:
    #     if idx == len(phone_book) : break

    #     num = phone_book[idx]
    #     # lenn = len(num)

    #     for i in range(len(phone_book)):
    #         if i == idx : continue
    #         elif len(num) > len(phone_book[i]): continue
    #         else :
    #             comp = phone_book[i]
    #             if num == comp[:len(num)]:
    #                 answer = False
        
    #     idx += 1
        
    # return answer

    # solution 2
    print(phone_book) # before sorting
    phone_book.sort()
    print(phone_book) # after sorting

    answer = True
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]: 
            answer = False
            break
    return answer



# test case
print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","1235","123","567","88"]))
