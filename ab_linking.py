from jamodict import *

word = WORDEX

def combine_jamo(ch1, ch2, ch3):
    return chr(BASE_CODE + CHOSUNG*ch1 + JUNGSUNG*ch2 + ch3)

new_word = ""
linking_idx = None
for char in list(word):
    if "가" <= char <= "힣":
        ch1 = (ord(char) - BASE_CODE) // CHOSUNG
        ch2 = (ord(char) - BASE_CODE - CHOSUNG*ch1) // JUNGSUNG
        ch3 = (ord(char) - BASE_CODE - CHOSUNG*ch1 - JUNGSUNG*ch2)
        
        if ch1 == 11 and linking_idx!=None and prev_ch3!=21:
            print("linking?")
            print("prev:", combine_jamo(prev_ch1, prev_ch2, prev_ch3))
            print("curr:", combine_jamo(linking_idx, ch2, ch3))
            print(new_word[-1])
            ############# here
        
        
        new_word += combine_jamo(ch1, ch2, ch3)
        
        char1 = CHOSUNG_LIST[ch1]
        char2 = JUNGSUNG_LIST[ch2]
        char3 = JONGSUNG_LIST[ch3]
        
        prev_ch1, prev_ch2, prev_ch3 = ch1, ch2, ch3
        if char3 in CHOSUNG_LIST:
            linking_idx = CHOSUNG_LIST.index(char3)
            prev_ch3 = 0
        elif char3 in DOUBLE_CHAR:
            if char3 == "ㄶ":
                linking_idx = CHOSUNG_LIST.index(DOUBLE_CHAR[char3][0])
                prev_ch3 = 0
            else:
                linking_idx = CHOSUNG_LIST.index(DOUBLE_CHAR[char3][1])
                prev_ch3 = JONGSUNG_LIST.index(DOUBLE_CHAR[char3][0])
        else:
            linking_idx = None
        
    else:
        new_word += char
        linking_idx = None
    
        
print(new_word)