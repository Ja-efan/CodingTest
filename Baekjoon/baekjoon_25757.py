# https://www.acmicpc.net/problem/25757
# 임스와 함께하는 미니게임 
# Silver V

import sys 

input = sys.stdin.readline

def solution():

    games = {
        'Y' : 2,
        'F' : 3, 
        'O' : 4
    }

    N, game = input().rstrip().split()

    N = int(N)
    guests = set()
    for i in range(N):
        guest = input()
        guests.add(guest)
    
    num_of_guests = len(guests)

    answer = num_of_guests // (games[game]-1)

    print(answer)

solution()