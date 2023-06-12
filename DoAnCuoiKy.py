import nltk

# Xây dựng các quy tắc văn phạm Context-Free Grammar

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> PROPERN | N | NOM | DET NOM | N ADJP | PROPERN NP | N N | DET NOM NP VP | NOM NP VP | DET NOM PROPERN | NOM PROPERN | NOM C NP
NOM -> N C PROPERN | N C N | N PROPERN | UN N | UN N ADJP | N N ADJP | N ADJP
VP -> ADVP VP | V PP | V NP | V VP | V NP PP | V | V NP VP | V PP VP | V VP ADJP | V NP ADJP | ADJP
ADJP -> ADJ | ADV ADJ | ADJ ADV ADJ
ADVP -> ADV
PP -> P NP 

PROPERN -> 'Nam' | 'Lan'
ADV -> 'thường' | 'mới' | 'rất' | 'hay'
ADJ -> 'mới' | 'hay'
V -> 'đến' | 'thích' | 'đọc' | 'ở' | 'mua' | 'tặng' | 'cho'
N -> 'thư_viện' | 'sách' | 'Nhà' | 'trường' | 'nhà' | 'nhà_trường'
C -> 'của'
DET -> 'một'
UN -> 'cuốn'
P -> 'ở' | 'gần'
""")

# nltk.app.rdparser()

def parse(sent):
    lst = []
    parser = nltk.RecursiveDescentParser(grammar)
    for tree in parser.parse(sent):
        lst.append(tree)
    return lst[0]


lines = open('TapNguLieuDoAnCuoiKy.txt', 'r', encoding="UTF8").readlines()
for line in lines:
    sentence = line.split()
    print(sentence)
    parse(sentence).draw()