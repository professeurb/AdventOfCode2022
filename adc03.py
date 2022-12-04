# file = "test03.txt"
file = "input03.txt"

with open(file, "r") as f:
    score = 0
    for ligne in f:
        s1 = set(ligne[:len(ligne)//2])
        s2 = set(ligne[len(ligne)//2:])
        item = ord(list(s1 & s2)[0])
        if item < ord('a'):
            score += item - ord('A') + 27
        else:
            score += item - ord('a') + 1

print("Part One :", score)

with open(file, "r") as f:
    score = 0
    cnt = 0
    for ligne in f:
        ligne = ligne.strip()
        if cnt == 0:
            bag = set(ligne)
        else:
            bag = bag & set(ligne)
        cnt += 1
        if cnt == 3:
            assert len(bag) == 1
            item = ord(list(bag)[0])
            if item < ord('a'):
                score += item - ord('A') + 27
            else:
                score += item - ord('a') + 1
            cnt = 0

print("Part Two :", score)
