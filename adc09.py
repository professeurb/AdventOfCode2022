import math

# file = "test09.txt"
# file = "test09_2.txt"
file = "input09.txt"

dirs = {"L": (0, -1), "R": (0, 1), "U": (1, 1), "D": (1, -1)}


# I use copysign since -1 // 2 == -1

def follow(head, tail):
    delta = [tail[i] - head[i] for i in range(2)]
    if max(abs(delta[0]), abs(delta[1])) == 2:
        return tuple(head[i] + math.copysign(abs(delta[i]) // 2, delta[i])
                     for i in range(2))
    return tuple(head[i] + delta[i] for i in range(2))


def check(a, b):
    for i in range(2):
        assert abs(a[i] - b[i]) <= 1


with open(file, "r") as f:
    head = [0, 0]
    traj = [tuple(head)]
    for line in f:
        dir = line[0]
        d, f = dirs[dir]
        amp = int(line[2:])
        for _ in range(amp):
            head[d] += f
            traj.append(tuple(head))
    for i in range(9):
        tail = (0, 0)
        traj2 = [tail]
        for h in traj:
            old = tail
            tail = follow(h, tail)
            traj2.append(tail)
            check(h, tail)
            check(old, tail)
        traj = traj2
    print(len(set(traj)))
