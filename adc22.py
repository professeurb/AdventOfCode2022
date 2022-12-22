# file, side = "test22.txt", 4
file, side = "input22.txt", 50

map = dict()

with open(file, "r") as data:
    for y, line in enumerate(data):
        # print(repr(line))
        if line == "\n":
            break
        for d, c in enumerate(line):
            if c != "\n" and c != " ":
                map[(d, y)] = c
    instr = next(data).strip()

# print(map)
# print(instr)

boundx = dict()
for d in set((x for (x, _) in map)):
    s = set((y for (xx, y) in map if xx == d))
    boundx[d] = (min(s), max(s))

boundy = dict()
for y in set((y for (_, y) in map)):
    s = set((x for (x, yy) in map if y == yy))
    boundy[y] = (min(s), max(s))

xpos = boundy[0][0]
ypos = 0
dir = [1, 0]

facings = {(1, 0): (0, '>'), (0, 1): (1, 'v'),
           (-1, 0): (2, '<'), (0, -1): (3, '^')}


def forward(amount):
    global xpos, ypos
    for _ in range(amount):
        xnew = xpos + dir[0]
        ynew = ypos + dir[1]
        if (xnew, ynew) not in map:
            if dir[0] == 1:
                assert dir[1] == 0
                xnew = boundy[ypos][0]
            elif dir[0] == -1:
                assert dir[1] == 0
                xnew = boundy[ypos][1]
            elif dir[1] == 1:
                assert dir[0] == 0
                ynew = boundx[xpos][0]
            else:
                assert dir[1] == -1
                assert dir[0] == 0
                ynew = boundx[xpos][1]
        if map[(xnew, ynew)] == "#":
            break
        # print((xpos, ypos))
        map[(xpos, ypos)] = facings[tuple(dir)][1]
        xpos = xnew
        ypos = ynew


# R : (1, 0) -> (0, 1)

amount = 0
for c in instr:
    if c in "0123456789":
        amount = 10 * amount + (ord(c) - 48)
    else:
        forward(amount)
        amount = 0
        if c == "L":
            # (xd + i yd) * -i
            [xd, yd] = dir
            dir[0] = yd
            dir[1] = -xd
        else:
            assert c == "R"
            # (xd + i yd) * i = - yd + i xd
            [xd, yd] = dir
            dir[0] = - yd
            dir[1] = xd
forward(amount)
map[(xpos, ypos)] = facings[tuple(dir)][1]

print(
    f"Part One: {xpos}, {ypos}, {facings[tuple(dir)]} : {1000 * (ypos + 1) + 4 * (xpos + 1) + facings[tuple(dir)][0]}")

# ymax = max(y for (_, y) in map) + 1
# for y in range(ymax):
#     print(" " * boundy[y][0], end="")
#     # print(boundy[y], "", end="")
#     for d in range(boundy[y][0], boundy[y][1] + 1):
#         print(map[(d, y)], end="")
#         # print(x, "", end="")
#     print()
#
# print(map)

connect = dict()
if side == 4:
    for d in range(4):
        connect[(8 + d, -1, 0, -1)] = (3 - d, 4, (0, 1))
        connect[(3 - d, 3, 0, -1)] = (8 + d, 0, (0, 1))
        connect[(7, d, -1, 0)] = (4 + d, 4, (0, 1))
        connect[(4 + d, 3, 0, -1)] = (8, d, (1, 0))
        connect[(12, d, 1, 0)] = (15, 11 - d, (-1, 0))
        connect[(16, 11 - d, 1, 0)] = ((11, d, (-1, 0)))
        connect[(12, 4 + d, 1, 0)] = (15 - d, 8, (0, 1))
        connect[(12 + d, 7, 0, -1)] = (11, 7 - d, (-1, 0))
        connect[(4 + d, 8, 0, 1)] = (8, 11 - d, (1, 0))
        connect[(7, 11 - d, -1, 0)] = (4 + d, 7, (0, -1))
        connect[(d, 8, 0, 1)] = (11 - d, 11, (0, -1))
        connect[(11 - d, 12, 0, 1)] = (d, 7, (0, -1))
        connect[(-1, 4 + d, -1, 0)] = (15 - d, 11, (0, -1))
        connect[(15 - d, 12, 0, 1)] = (0, 4 + d, (1, 0))
