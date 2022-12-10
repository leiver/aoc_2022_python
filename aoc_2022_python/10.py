from utils.api import get_input

input_str = get_input(10)

x = 1
x_values = [x]
for command in input_str.rstrip().split("\n"):
    if command.rstrip() == "noop":
        x_values.append(x)
    else:
        number = int(command.rstrip().split(" ")[1])

        x_values.extend([x, x+number])
        x += number

result_part_1 = (
    x_values[19] * 20 +
    x_values[59] * 60 +
    x_values[99] * 100 +
    x_values[139] * 140 +
    x_values[179] * 180 +
    x_values[219] * 220
)

print(f'Solution part 1: {result_part_1}')

pixels = ""
for i in range(240):
    if i % 40 in range(x_values[i]-1, x_values[i] + 2):
        pixels += "#"
    else:
        pixels += "."

print("Solution part 2:")
for i in range(6):
    print(pixels[i*40:i*40+40])
