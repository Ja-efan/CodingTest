# 12981

def solution(n, words):
    """
    English Endings : 영어 끝말잇기

    Args : 
    - n : 끝말잇기에 참가하는 사람의 수 , 2<= n <= 10
    - words : 끝말잇기에 사용한 단어들이 순서대로 저장된 리스트, n <= len(words) <= 100

    Returns : 
    - 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는 지 구해서 리스트로 반환 -> [참가자 번호, 탈락 차례]
    """

    user_count = {}
    for i in range(1, n+1): # dictionary 초기화 -> 참가 번호 : 단어 리스트 
        user_count[i] = 0

    used_words = []
    print(used_words)

    for i in range(0, len(words)):
        user = (i+1) % n
        if (i+1) % n == 0:
            user = n
        if words[i] in used_words:
            return [user, user_count[user]+1]
        elif used_words and (used_words[-1][-1] != words[i][0]):
            return [user, user_count[user]+1]
        used_words.append(words[i])
        user_count[user] += 1
        print(used_words)
    return [0,0]
        
print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))