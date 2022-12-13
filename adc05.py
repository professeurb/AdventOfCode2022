# file = "test04.txt"
file = "input04.txt"

with open(file, "r") as f:
    cnt = 0
    for ligne in f:
        [g, d] = ligne.split(",")
        [gd, gf] = map(int, g.split("-"))
        [dd, df] = map(int, d.split("-"))
        test = (gd <= dd <= df <= gf) or (dd <= gd <= gf <= df)
        if test:
            cnt += 1


print("Part One :", cnt)

with open(file, "r") as f:
    cnt = 0
    for ligne in f:
        [g, d] = ligne.split(",")
        [gd, gf] = map(int, g.split("-"))
        [dd, df] = map(int, d.split("-"))
        test = ((gd <= dd <= gf) or (dd <= gd <= df)
                or (gd <= df <= gf) or (dd <= gf <= df))
        if test:
            cnt += 1


print("Part Two :", cnt)
