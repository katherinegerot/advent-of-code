print(sum(map((lambda a: lambda v: a(a, int(v))(lambda s, x: 0 if x <= 0 else x + s(s, (x // 3) - 2)), open("fuel.txt", "r").readlines()))) - (sum(map(int, open("fuel.txt", "r").readlines()))))
