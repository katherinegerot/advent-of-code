lines = list(map(int, open("intcode.txt", "r").read().split(",")))
i = 0
while i < len(lines):
    if lines[i] == 1:
        lines[lines[i + 3]] = lines[lines[i + 1]] + lines[lines[i + 2]]
    elif lines[i] == 2:
        lines[lines[i + 3]] = lines[lines[i + 1]] * lines[lines[i + 2]]
    else:
        break
    i+= 4 if lines[i] == 1 or lines[i] == 2 else 1
print(lines)
