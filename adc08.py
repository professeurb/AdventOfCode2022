# file = "test08.txt"
file = "input08.txt"

grid = []

with open(file, "r") as f:
    for line in f:
        grid.append(list(map(int, line.strip())))

h = len(grid)
w = len(grid[0])

b = [[False] * w for _ in range(h)]

for y in range(h):
    r = -1
    for x in range(w):
        if grid[y][x] > r:
            b[y][x] = True
            r = grid[y][x]
    r = -1
    for x in range(w - 1, -1, -1):
        if grid[y][x] > r:
            b[y][x] = True
            r = grid[y][x]

for x in range(w):
    r = -1
    for y in range(h):
        if grid[y][x] > r:
            b[y][x] = True
            r = grid[y][x]
    r = -1
    for y in range(h - 1, -1, -1):
        if grid[y][x] > r:
            b[y][x] = True
            r = grid[y][x]

cnt = 0
for y in range(h):
    for x in range(w):
        cnt += b[y][x]

print(f"Part One: {cnt}")

maxi = 0

for y in range(h):
    for x in range(w):
        print(f"Arbre {y} {x} (hauteur {grid[y][x]}) :")
        s = 1
        d = 1
        for yp in range(y + 1, h):
            if grid[yp][x] >= grid[y][x]:
                print(f"... y -> {yp} : {d}")
                break
            d += 1
        else:
            d -= 1
            print(f"... y :-> {yp} : {d}")
        s *= d
        d = 1
        for yp in range(y - 1, -1, -1):
            if grid[yp][x] >= grid[y][x]:
                print(f"... y -> {yp} : {d}")
                break
            d += 1
        else:
            d -= 1
            print(f"... y :-> {yp} : {d}")
        s *= d
        d = 1
        for xp in range(x + 1, w):
            if grid[y][xp] >= grid[y][x]:
                print(f"... x -> {xp} : {d}")
                break
            d += 1
        else:
            d -= 1
            print(f"... x :-> {xp} : {d}")
        s *= d
        d = 1
        for xp in range(x - 1, -1, -1):
            if grid[y][xp] >= grid[y][x]:
                print(f"... x -> {xp} : {d}")
                break
            d += 1
        else:
            d -= 1
            print(f"... x :-> {xp} : {d}")
        s *= d
        print(x, y, s)
        maxi = max(maxi, s)

print(maxi)
