# 42579 
# https://school.programmers.co.kr/learn/courses/30/lessons/42579
# Hash

def solution(genres:list, plays:list) -> list:
    """
    베스트앨범 : 
    장르 별 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 한다. 
    베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 반환.
    수록 기준 
        1. 속한 노래가 많이 재생된 장르를 먼저 수록한다.
        2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.
        3. 장르 내에서 재생 횟수가 같은 노래중에서는 고유 번호가 낮은 노래를 먼저 수록한다.
    
    Args :
    - genres : 노래의 장르를 나타내는 문자열 배열(list)
               i번째 인덱스에는 고유번호가 i인 노래의 장르

    - plays : 노래별 재생 횟수를 나타내는 정수 배열(list)
              i번째 인덱스에는 고유번호가 i인 노래의 재생 횟수

        genres와 plays의 길이는 같다. (1이상 10,000이하)
        장루 종류는 100개 미만
        장로에 속한 곡이 하나라면, 하나의 곡만 선택
        모든 장르는 재생된 횟수가 다름
    """

    # solution 1 : 53.3 / 100
    # 53.3 나오던 이유
    # -> 59번째 줄에 answer.append(index_of_songs[:1])로 되어 있어서 list가 append 됨.
    # -> 장르에 속한 노래가 하나인 경우, 모두 list로 answer에 append.

    # dict_genres -> genre : [노래 개수, {노래 고유번호 : 재생 횟수}] 를 담는 Dictionary
    dict_genres = {
        genre : [0, {}] for genre in genres
    }

    # print(dict_genres)

    for i, (genre, play) in enumerate(zip(genres, plays)):
        dict_genres[genre][0] += play
        dict_genres[genre][1][i] = play
        
    
    dict_genres = dict(sorted(dict_genres.items(), key=lambda x:x[1][0], reverse=True)) # dict_genres의 items를 정렬, 정렬 기준은 dict_genres[1][0] -> 장르별 재생 횟수, 내림차순 = True

    print(dict_genres)

    # 각 장르마다 노래 재생 횟수에 따라 노래 고유번호 정렬 (내림차순)
    for key in dict_genres.keys():
        dict_genres[key][1] = dict(sorted(dict_genres[key][1].items(), key=lambda x:x[1], reverse=True))

    print(dict_genres)

    answer = []

    for value in dict_genres.values():
        index_of_songs = list(value[1].keys())
        if len(index_of_songs) < 2:
            answer.append(index_of_songs[0]) 
        else : 
            answer.append(index_of_songs[0])
            answer.append(index_of_songs[1])

    return answer





# test case
print(solution(["classic", "pop","pop","classic", "classic", "pop","ballad", "pop"],[500, 600, 600, 150, 8000, 3000,2500, 600] ))
        

