import sys


list_n = int(input())

list = list(map(int, input().split()))

find_n = int(input())

n = list.count(find_n)

print(n) 