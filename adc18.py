# file = "test18.txt"
file = "input18.txt"

s = set()
with open(file, "r") as data:
    for line in data:
        s.add(tuple(map(int, line.strip().split(","))))

total = 6 * len(s)
for (x, y, z) in s:
    if (x + 1, y, z) in s:
        total -= 2
    if (x, y + 1, z) in s:
        total -= 2
    if (x, y, z + 1) in s:
        total -= 2

print(f"Part One: {total}")

xmin = min(x for (x, _, _) in s) - 1
xmax = max(x for (x, _, _) in s) + 1
ymin = min(y for (_, y, _) in s) - 1
ymax = max(y for (_, y, _) in s) + 1
zmin = min(z for (_, _, z) in s) - 1
zmax = max(z for (_, _, z) in s) + 1

s2 = set()

pile = [(xmin, ymin, zmin)]


while pile:
    (x, y, z) = pile.pop()
    s2.add((x, y, z))
    for (x2, y2, z2) in [(x + 1, y, z),
                         (x - 1, y, z),
                         (x, y + 1, z),
                         (x, y - 1, z),
                         (x, y, z + 1),
                         (x, y, z - 1)]:
        if ((x2, y2, z2) not in s2
            and (x2, y2, z2) not in s
            and x2 >= xmin and x2 <= xmax
            and y2 >= ymin and y2 <= ymax
                and z2 >= zmin and z2 <= zmax):
            pile.append((x2, y2, z2))


# print(len(s2))

total2 = 6 * len(s2)

total2 -= 2 * ((xmax - xmin + 1) * (ymax - ymin + 1))
total2 -= 2 * ((xmax - xmin + 1) * (zmax - zmin + 1))
total2 -= 2 * ((zmax - zmin + 1) * (ymax - ymin + 1))

for (x, y, z) in s2:
    if (x + 1, y, z) in s2:
        total2 -= 2
    if (x, y + 1, z) in s2:
        total2 -= 2
    if (x, y, z + 1) in s2:
        total2 -= 2

print(f"Part Two: {total2}")
