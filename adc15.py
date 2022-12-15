import re

# file, row, maxi = "test15.txt", 10, 20
file, row, maxi = "input15.txt", 2000000, 4000000

ss, bs = [], []

r = re.compile(
    "Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

with open(file, "r") as f:
    for line in f:
        m = r.match(line.strip())
        assert m is not None
        [xs, ys, xb, yb] = [int(m.group(i)) for i in range(1, 5)]
        ss.append((xs, ys, abs(xb - xs) + abs(yb - ys)))
        bs.append((xb, yb))

ss.sort()


def process_line(ss, y):
    line = []
    for (xs, ys, rs) in ss:
        d = rs - abs(y - ys)
        if d < 0:
            continue
        xl, xr = xs - d, xs + d
        while line and xl <= line[-1][1] + 1:
            zl, zr = line.pop()
            xl, xr = min(xl, zl), max(xr, zr)
        line.append((xl, xr))
    return line


print(
    f"Part One: {sum([r - l + 1 for (l, r) in process_line(ss, row)]) - sum([1 for (_, y) in bs if y == row])}")

for y in range(maxi + 1):
    # print(y, process_line(ss, y))
    for (xl, xr) in process_line(ss, y):
        if xr < 0:
            continue
        if xl <= 0 and xr < maxi:
            print(f"Part Two: {4000000 * (xr + 1) + y} at ({xr + 1}, {y})")
            exit()
