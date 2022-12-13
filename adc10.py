# file = "test10.txt"
file = "input10.txt"


def gen_values():
    val = 1
    yield val
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            # print(line)
            if line == "noop":
                yield val
                continue
            assert line[:4] == "addx"
            yield val
            val += int(line[5:])
            yield val


values = gen_values()
sum = 0
for i in range(1, 221):
    v = next(values)
    print(i, v, i * v)
    if i in [20, 60, 100, 140, 180, 220]:
        sum += v * i
print("Sum:", sum)

values = gen_values()
for i in range(6):
    for j in range(40):
        v = next(values)
        if abs(v - j) <= 1:
            print("#", end="")
        else:
            print(".", end="")
    print()

# PCPBKAPJ
