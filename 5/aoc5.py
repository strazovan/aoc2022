from enum import Enum

class Phase(Enum):
    CARGO = 1
    INSTRUCTIONS = 2

stacks = []
MATCH_PATTERN = "[ ] "

def process_cargo_line(line: str):
    if line.startswith(' 1'):
        # skip the line with stack numbers
        return
    stack_index = 0
    for index in range(0, len(line), len(MATCH_PATTERN)):
        package = line[index: index+len(MATCH_PATTERN)]
        content = package[1]
        if content != ' ':
            stacks[stack_index].insert(0, content)
        stack_index += 1
        

def process_instruction_line(line: str):
    split = line.split(' ')
    count = int(split[1])
    from_stack = int(split[3])
    to_stack = int(split[5])
    #part two specific
    dock = []
    for _ in range(count):
        value = stacks[from_stack-1].pop()
    # part one
        #stacks[to_stack-1].append(value)
    # part two - could be written in more performant way
        dock.append(value)
    dock.reverse()
    stacks[to_stack-1].extend(dock)



PHASE = Phase.CARGO

with open("input.txt", "r") as file:
    line = file.readline().replace('\n', '')
    # we can read number of stacks from the first line, every stack, but the last one, has this pattern "[.] "
    number_of_stacks = int(len(line)/len(MATCH_PATTERN) + 1)
    for i in range(number_of_stacks):
        stacks.append([])
    process_cargo_line(line)
    while True:
        line = file.readline()
        if not line:
            break
        line = line.replace('\n', '')
        if len(line) == 0:
            # empty line separates cargo from instructions
            PHASE = Phase.INSTRUCTIONS
            continue

        if PHASE == Phase.CARGO:
            process_cargo_line(line)
        else:
            process_instruction_line(line)

# for result we need to print top of each of the stacks
result = ""
for stack in stacks:
    if len(stack) == 0:
        result += " "
    else:  
        result += stack.pop()
print(result)