
# PART ONE
#WINDOW_LENGTH = 4

# PART TWO
WINDOW_LENGTH = 14

def check_window(window):
    return len(set(window)) == WINDOW_LENGTH

with open("input.txt", "r") as file:
    input = file.readline()
    # there is better way for sure than do the first window in a "hardcoded" way
    floating_window = [*input[0:WINDOW_LENGTH]]
    print(floating_window)
    if check_window(floating_window):
        print(WINDOW_LENGTH)
        exit()

    for index in range(WINDOW_LENGTH, len(input)):
        char = input[index]
        floating_window[index%WINDOW_LENGTH] = char
        if check_window(floating_window) == True:
            break
    print(index+1)