if side == 50:
    for d in range(50):
        connect[(49, d, -1, 0)] = (0, 149 - d, (1, 0))  # 1
        connect[(-1, 100 + d, -1, 0)] = (50, 49 - d, (1, 0))
        connect[(49, 50 + d, -1, 0)] = (d, 100, (0, 1))  # 2
        connect[(d, 99, 0, -1)] = (50, 50 + d, (1, 0))
        connect[(100, 50 + d, 1, 0)] = (100 + d, 49, (0, -1))  # 3
        connect[(100 + d, 50, 0, 1)] = (99, 50 + d, (-1, 0))
        connect[(100, 100 + d, 1, 0)] = (149, 49 - d, (-1, 0))  # 4
        connect[(150, d, 1, 0)] = (99, 149 - d, (-1, 0))
        connect[(50, 150 + d, 1, 0)] = (50 + d, 149, (0, -1))  # 5
        connect[(50 + d, 150, 0, 1)] = (49, 150 + d, (-1, 0))
        connect[(d, 200, 0, 1)] = (100 + d, 0, (0, 1))  # 6
        connect[(100 + d, -1, 0, -1)] = (d, 199, (0, -1))
        connect[(50 + d, -1, 0, -1)] = (0, 150 + d, (1, 0))  # 7
        connect[(-1, 150 + d, -1, 0)] = (50 + d, 0, (0, 1))

for (x, y) in map:
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x2 = x + d[0]
        y2 = y + d[1]
        if (x2, y2) not in map:
            xp, yp, nd = connect[(x2, y2, d[0], d[1])]
            xpp = xp - nd[0]
            ypp = yp - nd[1]
            print(
                f"{x, y, d[0], d[1]} -> {x2, y2} == {xp, yp, nd[0], nd[1]} -> {xpp, ypp}")
            xppp, yppp, _ = connect[(xpp, ypp, -nd[0], -nd[1])]
            assert x == xppp and y == yppp, f"{x, y} -> {x2, y2} == {xp, yp} -> {xpp, ypp} == {xppp,  yppp}"

print("Check algebraic topology")


def forward2(amount):
    global xpos, ypos
    for _ in range(amount):
        xnew = xpos + dir[0]
        ynew = ypos + dir[1]
        dirnew = None
        if (xnew, ynew) not in map:
            print(xnew, ynew, connect[(xnew, ynew, dir[0], dir[1])])
            (xnew, ynew, dirnew) = connect[(xnew, ynew, dir[0], dir[1])]
        if map[(xnew, ynew)] == "#":
            break
        # print((xpos, ypos))
        map[(xpos, ypos)] = facings[tuple(dir)][1]
        xpos = xnew
        ypos = ynew
        if dirnew:
            dir[0] = dirnew[0]
            dir[1] = dirnew[1]


for (x, y) in map:
    if map[(x, y)] != "#":
        map[(x, y)] = ","

xpos = boundy[0][0]
ypos = 0
dir = [1, 0]

amount = 0
for c in instr:
    if c in "0123456789":
        amount = 10 * amount + (ord(c) - 48)
    else:
        forward2(amount)
        amount = 0
        if c == "L":
            # (xd + i yd) * -i
            [xd, yd] = dir
            dir[0] = yd
            dir[1] = -xd
        else:
            assert c == "R"
            # (xd + i yd) * i = - yd + i xd
            [xd, yd] = dir
            dir[0] = - yd
            dir[1] = xd
forward2(amount)
map[(xpos, ypos)] = facings[tuple(dir)][1]

print(
    f"Part Two: {xpos}, {ypos}, {facings[tuple(dir)]} : {1000 * (ypos + 1) + 4 * (xpos + 1) + facings[tuple(dir)][0]}")

ymax = max(y for (_, y) in map) + 1
for y in range(ymax):
    print(" " * boundy[y][0], end="")
    # print(boundy[y], "", end="")
    for d in range(boundy[y][0], boundy[y][1] + 1):
        print(map[(d, y)], end="")
        # print(x, "", end="")
    print()
