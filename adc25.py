file = "test25.txt"
file = "input25.txt"

digits = {"2":2, "1":1, "0":0, "-":-1, "=":-2 }

def read_number(s):
    acc = 0
    for c in s:
        acc = 5 * acc + digits[c]
    return acc

def unsnaf(n):
    d = "=-012"
    s = ""
    p = 1
    while p <= n:
        n += 2 * p
        p *= 5
    while n != 0:
        s = d[n % 5] + s
        n //= 5
    return s


with open(file, "r") as data:
    sum = 0
    for line in data:
        line = line.strip()
        value = read_number(line)
        print(line, value, unsnaf(value))
        sum += value
    print("Part One", sum, unsnaf(sum))
