# file = "test03.txt"
file = "input03.txt"


def value(c):
    if ord(c) < ord('a'):
        return ord(c) - ord('A') + 27
    return ord(c) - ord('a') + 1


def gen1():
    with open(file, "r") as f:
        for ligne in f:
            s1 = set(ligne[:len(ligne)//2])
            s2 = set(ligne[len(ligne)//2:])
            yield list(s1 & s2)[0]


print("Part One :", sum(value(c) for c in gen1()))


def gen2():
    with open(file, "r") as f:
        try:
            while True:
                s1 = set(next(f).strip())
                s2 = set(next(f).strip())
                s3 = set(next(f).strip())
                yield list(s1 & s2 & s3)[0]
        except StopIteration:
            pass


print("Part Two :", sum(value(c) for c in gen2()))
