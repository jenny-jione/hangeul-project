from jamodict import *
import random

word = WORDEX
R2 = 2
R3 = 1
new_word = ""


def get_new_idx(idx, li, r):
    start = idx - r if idx - r >= 0 else 0
    end = idx + r if idx + r < len(li) else len(li) - 1
    new_idx = random.randint(start, end)
    return new_idx
    

for char in list(word):
    if "가" <= char <= "힣":
        ch1 = (ord(char) - BASE_CODE) // CHOSUNG
        ch2 = (ord(char) - BASE_CODE - CHOSUNG * ch1) // JUNGSUNG
        ch3 = (ord(char) - BASE_CODE - CHOSUNG * ch1 - JUNGSUNG * ch2)
        
        char1 = CHOSUNG_LIST[ch1]
        
        if ch1 in [0, 3, 7, 9, 12]:
            ch1 += 1
            
        newch2 = get_new_idx(ch2, JUNGSUNG_LIST, R2)
        newch3 = get_new_idx(ch3, JONGSUNG_LIST, R3)
        newch3 = ch3
        new_word += chr(BASE_CODE + ch1*CHOSUNG + newch2*JUNGSUNG + newch3)
    else:
        new_word += char

print(new_word)
