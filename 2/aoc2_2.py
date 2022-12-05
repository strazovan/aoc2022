WIN = 6
LOSE = 0
DRAW = 3
NORMALIZATION_MAP = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
}
RESULT_MAP = {
    'X': LOSE,
    'Y': DRAW,
    'Z': WIN
}
POINTS_MAP = {
    'R': 1,
    'P': 2,
    'S': 3
}
RESPONSES = {
    'P': {
        DRAW: 'P',
        LOSE: 'R',
        WIN: 'S' 
    },
    'R': { 
        WIN: 'P' ,
        DRAW: 'R' ,
        LOSE: 'S' 
    },
    'S': { 
        LOSE: 'P',
        WIN: 'R',
        DRAW: 'S'
    } 
}
score = 0
with open("input.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        
        split = line.split(' ')
        elf = NORMALIZATION_MAP[split[0]]
        required_result = RESULT_MAP[split[1][:-1]]
        # find the rule that starts with elfs move and results with result
        
        score += POINTS_MAP[RESPONSES[elf][required_result]] + required_result

print(score)