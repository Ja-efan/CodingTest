# https://www.acmicpc.net/problem/20006
# 랭킹전 대기열
# Silver II

import sys
from collections import deque

# fast io 
inputf = sys.stdin.readline
printf = sys.stdout.write

def matching(player:tuple, rooms:dict, max_players:int) -> dict:

    """
    플레이어 정보(player)와 현재 방 상태(rooms)를 받아 플레이어 입장 후의 방 상태를 반환
    - [x] 가장 처음 입장한 플레이어
    - [x] 입장 가능한 방이 없는 경우 
    - [x] 입장 가능한 경우 
    - [x] 입장 가능한 방이 여러 개인 경우
    """

    p_lv = player[0]
    p_nickname = player[1]
    
    num_of_rooms = len(list(rooms.keys()))

    rooms = dict(sorted(rooms.items(), key=lambda x:x[0]))

    # 입장 가능한 경우, 입장 가능한 방이 여러 개인 경우 
    for room_id, room_info in rooms.items():
        min_lv = room_info[0][0]
        max_lv = room_info[0][1] 
        players_of_room = room_info[1]
     
        if min_lv <= p_lv and p_lv <= max_lv:
            if len(players_of_room) < max_players:
                room_info[1].append((p_lv, p_nickname))
                return rooms
        
    
    # 입장 가능한 방이 없는 경우 
    rooms[num_of_rooms+1] = [(p_lv-10, p_lv+10), [(p_lv, p_nickname)]]
    return rooms


def solution():
    # p : 플레이어의 수, m : 방 한개의 정원
    p, m = map(int, inputf().split())
    
    players = []  # 전체 플레이어의 정보(레벨, 닉네임)을 입장 순서대로 저장하는 리스트 
    for _ in range(p):
        # l : 플레이어의 레벨 , n : 플레이어의 닉네임 
        l, n = inputf().rstrip().split()
        players.append((int(l), n))

        """
        매칭 시스템 :
        1. 입장 시점 매칭 가능한 방이 없다면 새로운 방을 생성하고 입장. 
           이때, 해당 방에는 처음 입장한 플레이어의 레벨을 기준으로 [-10, 10]까지 입장 가능하다.
        2. 입장 가능한 방이 있다면 입장시킨 후 정원이 모두 찰 때까지 대기시킨다.
            - 이때 입장 가능한 방이 여러 개라면 먼저 생성된 방에 입장한다.
        3. 방의 정원이 모두 차면 게임을 시작한다.
        """

    rooms = dict()  # {room_id : [(min_lv, max_lv), [nickname of players]]}
    players = deque(players)  # popleft() 연산을 위해 deque 변환
    while players:
        player = players.popleft()
        rooms = matching(player=player, rooms=rooms, max_players=m)
        
    for rid, rinfo in rooms.items():
        players_of_room = rinfo[1]
        players_of_room = sorted(players_of_room, key=lambda x:x[1]) 

        if len(players_of_room) == m :
            printf("Started!\n")
        else:
            printf("Waiting!\n")

        for player in players_of_room:
                printf("{} {}\n".format(player[0], player[1]))

                
solution()