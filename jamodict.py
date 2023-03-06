ENGTOHAN = {
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

AB_CHO_DICT = {
    "ㄱ" : ["ㄱ", "ㄲ"],
    "ㄷ" : ["ㄷ", "ㄸ"],
    "ㅂ" : ["ㅂ", "ㅃ"],
    "ㅅ" : ["ㅅ", "ㅆ"],
    "ㅈ" : ["ㅈ", "ㅉ"],
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
    'ㅄ': ['ㅂ','ㅅ']
}

# WORDEX = "특정 버전의 이미지를 다운받고자 할 경우, 버전명을 명시해서 다운받을 수 있음."
# WORDEX = """container_name 은 markcloud 로 할 것
# hostname 부분은 자신이 사용하고 있는 IP주소 머신에 할당 된 ip 주소
# external_url ‘http://IP주소’  외부포트
# ssh 포트는 실제로 바깥에서 접속할 때의 ssh포트를 적어주어야 한다.
# listen_port 는 내부 포트 컨테이너 자체의 포트"""
# WORDEX = "위의 첫번째 코드를 작성하게 되면 컨테이너 내부로 진입이 가능합니다. 그렇다면 두번째 코드를 입력해줍니다. 아래의 사진과 같은 내용이 뜰때까지 대기합니다."
WORDEX = "이 경우에는 특정 버전의 이미지를 읽을 수 있게 한다 많이"

if __name__ == "__main__":
    print(len(CHOSUNG_LIST))
    print(len(JUNGSUNG_LIST))
    print(len(JONGSUNG_LIST))