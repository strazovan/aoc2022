BATCH_SIZE = 3


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


item_counts = {}
current_batch = []

overall = []

with open("input.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break

        current_batch.append(line[:-1])
        if len(current_batch) == BATCH_SIZE:
            # process the batch
            common_items = is_in_every_list(current_batch)
            if len(common_items) != 1:
                print("something went terribly wrong")
                exit(-1)
            overall.append(common_items[0])
            current_batch.clear()

sum = sum(map(lambda n: get_points(n), overall))
print(sum)
