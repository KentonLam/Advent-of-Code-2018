from collections import defaultdict

def solve_1(claims):
    claimed = defaultdict(lambda: 0)

    for line in claims:
        split = line.rstrip().split(' ')
        code = split[0]
        coords = list(map(int, split[2].rstrip(':').split(',')))
        size = list(map(int, split[3].split('x')))
        
        for dx in range(size[0]):
            for dy in range(size[1]):
                claimed[(coords[0] + dx, coords[1] + dy)] += 1

    return [x >= 2 for x in claimed.values()].count(True)

def solve_2(claims):
    claimed = defaultdict(lambda: 0)

    for line in claims:
        split = line.rstrip().split(' ')
        code = split[0]
        coords = list(map(int, split[2].rstrip(':').split(',')))
        size = list(map(int, split[3].split('x')))
        
        # print(claimed[code])
        # return
        for dx in range(size[0]):
            for dy in range(size[1]):
                claimed[(coords[0] + dx, coords[1] + dy)] += 1

    for line in claims:
        split = line.rstrip().split(' ')
        code = split[0]
        coords = list(map(int, split[2].rstrip(':').split(',')))
        size = list(map(int, split[3].split('x')))
        
        this_claim = []

        for dx in range(size[0]):
            for dy in range(size[1]):
                this_claim.append((coords[0] + dx, coords[1] + dy))
        
        if all(claimed[pos] == 1 for pos in this_claim):
            print(code)

if __name__ == "__main__":
    with open('03_input.txt') as f:
        print(solve_2(list(f)))