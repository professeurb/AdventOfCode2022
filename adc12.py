from collections import deque

# file = "test12.txt"
file = "input12.txt"


def get_terrain():
    ter = []
    start = (0, 0)
    end = (0, 0)
    with open(file, "r") as f:
        for y, line in enumerate(f):
            l = list(line.strip())
            if "S" in l:
                x = l.index("S")
                start = (x, y)
                l[x] = "a"
            if "E" in l:
                x = l.index("E")
                end = (x, y)
                l[x] = "z"
            ter.append([ord(c) - ord("a") for c in l])
    return ter, start, end


terrain, start, end = get_terrain()
h = len(terrain)
w = len(terrain[0])
score = [[-1] * w for _ in range(h)]
file = deque([(start, 0)])
while True:
    v = file.popleft()
    print(v)
    ((x, y), p) = v
    if score[y][x] >= 0:
        continue
    score[y][x] = p
    if (x, y) == end:
        print(p)
        break
    if x > 0 and terrain[y][x - 1] <= terrain[y][x] + 1:
        file.append(((x - 1, y), p + 1))
    if x < w - 1 and terrain[y][x + 1] <= terrain[y][x] + 1:
        file.append(((x + 1, y), p + 1))
    if y > 0 and terrain[y - 1][x] <= terrain[y][x] + 1:
        file.append(((x, y - 1), p + 1))
    if y < h - 1 and terrain[y + 1][x] <= terrain[y][x] + 1:
        file.append(((x, y + 1), p + 1))

score = [[-1] * w for _ in range(h)]
file = deque([(end, 0)])
while True:
    v = file.popleft()
    print(v)
    ((x, y), p) = v
    if score[y][x] >= 0:
        continue
    score[y][x] = p
    if terrain[y][x] == 0:
        print(p)
        break
    if x > 0 and terrain[y][x - 1] >= terrain[y][x] - 1:
        file.append(((x - 1, y), p + 1))
    if x < w - 1 and terrain[y][x + 1] >= terrain[y][x] - 1:
        file.append(((x + 1, y), p + 1))
    if y > 0 and terrain[y - 1][x] >= terrain[y][x] - 1:
        file.append(((x, y - 1), p + 1))
    if y < h - 1 and terrain[y + 1][x] >= terrain[y][x] - 1:
        file.append(((x, y + 1), p + 1))
