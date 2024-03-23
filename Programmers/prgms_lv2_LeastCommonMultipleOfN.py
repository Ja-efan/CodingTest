# 12953

def solution(arr:list) -> int:
    """
    N개의 최소 공배수 

    Args : 
    - arr : n개의 숫자를 담은 리스트 (길이는 1이상, 15이하이며 원소는 100이하인 자연수)

    Returns : arr원소들의 최소 공배수 
    """
    arr = sorted(arr)
    max_arr = arr[-1]
    len_arr = len(arr)
    lcs =  max_arr
    count_mod_eq_zero  = 0
    # multiplier = 1
    while count_mod_eq_zero != len_arr : 
        for i in arr:
            if lcs % i == 0:
                count_mod_eq_zero += 1
            else : 
                # multiplier += 1
                lcs += max_arr
                count_mod_eq_zero = 0
                break
    

    return lcs


# test case 

print(solution([2,6,8,14]))
print(solution([1,2,3]))

