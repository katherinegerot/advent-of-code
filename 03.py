import sys

f = open(sys.argv[1], "r")
content = f.read()
lines = content.split(",")
i = 0
while i < len(lines) :
    code = lines[i]
    if code == 1 :
        a = lines[i + 1]
        b = lines[i + 2]
        out = lines[i + 3]
        lines[out] = lines[a] + lines[b]
        i+=3
    elif code == 2 :
        a = lines[i + 1]
        b = lines[i + 2]
        out = lines[i + 3]
        lines[out] = lines[a] * lines[b]
        i+=3
    elif code == 99 :
        print("HALT: 99,", i)
        break;
    else :
        print("Something went wrong, CODE:", code, "INDEX:", i)
    i+=1
print(lines)
