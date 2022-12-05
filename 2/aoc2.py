WIN = 6
LOSE = 0
DRAW = 3

NORMALIZATION_MAP = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
    'X': 'R',
    'Y': 'P',
    'Z': 'S'
}

POINTS_MAP = {
    'R': 1,
    'P': 2,
    'S': 3
}

RULES = {
    'PP': DRAW,
    'RR': DRAW,
    'SS': DRAW,
    'PR': LOSE,
    'PS': WIN,
    'RP': WIN,
    'RS': LOSE,
    'SP': LOSE,
    'SR': WIN
}

score = 0
with open("input.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        
        split = line.split(' ')
        elf = NORMALIZATION_MAP[split[0]]
        me = NORMALIZATION_MAP[split[1][:-1]]
        score += POINTS_MAP[me] + RULES[elf + me]

print(score)