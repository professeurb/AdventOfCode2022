# file = "test06_1.txt"
file = "input06.txt"


def distinct(s, pos, delta):
    while len(set(s[pos - delta:pos])) != delta:
        pos += 1
    return pos


with open(file) as f:
    line = f.readline().strip()
    print(distinct(line, 4, 4))
    print(distinct(line, 14, 14))
