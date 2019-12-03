def req(x) :
    return 0 if x <= 0 else x + req((x//3)-2)

print(sum(list(map(lambda x: req((int(x)//3)-2), open("fuel.txt", "r").readlines()))))
