# file = "test20.txt"
file = "input20.txt"

seq = []

with open(file, "r") as data:
    for i, l in enumerate(data):
        seq.append((i, int(l.strip())))

n = len(seq)
backseq = list(range(n))

# print(seq)


def check(seq, backseq):
    for i in range(len(seq)):
        assert i == backseq[seq[i][0]], f"{i}, {seq}, {backseq}"


for i in range(n):
    # move ith value
    curr = seq[backseq[i]]
    # print(f"Moving {i}th number : {curr[1]}")
    p = backseq[i]
    d = curr[1] % (n - 1)
    if d > 0:
        for j in range(d):
            seq[(p + j) % n] = seq[(p + j + 1) % n]
            backseq[seq[(p + j) % n][0]] = (p + j) % n
        seq[(p + d) % n] = curr
        backseq[curr[0]] = (p + d) % n
        check(seq, backseq)
    elif d < 0:
        d = -d
        for j in range(d):
            seq[(p - j) % n] = seq[(p - j - 1) % n]
            backseq[seq[(p - j) % n][0]] = (p - j) % n
        seq[(p - d) % n] = curr
        backseq[curr[0]] = (p - d) % n
        # check(seq, backseq)
    # print(seq)
zero = 0
for i in range(n):
    if seq[i][1] == 0:
        zero = i
v1 = seq[(zero + 1000) % n][1]
v2 = seq[(zero + 2000) % n][1]
v3 = seq[(zero + 3000) % n][1]
print(f"Part One: {v1} + {v2} + {v3} = {v1 + v2 + v3}")

# Part Twp

key = 811589153

seq = []

with open(file, "r") as data:
    for i, l in enumerate(data):
        seq.append((i, key * int(l.strip())))

n = len(seq)
backseq = list(range(n))

# pri
# def check(seq, backseq):
#     for i in range(len(seq)):
#         assert i == backseq[seq[i][0]], f"{i}, {seq}, {backseq}"

for _ in range(10):
    for i in range(n):
        # move ith value
        curr = seq[backseq[i]]
        # print(f"Moving {i}th number : {curr[1]}")
        p = backseq[i]
        d = curr[1] % (n - 1)
        if d > 0:
            for j in range(d):
                seq[(p + j) % n] = seq[(p + j + 1) % n]
                backseq[seq[(p + j) % n][0]] = (p + j) % n
            seq[(p + d) % n] = curr
            backseq[curr[0]] = (p + d) % n
            check(seq, backseq)
        elif d < 0:
            d = -d
            for j in range(d):
                seq[(p - j) % n] = seq[(p - j - 1) % n]
                backseq[seq[(p - j) % n][0]] = (p - j) % n
            seq[(p - d) % n] = curr
            backseq[curr[0]] = (p - d) % n

zero = 0
for i in range(n):
    if seq[i][1] == 0:
        zero = i

v1 = seq[(zero + 1000) % n][1]
v2 = seq[(zero + 2000) % n][1]
v3 = seq[(zero + 3000) % n][1]
print(f"Part Two: {v1} + {v2} + {v3} = {v1 + v2 + v3}")
