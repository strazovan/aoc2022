currentSum = 0

MAX_LIMIT = 3

max = []

def record_sum():
    max.append(currentSum)
    if len(max) > MAX_LIMIT:
        max.sort(reverse=True)
        del max[-1]

with open("input.txt", 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        if len(line) == 1:
            record_sum()
            currentSum = 0
        else:
            currentSum += int(line)

print(sum(max))