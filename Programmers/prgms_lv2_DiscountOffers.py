# 131127 
# https://school.programmers.co.kr/learn/courses/30/lessons/131127

def solution(want, number, discount):
    """
    할인 행사 :
    - 일정 금액 지불 시 10일 간의 회원 자격
    - 회원을 대상으로 매일 한 가지 제품을 할인
    - 할인하는 제품은 하루에 하나씩만 구매 가능
    - 정현이는 자신이 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우에 맞춰서 회원가입을 하려고 한다.

    Args :
    - want : 정현이가 원하는 제품을 나타내는 문자열 배열(list)
    - number : 정현이가 원하는 제품의 수량을 나타내는 정수 배열(list), number 원소의 합은 10
    - discount : 마트에서 할인하는 제품을 나타내는 문자열 배열(list)

    Retuns : 회원 등록시 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원 등록 날짜의 총 일수, 가능한 날이 없으면 0을 리턴
    """

    """
    1. 리스트 want의 모든 원소가 리스트 discount에 존재해야 함.
    2.
    """
    answer = 0
    want_number_stack = [] # 원하는 물품들을 원하는 개수만큼 저장해놓은 스택 
    for i in range(len(want)):
        for j in range(0,number[i]):
            want_number_stack.append(want[i])
    # print(want_number_stack)
    want_number_stack = sorted(want_number_stack)
    for i in range(len(discount) - len(want_number_stack)+1):
        new_discount = sorted(discount[i:i+10])
        
        if want_number_stack == new_discount:
            answer += 1
            
    return answer

# test case
print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10],["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"] ))