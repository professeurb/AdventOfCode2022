# file = "test20.txt"
file = "input20.txt"

key = 811589153

seq = []
zero_node = None
with open(file, "r") as data:
    for line in data:
        node = [int(line.strip()), None, None]
        if node[0] == 0:
            zero_node = node
        seq.append(node)

n = len(seq)
for i in range(n):
    seq[i][1] = seq[(i + 1) % n]
    seq[(i + 1) % n][2] = seq[i]


def remove(node):
    node[1][2] = node[2]
    node[2][1] = node[1]


def insert_after(a, b):
    n = a[1]
    b[1] = n
    n[2] = b
    a[1] = b
    b[2] = a


def move_right(start_node, delta):
    if delta == 0:
        return
    assert delta > 0
    next_node = start_node[1]
    for _ in range(delta - 1):
        next_node = next_node[1]
    # plug everything
    remove(start_node)
    insert_after(next_node, start_node)


def move_left(start_node, delta):
    if delta == 0:
        return
    assert delta > 0
    next_node = start_node[2]
    for _ in range(delta - 1):
        next_node = next_node[2]
    # plug everything
    remove(start_node)
    insert_after(next_node[2], start_node)


for node in seq:
    delta = node[0] % (n - 1)
    if delta > (n - 1) // 2:
        delta -= (n - 1)
        move_left(node, -delta)
    else:
        move_right(node, delta)

curr = zero_node
sum = 0
for _ in range(3):
    for _ in range(1000):
        curr = curr[1]
    sum += curr[0]
print(f"Part One: {sum}")

# Part Two
seq = []
zero_node = None
with open(file, "r") as data:
    for line in data:
        node = [key * int(line.strip()), None, None]
        if node[0] == 0:
            zero_node = node
        seq.append(node)

n = len(seq)
for i in range(n):
    seq[i][1] = seq[(i + 1) % n]
    seq[(i + 1) % n][2] = seq[i]
for _ in range(10):
    for node in seq:
        delta = node[0] % (n - 1)
        if delta > (n - 1) // 2:
            delta -= (n - 1)
            move_left(node, -delta)
        else:
            move_right(node, delta)


curr = zero_node
sum = 0
for _ in range(3):
    for _ in range(1000):
        curr = curr[1]
    sum += curr[0]
print(f"Part Two: {sum}")
