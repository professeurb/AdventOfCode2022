# file = "test17.txt"
file = "input17.txt"

dirs = open(file).read().strip()

rocks = [["####"],
         [".#.",
          "###",
          ".#."],
         ["###", "..#", "..#"],
         ["#",
          "#",
          "#",
          "#"],
         ["##",
          "##"]]


chamber = [list("+-------+")]


def rock_at_position(rock, y, x):
    if y <= 0:
        return False
    for line in range(len(rock)):
        if y + line >= len(chamber):
            return x >= 1 and x + len(rock[0]) < 9
        for col in range(len(rock[line])):
            if (rock[line][col] == "#"
                    and chamber[y + line][x + col] != "."):
                return False
    return True


def put_rock_at_position(rock, y, x):
    for i in range(len(chamber), len(rock) + y):
        chamber.append(list("|.......|"))
    for line in range(len(rock)):
        for col in range(len(rock[line])):
            if rock[line][col] == "#":
                assert chamber[y + line][x + col] == '.'
                chamber[y + line][x + col] = '#'


def print_chamber():
    for line in chamber[:-10:-1]:
        print("".join(line))


topline = 0

d = 0
t = 0
dico = dict()

while t < 2022:
    r = rocks[t % 5]
    x = 3
    y = topline + 4
    while True:
        if dirs[d] == ">":
            if rock_at_position(r, y, x + 1):
                x = x + 1
        elif rock_at_position(r, y, x - 1):
            x = x - 1
        d = (d + 1) % len(dirs)
        if rock_at_position(r, y - 1, x):
            y = y - 1
        else:
            break
    put_rock_at_position(r, y, x)
    topline = max(topline, y + len(r) - 1)
    t += 1

print(f"Part One: {topline}")

topadd = 0

while t < 1000000000000:
    r = rocks[t % 5]
    x = 3
    y = topline + 4
    while True:
        if dirs[d] == ">":
            if rock_at_position(r, y, x + 1):
                x = x + 1
        elif rock_at_position(r, y, x - 1):
            x = x - 1
        d = (d + 1) % len(dirs)
        if rock_at_position(r, y - 1, x):
            y = y - 1
        else:
            break
    put_rock_at_position(r, y, x)
    topline = max(topline, y + len(r) - 1)
    #
    if (d, t % 5, x, topline - y) in dico:
        (ot, oy) = dico[(d, t % 5, x, topline - y)]
        delta_t = t - ot
        delta_y = topline - oy
        periods = (1000000000000 - t) // delta_t
        t += periods * delta_t
        topadd += periods * delta_y
    dico[(d, t % 5, x, topline - y)] = (t, topline)
    #
    t += 1

print(f"Part Two: {topline + topadd}")
