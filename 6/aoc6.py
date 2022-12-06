
# PART ONE
#WINDOW_LENGTH = 4

# PART TWO
WINDOW_LENGTH = 14

with open("input.txt", "r") as file:
    input = file.readline()
    # there is better way for sure than do the first window in a "hardcoded" way 
    floating_window = [*input[0:WINDOW_LENGTH]]
    print(floating_window)
    for index in range(0, len(input)):
        char = input[index]
        floating_window[index%WINDOW_LENGTH] = char
        if len(set(floating_window)) == WINDOW_LENGTH:
            break
    print(index+1)
