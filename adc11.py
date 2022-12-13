from collections import deque

# file = "test11.txt"
file = "input11.txt"


def get_monkeys():
    cnt = 0
    with open(file, "r") as f:
        while True:
            line = next(f).strip()
            # print(line)
            assert line == f"Monkey {cnt}:"
            line = next(f).strip()
            items = list(map(int, line[16:].split(", ")))
            # print("Items:", items)
            line = next(f).strip()
            op = line[17:].split(" ")
            # print("Operation:", op)
            line = next(f).strip()
            assert line[:19] == "Test: divisible by "
            div = int(line[19:])
            # print("Divisibility:", div)
            line = next(f).strip()
            assert line[:25] == "If true: throw to monkey "
            iftrue = int(line[25:])
            line = next(f).strip()
            assert line[:26] == "If false: throw to monkey "
            iffalse = int(line[26:])
            # print("Test:", iftrue, iffalse)
            yield((deque(items), op, div, iftrue, iffalse))
            try:
                _ = next(f)
            except StopIteration:
                break
            cnt += 1


for rnd in range(1, 21):
    print("Round", rnd)
    for i in range(len(monkeys)):
        print("  Monkey", i)
        items, op, div, iftrue, iffalse = monkeys[i]
        print(" Items:", items)
        try:
            while True:
                item = items.popleft()
                scores[i] += 1
                print("    Item", item)
                # inspect
                operand = item if op[2] == "old" else int(op[2])
                new = item + operand if op[1] == "+" else item * operand
                print("      becomes", new)
                new2 = new // 3
                print("      and then", new2)
                if new2 % div == 0:
                    print("      pass to", iftrue)
                    monkeys[iftrue][0].append(new2)
                else:
                    print("      pass to", iffalse)
                    monkeys[iffalse][0].append(new2)
        except IndexError:
            pass
    print(f"  so that after round {rnd}...")
    for i in range(len(monkeys)):
        print("   ", i, monkeys[i][0])
    print()

print(scores)
scores.sort()
print("Part One:", scores[-1] * scores[-2])
"""


def euclide(a, b):
    if b == 0:
        return a
    return euclide(b, a % b)


def ppcm(a, b):
    return (a * b) // euclide(a, b)


monkeys = list(get_monkeys())
print(monkeys)
modulo = 1
for i in range(len(monkeys)):
    modulo = ppcm(modulo, monkeys[i][2])
    print(monkeys[i][2], modulo)
scores = [0] * len(monkeys)

for rnd in range(1, 10001):
    # print(rnd)
    # print("Round", round)
    for i in range(len(monkeys)):
        # print("  Monkey", i)
        items, op, div, iftrue, iffalse = monkeys[i]
        # print(" Items:", items)
        try:
            while True:
                item = items.popleft()
                scores[i] += 1
                # print("    Item", item)
                # inspect
                operand = item if op[2] == "old" else int(op[2])
                new = item + operand if op[1] == "+" else item * operand
                # print("      becomes", new)
                # new2 = new // 3
                new2 = new % modulo
                # print("      and then", new2)
                if new2 % div == 0:
                    # print("      pass to", iftrue)
                    monkeys[iftrue][0].append(new2)
                else:
                    # print("      pass to", iffalse)
                    monkeys[iffalse][0].append(new2)
        except IndexError:
            pass
    if rnd in [1, 20, 100, 500, 750, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
        print(f"Round {rnd}:", scores)

print(scores)
scores.sort()
print("Part Two:", scores[-1] * scores[-2])
