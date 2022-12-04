import heapq

data = []

with open("input01.txt", "r") as f:
    elf = 0
    for ligne in f:
        if ligne == "\n":
            data.append(-elf)
            elf = 0
        else:
            elf += int(ligne.strip())
    data.append(-elf)

heapq.heapify(data)
print("Part One:", maxi := - heapq.heappop(data))
print("Part Two:", maxi - heapq.heappop(data) - heapq.heappop(data))
