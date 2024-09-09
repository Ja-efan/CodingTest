# 숫자 만들기
# 모의 SW 역량테스트

from itertools import permutations


def perm(operators, remain):
    global result_list, min_, max_

    if not remain:
        # 연산자 조합 순열 완성

        tmp_numbers = numbers[::-1]
        operators = list(operators)[::-1]

        tmp_result = tmp_numbers.pop()
        while tmp_numbers:
            a = tmp_numbers.pop()
            # print(tmp_result, a)
            # b = tmp_numbers.pop()
            operator = operators.pop()
            if operator == 0:
                tmp_result += a
            elif operator == 1:
                tmp_result -= a
            elif operator == 2:
                tmp_result *= a
            elif operator == 3:
                tmp_result = int(tmp_result/a)
            # tmp_numbers.append(tmp_result)

        min_ = min(min_, tmp_result)
        max_ = max(max_, tmp_result)

    else:
        for i in range(len(remain)):
            select_i = remain[i]
            remain_list = remain[:i] + remain[i + 1:]
            perm(operators + [select_i], remain_list)


def make_number():
    global result_list, numbers

    N = int(input())
    M = N - 1  # 연산자 개수
    num_of_operators = list(map(int, input().split()))  # 연산자 개수
    numbers = list(map(int, input().split()))  # 숫자 리스트: 피연산자

    operator_list = []
    for i in range(len(num_of_operators)):
        for j in range(num_of_operators[i]):
            operator_list.append(i)

    # operator_perm = list(permutations(operator_list, M))

    perm([], operator_list)
    result_list.sort()


def main():
    global result_list, max_, min_
    T = int(input())
    for tc in range(1, T + 1):
        max_ = -100000000
        min_ = 100000000
        result_list = []
        make_number()
        # print(f"max: {result_list[-1]}, min:{result_list[0]}")
        # diff = result_list[-1] - result_list[0]
        diff = max_ - min_
        print(f"#{tc} {diff}")
    return


if __name__ == "__main__":
    import sys
    sys.stdin = open("./testcases/input_4008.txt")
    max_ = -100000000
    min_ = 100000000
    result_list = []
    numbers = []
    main()
