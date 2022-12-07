SIZE_TRESHOLD = 100000
DISK_SIZE = 70000000
REQUIRED_SPACE = 30000000


class Node():
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.children = {}
        self.cached_size = None

    def add_child(self, node):
        self.children[node.name] = node

    def get_size(self):
        if self.cached_size is not None:
            return self.cached_size
        sum = 0
        if self.size is not None:
            sum += self.size
        for child in self.children.values():
            sum += child.get_size()
        self.cached_size = sum
        return sum

root_folder = Node("/", None)
folder_stack = None

with open("input.txt", "r") as file:
    while True:
        line = file.readline().replace("\n", "")
        if not line:
            break
        if line.startswith("$ "):
            command_data = line[len("$ "):].split(" ")
            if command_data[0] == "cd":
                if command_data[1] == "..":
                    folder_stack.pop()
                    pass
                elif command_data[1] == "/":
                    folder_stack = [root_folder]
                else:
                    # target folder should be always there
                    folder_stack.append(folder_stack[-1].children[command_data[1]])
                    pass
        elif line.startswith("dir "):
            dir_name = line[len("dir "):]
            folder_stack[-1].add_child(Node(dir_name, None))
        else:
            file_data = line.split(" ")
            folder_stack[-1].add_child(Node(file_data[1], int(file_data[0])))

#part 1
def get_nodes_below_threshold(node: Node):
    sum = 0
    size = node.get_size()
    if (size < SIZE_TRESHOLD):
        sum += size
    for key, value in node.children.items():
        # we are interested only in folders
        if value.size is None:
            sum += get_nodes_below_threshold(value)
    return sum 

print(get_nodes_below_threshold(root_folder))

# part 2
free_space = DISK_SIZE - root_folder.get_size()
if free_space >= REQUIRED_SPACE:
    # that would be funny...
    exit()

min_size = root_folder.get_size()

def find_smallest_folder_to_delete(node: Node, min_size):
    size = node.get_size()
    if size < min_size and free_space + size >= REQUIRED_SPACE:
        min_size = size
    for key, value in node.children.items():
        # we are interested only in folders
        if value.size is None:
            min_size = min(find_smallest_folder_to_delete(value, min_size), min_size)
    return min_size

min_size = find_smallest_folder_to_delete(root_folder, min_size)
print(min_size)