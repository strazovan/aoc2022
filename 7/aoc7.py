SIZE_TRESHOLD = 100000

class Node():
    def __init__(self,name, size):
        self.name = name
        self.size = size
        self.children = dict()
    
    def add_child(self, node):
        self.children[node.name] = node

root_folder = Node("/", None)

with open("input2.txt", "r") as file:
    while True:
        line = file.readline().replace("\n", "")
        if not line:
            break
        if line.startswith("$ "):
            command_data = line[len("$ "):].split(" ")
            if command_data[0] == "cd":
                if command_data == "..":
                    #folder_stack.pop()
                    pass
                elif command_data == "/":
                    print("changing to root")
                    #folder_stack = ["/"]
                    pass
                else:
                    print("changing to:")
                   # folder_stack.append(command_data[1].strip()) 
                    pass
        elif line.startswith("dir "):
            dir_name = line[len("dir "):]
            print("dir:", dir_name)
        else:
            file_data = line.split(" ")
            print("file:", file_data[0], ", name=", file_data[1])
        
result = 0
print(result)