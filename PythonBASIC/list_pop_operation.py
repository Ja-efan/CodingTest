import time

# 리스트 생성
n = 1000000
test_list = list(range(n))

# pop(0) 시간 측정
start_time = time.time()
test_list.pop(0)
pop_0_time = time.time() - start_time

# pop() 시간 측정
test_list = list(range(n))
start_time = time.time()
test_list.pop()
pop_time = time.time() - start_time

print(pop_0_time, pop_time)