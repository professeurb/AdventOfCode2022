from collections import defaultdict

# file = "test21.txt"
file = "input21.txt"

monkeys = dict()
with open(file, "r") as data:
    for line in data:
        monk = line.strip().split(" ")
        monkeys[monk[0][:-1]] = [0, monk[1:]]


def value(monkey):
    job = monkeys[monkey]
    if job[0] == 1:
        return job[1]
    if len(job[1]) == 1:
        job[1] = int(job[1][0])
        job[0] = 1
        return job[1]
    v1 = value(job[1][0])
    v2 = value(job[1][2])
    if job[1][1] == '+':
        job[1] = v1 + v2
    elif job[1][1] == '-':
        job[1] = v1 - v2
    elif job[1][1] == '*':
        job[1] = v1 * v2
    else:
        job[1] = v1 // v2
    job[0] = 1
    return job[1]


print(f"Part One : {value('root')}")

monkeys = dict()
with open(file, "r") as data:
    for line in data:
        monk = line.strip().split(" ")
        monkeys[monk[0][:-1]] = [0, monk[1:]]

monkeys["root"][1][1] = "="


comonkeys = defaultdict(lambda: [])
for m in monkeys:
    job = monkeys[m][1]
    if len(job) == 3:
        comonkeys[job[0]].append(m)
        comonkeys[job[2]].append(m)


def revert(m):
    assert len(comonkeys[m]) == 1
    mm = comonkeys[m][0]
    mmj = monkeys[mm][1]
    assert len(mmj) == 3
    if mmj[1] == "+":
        if mmj[0] == m:
            # mm = m + mmj[2]
            monkeys[m][1] = [mm, "-", mmj[2]]
            revert(mm)
        else:
            assert mmj[2] == m
            # mm = mmj[0] + m
            monkeys[m][1] = [mm, "-", mmj[0]]
            revert(mm)
    elif mmj[1] == "-":
        if mmj[0] == m:
            # mm = m - mmj[2]
            monkeys[m][1] = [mm, "+", mmj[2]]
            revert(mm)
        else:
            assert mmj[2] == m
            # mm = mmj[0] - m
            monkeys[m][1] = [mmj[0], "-", mm]
            revert(mm)
    elif mmj[1] == "*":
        if mmj[0] == m:
            # mm = m * mmj[2]
            monkeys[m][1] = [mm, "/", mmj[2]]
            revert(mm)
        else:
            assert mmj[2] == m
            # mm = mmj[0] * m
            monkeys[m][1] = [mm, "/", mmj[0]]
            revert(mm)
    elif mmj[1] == "/":
        if mmj[0] == m:
            # mm = m / mmj[2]
            monkeys[m][1] = [mm, "*", mmj[2]]
            revert(mm)
        else:
            assert mmj[2] == m
            # mm = mmj[2] / m
            monkeys[m][1] = [mmj[2], "/", mm]
            revert(mm)
    else:
        assert mmj[1] == "="
        if mmj[0] == m:
            # mm = m == mmj[2]
            monkeys[m] = monkeys[mmj[2]]
        else:
            assert mmj[2] == m
            monkeys[m] = monkeys[mmj[0]]


revert("humn")
print(f"Part Two : {value('humn')}")
