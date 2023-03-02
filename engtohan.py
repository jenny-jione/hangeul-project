from jamodict import *
    

def to_hangeul(word):
    h_word = ""
    for x in word:
        h_word += ENGTOHAN[x]
    return h_word


def make_tuple(indices: list):
    result = []
    if indices[0]:
        result.append((0, indices[0]))
    for i, _ in enumerate(indices):
        if i+1 < len(indices):
            result.append((indices[i], indices[i+1]))
    result.append((indices[-1], len(indices)-1))
    print(result)
    return result


# slice by jungsung
def slice_by_jungsung(h_word):
    result = []
    indices = []
    for i, c in enumerate(h_word):
        if c in JUNGSUNG_LIST:
            if h_word[i-1] not in JUNGSUNG_LIST and i>0:
                indices.append(i-1)
    print(indices, "@indices")
    if not indices:
        return [h_word]
    index_range = make_tuple(indices)
    for ir in index_range[:-1]:
        result.append(h_word[ir[0]:ir[1]])
    result.append(h_word[index_range[-1][0]:])
    return result


def is_double_char(c1:str, c2:str):
    if (c1 == 'ㄱ' and c2 == 'ㅅ') or \
        (c1 == 'ㄴ' and c2 == 'ㅈ') or \
        (c1 == 'ㄴ' and c2 == 'ㅎ') or \
        (c1 == 'ㄹ' and c2 == 'ㄱ') or \
        (c1 == 'ㄹ' and c2 == 'ㅁ') or \
        (c1 == 'ㄹ' and c2 == 'ㅂ') or \
        (c1 == 'ㄹ' and c2 == 'ㅅ') or \
        (c1 == 'ㄹ' and c2 == 'ㅌ') or \
        (c1 == 'ㄹ' and c2 == 'ㅍ') or \
        (c1 == 'ㄹ' and c2 == 'ㅎ') or \
        (c1 == 'ㅂ' and c2 == 'ㅅ') or \
        (c1 == 'ㅗ' and c2 == 'ㅏ') or \
        (c1 == 'ㅗ' and c2 == 'ㅐ') or \
        (c1 == 'ㅗ' and c2 == 'ㅣ') or \
        (c1 == 'ㅜ' and c2 == 'ㅓ') or \
        (c1 == 'ㅜ' and c2 == 'ㅔ') or \
        (c1 == 'ㅜ' and c2 == 'ㅣ') or \
        (c1 == 'ㅡ' and c2 == 'ㅣ'):
            return True
    else:
        return False
    

def get_syllable(letters):
    leng = len(letters)
    
    if letters[0] in CHOSUNG_LIST:
        if leng == 1:
            return [letters]
        if letters[1] in JUNGSUNG_LIST:
            if leng == 2:
                return [letters]
            if letters[2] in JUNGSUNG_LIST:
                if is_double_char(letters[1], letters[2]):
                    if leng == 3:
                        return [letters]
                    if letters[3] in JONGSUNG_LIST:
                        if leng == 4:
                            return [letters]
                        if letters[4] in JONGSUNG_LIST:
                            if is_double_char(letters[3], letters[4]):
                                if leng == 5:
                                    return [letters]
                                else:
                                    return [letters[:5], list(letters[4:])]
                            else:
                                return [letters[:4], list(letters[4:])]
                        else:
                            return [letters[:4], list(letters[4:])]
                    else:
                        return [letters[:3], list(letters[3:])]
                else:
                    return [letters[:2], list(letters[2:])]    
            elif letters[2] in JONGSUNG_LIST:
                if leng == 3:
                    return [letters]
                else:
                    return [letters[:3], list(letters[3:])]
            else:
                return [letters[:2], list(letters[2:])]
        else:
            return list(letters)
    else:
        return list(letters)
    

def make_flat(slist: list):
    result = []
    for s in slist:
        print(s)
        if isinstance(s, str):
            result.append(s)
            print(s)
            # return result
        elif isinstance(s, list):
            result.extend(make_flat(s))
            

if __name__ == "__main__":
    # word = "bbbdlfgfdnltkaa"
    word = "bbnldbdbbddlfgfdnltkaadddtkadbb"
    # word = "nn"
    # word = "dd"
    # word = "dhh"
    # word = "dknssl"
    # word = "bbbrnldudnjbbbb"
    # word = "dhdnsssssskskskskskfkfkfk"
    word = "dnsrsefaqt"
    print("input:", word)
    han_word = to_hangeul(word)
    print(han_word)
    
    res = slice_by_jungsung(han_word)
    print(res)
    
    syllables = []
    for letters in res:
        syllables.append(get_syllable(letters))
    
    print(syllables)
    print(syllables[1])
    # make_flat(syllables[1])
    