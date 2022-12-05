NUM_OF_COMPARTMENTS = 2


def split_to_compartments(line: str):
    num_of_items_in_compartment = int(len(line)/NUM_OF_COMPARTMENTS)
    res = []
    for i in range(0, NUM_OF_COMPARTMENTS, 1):
        start = i*num_of_items_in_compartment
        res.append(line[start:start + num_of_items_in_compartment])
    return res


def get_points(char):
    ascii = ord(char)
    if ascii > 96:
        # lowercase
        return ascii - 96
    else:
        # uppercase
        return ascii - 38


def is_in_every_list(lists):
    # assuming that there is always at least one
    result = set(lists[0])
    for i in range(len(lists)):
        result = result & set(lists[i])
    return list(result)

overall = []

with open("input.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break

        common_items = is_in_every_list(split_to_compartments(line))
        for item in common_items:
            overall.append(item)

sum = sum(map(lambda n: get_points(n), overall))
print(sum)
