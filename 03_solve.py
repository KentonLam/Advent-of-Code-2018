from collections import defaultdict, namedtuple

Claim = namedtuple('Claim', ('id', 'coords', 'size'))

def parse_claim(claim: str) -> Claim:
    split = claim.rstrip().split(' ')
    code = split[0]
    coords = tuple(map(int, split[2].rstrip(':').split(',')))
    size = tuple(map(int, split[3].split('x')))
    return Claim(code, coords, size)

def solve_1(claims):
    claimed = defaultdict(lambda: 0)

    for line in claims:
        c = parse_claim(line)
        for dx in range(c.size[0]):
            for dy in range(c.size[1]):
                claimed[(c.coords[0] + dx, c.coords[1] + dy)] += 1

    return [x >= 2 for x in claimed.values()].count(True)

def solve_2(claims):
    # mapping from each coordinate to the claim codes which have claimed it
    claimed = defaultdict(lambda: set())

    all_codes = set()

    overlapping_codes = set()

    for line in claims:
        c = parse_claim(line)
        
        all_codes.add(c.id)
        
        # print(claimed[code])
        # return
        for dx in range(c.size[0]):
            for dy in range(c.size[1]):
                claimed_by = claimed[(c.coords[0] + dx, c.coords[1] + dy)]
                claimed_by.add(c.id)
                if len(claimed_by) > 1:
                    # if this position has been claimed by anything other than
                    # this claim, it is overlapping.
                    overlapping_codes.update(claimed_by)
                
    # return the non-overlapping codes. should be only one.
    return (all_codes - overlapping_codes)

if __name__ == "__main__":
    with open('03_input.txt') as f:
        print(solve_2(list(f)))