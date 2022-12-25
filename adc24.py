# file = "test24.txt"
file = "input24.txt"

dirs = {">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1)}

blizz = dict()
xsize = 0
ysize = 0

with open(file, "r") as data:
    for y, line in enumerate(data):
        line = line.strip()
        print(y, len(line), repr(line))
        if line.strip() == "":
            break
        for x, c in enumerate(line):
            xsize = max(xsize, x - 1)
            ysize = max(ysize, y - 1)
            if c in dirs:
                blizz[(x - 1, y - 1)] = dirs[c]
            # print(x, y, c)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


timeloop = lcm(xsize, ysize)

print(f"{xsize} ^ {ysize} = {timeloop}")

maps = [set() for _ in range(timeloop)]

for t in range(timeloop):
    for (x, y) in blizz:
        (dx, dy) = blizz[(x, y)]
        maps[t].add(((x + t * dx) % xsize, (y + t * dy) % ysize))

t = 0
seen = set()
candidats = {(0, -1)}
while True:
    assert len(candidats) > 0
    print(t, candidats)
    next_candidats = set()
    for (x, y) in candidats:
        if (x, y) in maps[t % timeloop]:
            continue
        if (x, y, t % timeloop) in seen:
            continue
        seen.add((x, y, t % timeloop))
        if x == xsize - 1 and y == ysize:
            print(t)
            exit()
        next_candidats.add((x, y))
        for (nx, ny) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if (nx >= 0 and nx < xsize and ny >= 0
                    and (ny < ysize or (ny == ysize and nx == xsize - 1))):
                next_candidats.add((nx, ny))
    candidats.clear()
    candidats.update(next_candidats)
    t = t + 1

print(len(blizz), blizz)
print(xsize, ysize, lcm(xsize, ysize))
