import string
"""
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 
단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다.
"""

def solution(s:str) -> str:
    split_s = s.split(" ")
    print(split_s)
    new_s = []
    for word in split_s:
        if word == "":
            new_s.append("")
            continue
        new_word = ""
        
        if isinstance(word[0], str):
            new_word = new_word + word[0].upper()
        else :
            new_word = new_word + word[0]
        new_word += word[1:].lower()
        new_s.append(new_word)
    answer = " ".join(new_s)
    
    return answer

# print(solution("3people unFollowed me"))

# print(solution("for  the last week"))

print('yes' if " " else " No ")