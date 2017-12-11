with open('input') as input_file:
    line = input_file.readline()

score = garbo_counter = current_depth = 0
garbo_flag = skip_char = False

for c in line:
    if garbo_flag:
        if skip_char:
            skip_char = False
        elif c == "!":
            skip_char = True
        elif c == ">":
            garbo_flag = False
        else:
            garbo_counter += 1
    else:
        if c == "{":
            current_depth += 1
        elif c == "}":
            score += current_depth
            current_depth -= 1
        elif c == "<":
            garbo_flag = True

print("1:", score)
print("2:", garbo_counter)
