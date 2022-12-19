class Tester:
    def __init__(self, costs, maxtime):
        self.costs = costs
        self.maxgeode = 0
        self.best = None
        self.states = set()
        self.maxrobots = [max(cost[i] for cost in self.costs)
                          for i in range(len(costs))]
        self.maxrobots[3] = 10000
        self.maxtime = maxtime

    def evolve(self, state):
        if state in self.states:
            return
        self.states.add(state)
        t, robots, items = state
        if t >= self.maxtime:
            return
        if (items[3] + robots[3] * (self.maxtime - t) +
                (self.maxtime - t) * (self.maxtime - t + 1) // 2) < self.maxgeode:
            return
        if robots[3] > 0:
            expect = items[3] + robots[3] * (self.maxtime - t)
            if expect > self.maxgeode:
                self.maxgeode = expect
                self.best = state
        for i in range(len(self.costs) - 1, -1, -1):
            cost = self.costs[i]
            if (all(cost[j] == 0 or robots[j] > 0 for j in range(4)) and
                    (robots[i] < self.maxrobots[i])):
                dt = max((cost[j] - items[j] + robots[j] - 1) // robots[j]
                         for j in range(4) if robots[j] > 0)
                dt = max(0, dt)
                new_state = (t + dt + 1,
                             tuple(robots[j] + 1 if j == i else robots[j]
                                   for j in range(4)),
                             tuple(items[j] + (dt + 1) * robots[j] - cost[j]
                                   for j in range(4)))
                self.evolve(new_state)

    def check(self):
        self.evolve((0, (1, 0, 0, 0), (0, 0, 0, 0)))
        return self.maxgeode


# file= "test19.txt"
file = "input19.txt"

maxtime = 24

with open(file, "r") as data:
    sum = 0
    for line in data:
        stuff = line.strip().split()
        costs = [(4, 0, 0, 0), (2, 0, 0, 0), (3, 14, 0, 0), (2, 0, 7, 0)]
        i = int(stuff[1][:-1])
        costs[0] = (int(stuff[6]), 0, 0, 0)
        costs[1] = (int(stuff[12]), 0, 0, 0)
        costs[2] = (int(stuff[18]), int(stuff[21]), 0, 0)
        costs[3] = (int(stuff[27]), 0, int(stuff[30]), 0)
        score = Tester(costs, maxtime).check()
        # print(i, "*", score, "=", i * score)
        sum += i * score
    print("Part One:", sum)

maxtime = 32

with open(file, "r") as data:
    prod = 1
    for _ in range(3):
        stuff = next(data).strip().split()
        costs = [(4, 0, 0, 0), (2, 0, 0, 0), (3, 14, 0, 0), (2, 0, 7, 0)]
        i = int(stuff[1][:-1])
        costs[0] = (int(stuff[6]), 0, 0, 0)
        costs[1] = (int(stuff[12]), 0, 0, 0)
        costs[2] = (int(stuff[18]), int(stuff[21]), 0, 0)
        costs[3] = (int(stuff[27]), 0, int(stuff[30]), 0)
        score = Tester(costs, maxtime).check()
        prod *= score
    print("Part Two:", prod)
