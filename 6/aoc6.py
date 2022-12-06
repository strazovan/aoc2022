
# PART ONE
#WINDOW_LENGTH = 4

# PART TWO
WINDOW_LENGTH = 14

with open("input.txt", "r") as file:
    input = file.readline()
    # there is better way for sure
    floating_window = [*input[0:WINDOW_LENGTH]]
    for index in range(0, len(input)):
        char = input[index]
        floating_window[index%WINDOW_LENGTH] = char
        if len(set(floating_window)) == WINDOW_LENGTH:
            break
    print(index+1)
