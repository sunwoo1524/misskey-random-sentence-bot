import random

# sentence components
_subjects = [
    "내가",
    "고양이가",
    "강아지가",
    "키위가",
    "코끼리가",
    "삐삐쀼쀼가",
    "물고기가",
    "사카밤바스피스가",
    "툿친이",
    "일론 머스크가",
    "카피바라가",
    "멜론이",
    "김정은이",
    "타임라인이",
    "도파민이",
    "상사가",
    "블롭캣이",
    "아기가"
]

_modifiers = [
    "놀라운",
    "거대한",
    "하와와한",
    "귀여운",
    "말랑말랑한",
    "무서운",
    "더러운",
    "최고의",
    "최애의",
    "맛있는",
    "복잡한",
    "반짝반짝한",
    "뿌슝빠슝한",
    "엘렐레한",
    "작은",
    "작고 하찮은",
    "둔한",
    "날렵한",
    "느린",
    "빠른"
]

_objects = [
    "서버장을",
    "블롭캣을",
    "키보드를",
    "고양이를",
    "탕후루를",
    "지뢰를",
    "삐삐쀼쀼를",
    "생체 서버를",
    "학교를",
    "트위터를",
    "아이폰을",
    "리눅스를",
    "서버를",
    "멸치를",
    "연필을",
    "ActiveX를",
    "턱스를",
    "비밀번호를",
    "돈을",
    "통장을",
    "집을",
    "회사를"
]

_verbs = [
    "담궜다",
    "먹었다",
    "쓰다듬었다",
    "만들었다",
    "사랑했다",
    "던졌다",
    "요리했다",
    "찼다",
    "구웠다",
    "사냥했다",
    "터뜨렸다",
    "반으로 갈랐다",
    "구부려트렸다",
    "삭제했다",
    "촬영했다",
    "키웠다",
    "잡아먹었다",
    "눌렀다",
    "서버로 만들었다"
]


# choose random sentence components and generate sentence using them
def generateSentence():
    subject = random.choice(_subjects)
    modifier = random.choice(_modifiers)
    object = random.choice(_objects)
    verb = random.choice(_verbs)

    return f"{subject} {modifier} {object} {verb}."
