from jamodict import *

HANTOENG = {
    'ㅁ':'a',
    'ㅠ':'b',
    'ㅊ':'c',
    'ㅇ':'d',
    'ㄷ':'e',
    'ㄸ':'E',
    'ㄹ':'f',
    'ㅎ':'g',
    'ㅗ':'h',
    'ㅑ':'i',
    'ㅓ':'j',
    'ㅏ':'k',
    'ㅣ':'l',
    'ㅡ':'m',
    'ㅜ':'n',
    'ㅐ':'o',
    'ㅒ':'O',
    'ㅔ':'p',
    'ㅖ':'P',
    'ㅂ':'q',
    'ㅃ':'Q',
    'ㄱ':'r',
    'ㄲ':'R',
    'ㄴ':'s',
    'ㅅ':'t',
    'ㅆ':'T',
    'ㅕ':'u',
    'ㅍ':'v',
    'ㅈ':'w',
    'ㅉ':'W',
    'ㅌ':'x',
    'ㅛ':'y',
    'ㅋ':'z'
    }

DOUBLE_CHAR = {
    'ㄳ': ['ㄱ','ㅅ'],
    'ㄵ': ['ㄴ','ㅈ'],
    'ㄶ': ['ㄴ','ㅎ'],
    'ㄺ': ['ㄹ','ㄱ'],
    'ㄻ': ['ㄹ','ㅁ'],
    'ㄼ': ['ㄹ','ㅂ'],
    'ㄽ': ['ㄹ','ㅅ'],
    'ㄾ': ['ㄹ','ㅌ'],
    'ㄿ': ['ㄹ','ㅍ'],
    'ㅀ': ['ㄹ','ㅎ'],
    'ㅄ': ['ㅂ','ㅅ'],
    'ㅘ': ['ㅗ','ㅏ'],
    'ㅙ': ['ㅗ','ㅐ'],
    'ㅚ': ['ㅗ','ㅣ'],
    'ㅝ': ['ㅜ','ㅓ'],
    'ㅞ': ['ㅜ','ㅔ'],
    'ㅟ': ['ㅜ','ㅣ'],
    'ㅢ': ['ㅡ','ㅣ'],
}

word = "줡"
print(ord(word))

result = []
for char in list(word):
    if "가" <= char <= "힣":
        ch1 = (ord(char) - BASE_CODE) // CHOSUNG
        ch2 = (ord(char) - BASE_CODE - CHOSUNG*ch1) // JUNGSUNG
        ch3 = (ord(char) - BASE_CODE - CHOSUNG*ch1 - JUNGSUNG*ch2)
        
        result.append(CHOSUNG_LIST[ch1])
        result.append(JUNGSUNG_LIST[ch2])
        result.append(JONGSUNG_LIST[ch3])
    else:
        result.append(char)


result2 = []
for ch in result:
    if ch:
        if ch in DOUBLE_CHAR:
            for v in DOUBLE_CHAR[ch]:
                result2.append(v)
        else:
            result2.append(ch)
print(''.join(result2))

result3 = []
for ch in result2:
    result3.append(HANTOENG[ch])

print(''.join(result3))