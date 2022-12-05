class Interval():
    def __init__(self, interval_string):
        split = interval_string.split('-')
        self.start = int(split[0])
        self.end = int(split[1])

    def includes(self, other):
        return other.start >= self.start and other.end <= self.end

    def overlaps(self, other):
        return other.start <= self.end and self.start <= other.end


result = 0

with open("input.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        elfs = line.split(',')
        first = Interval(elfs[0])
        second = Interval(elfs[1])
       # if first.includes(second) or second.includes(first):
        #    result += 1
        if first.overlaps(second):
            result += 1

print(result)