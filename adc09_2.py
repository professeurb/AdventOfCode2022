import math

# file = "test09.txt"
# file = "test09_2.txt"
file = "input09.txt"


# I use copysign as -1 // 2 == -1

def follow_once(head, tail):
    delta = [tail[i] - head[i] for i in range(2)]
    if max(abs(delta[0]), abs(delta[1])) == 2:
        return tuple(head[i] + int(math.copysign(abs(delta[i]) // 2, delta[i]))
                     for i in range(2))
    return tuple(head[i] + delta[i] for i in range(2))


def head(file):
    dirs = {"L": (0, -1), "R": (0, 1), "U": (1, 1), "D": (1, -1)}
    head = [0, 0]
    yield tuple(head)
    with open(file, "r") as f:
        for line in f:
            dir = line[0]
            amp = int(line[2:])
            d, f = dirs[dir]
            for _ in range(amp):
                head[d] += f
                yield tuple(head)


def follow(pred):
    curr = (0, 0)
    for prev in pred:
        curr = follow_once(prev, curr)
        yield curr


print("Part One:", len(set(follow(head(file)))))

positions = head(file)
for _ in range(9):
    positions = follow(positions)

print("Part Two:", len(set(positions)))
