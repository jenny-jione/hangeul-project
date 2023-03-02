ENGHAN = {
    'a':'ㅁ',
    'b':'ㅠ',
    'c':'ㅊ',
    'd':'ㅇ',
    'e':'ㄷ',
    'E':'ㄸ',
    'f':'ㄹ',
    'g':'ㅎ',
    'h':'ㅗ',
    'i':'ㅑ',
    'j':'ㅓ',
    'k':'ㅏ',
    'l':'ㅣ',
    'm':'ㅡ',
    'n':'ㅜ',
    'o':'ㅐ',
    'O':'ㅒ',
    'p':'ㅔ',
    'P':'ㅖ',
    'q':'ㅂ',
    'Q':'ㅃ',
    'r':'ㄱ',
    'R':'ㄲ',
    's':'ㄴ',
    't':'ㅅ',
    'T':'ㅆ',
    'u':'ㅕ',
    'v':'ㅍ',
    'w':'ㅈ',
    'W':'ㅉ',
    'x':'ㅌ',
    'y':'ㅛ',
    'z':'ㅋ'
    }

CHOSUNG_LIST = [
    "ㄱ",
    "ㄲ",
    "ㄴ",
    "ㄷ",
    "ㄸ",
    "ㄹ",
    "ㅁ",
    "ㅂ",
    "ㅃ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅉ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
]

JUNGSUNG_LIST = [
    "ㅏ",
    "ㅐ",
    "ㅑ",
    "ㅒ",
    "ㅓ",
    "ㅔ",
    "ㅕ",
    "ㅖ",
    "ㅗ",
    "ㅘ",
    "ㅙ",
    "ㅚ",
    "ㅛ",
    "ㅜ",
    "ㅝ",
    "ㅞ",
    "ㅟ",
    "ㅠ",
    "ㅡ",
    "ㅢ",
    "ㅣ",
]

JONGSUNG_LIST = [
    "",
    "ㄱ",
    "ㄲ",
    "ㄳ",
    "ㄴ",
    "ㄵ",
    "ㄶ",
    "ㄷ",
    "ㄹ",
    "ㄺ",
    "ㄻ",
    "ㄼ",
    "ㄽ",
    "ㄾ",
    "ㄿ",
    "ㅀ",
    "ㅁ",
    "ㅂ",
    "ㅄ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
]

BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28


def to_hangeul(word):
    h_word = ""
    for x in word:
        h_word += ENGHAN[x]
    return h_word


def get_syllable(h_word):
    result = []
    indices = []
    for i, c in enumerate(h_word):
        if c in JUNGSUNG_LIST:
            if h_word[i-1] not in JUNGSUNG_LIST:
                indices.append(i-1)
    
    print("indices:",indices)
    
    for idx in indices[::-1]:
        result.insert(0, h_word[idx:])
        h_word = h_word[:idx]
    return result


def get_double_char(char:str):
    if len(char) < 2:
        return char
    c1, c2 = list(char)
    if c1 == 'ㄱ' and c2 == 'ㅅ':
        return 'ㄳ'
    if c1 == 'ㄴ' and c2 == 'ㅈ':
        return 'ㄵ'
    if c1 == 'ㄴ' and c2 == 'ㅎ':
        return 'ㄶ'
    if c1 == 'ㄹ' and c2 == 'ㄱ':
        return 'ㄺ'
    if c1 == 'ㄹ' and c2 == 'ㅁ':
        return 'ㄻ'
    if c1 == 'ㄹ' and c2 == 'ㅂ':
        return 'ㄼ'
    if c1 == 'ㄹ' and c2 == 'ㅅ':
        return 'ㄽ'
    if c1 == 'ㄹ' and c2 == 'ㅌ':
        return 'ㄾ'
    if c1 == 'ㄹ' and c2 == 'ㅍ':
        return 'ㄿ'
    if c1 == 'ㄹ' and c2 == 'ㅎ':
        return 'ㅀ'
    if c1 == 'ㅂ' and c2 == 'ㅅ':
        return 'ㅄ'
    if c1 == 'ㅗ' and c2 == 'ㅏ':
        return 'ㅘ'
    if c1 == 'ㅗ' and c2 == 'ㅐ':
        return 'ㅙ'
    if c1 == 'ㅗ' and c2 == 'ㅣ':
        return 'ㅚ'
    if c1 == 'ㅜ' and c2 == 'ㅓ':
        return 'ㅝ'
    if c1 == 'ㅜ' and c2 == 'ㅔ':
        return 'ㅞ'
    if c1 == 'ㅜ' and c2 == 'ㅣ':
        return 'ㅟ'
    if c1 == 'ㅡ' and c2 == 'ㅣ':
        return 'ㅢ'


def get_cjj(syllable):
    try:
        ji = []
        for i, s in enumerate(syllable):
            if s in JUNGSUNG_LIST:
                ji.append(i)
        if len(ji) > 2:
            print(ji)
            raise Exception('NotValidSyllable')
        char1 = get_double_char(syllable[:ji[0]])
        char2 = get_double_char(syllable[ji[0]:ji[-1]+1])
        char3 = get_double_char(syllable[ji[-1]+1:])
        
        return [char1, char2, char3]
    except Exception as e:
        print('Unexcepted Exception:', e)
    
    
def combine(chars: list):
    char1_index = CHOSUNG_LIST.index(chars[0])
    char2_index = JUNGSUNG_LIST.index(chars[1])
    char3_index = JONGSUNG_LIST.index(chars[2])
    return BASE_CODE + CHOSUNG * char1_index + JUNGSUNG * char2_index + char3_index
    

if __name__ == "__main__":
    word = "dkssudgktpdyTkdwkdmaehehlqslekruqahdmaehehlqslekdhldnekruqwkdmaehehlqslekdPfmfemfausaksgek"
    print("input :", word)
    han_word = to_hangeul(word)
    print(han_word)
    syllables = get_syllable(han_word)
    print("syllables:", syllables)
    
    result = []
    try:
        for syllable in syllables:
            chars = get_cjj(syllable)
            result.append(chr(combine(chars)))
        print(''.join(result))
    except Exception as e:
        print(e)


    res = []
    for i in range(len(CHOSUNG_LIST)):
        for j in range(len(JUNGSUNG_LIST)):
            for k in range(len(JONGSUNG_LIST)):
                code = BASE_CODE + CHOSUNG * i + JUNGSUNG * j + k
                # print(chr(code))
                res.append(chr(code))
    
    print(len(res))
        
# TODO : 띄어쓰기도 되게 하기
# 한영 섞여도 되게 하기
# 이렇게 한영 tjRdueh 되게 하기