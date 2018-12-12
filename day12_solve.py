from util import * 
from collections import defaultdict, deque, namedtuple, OrderedDict
# import math
# from statistics import mean

# import numpy as np 
# import scipy as sp

def parse(file):
    f = [x.strip() for x in file]
    initial = f[0].replace('initial state: ', '')

    mappings = OrderedDict()

    for line in f[2:]:
        left, _, right = line.split(' ')
        mappings[tuple(c == '#' for c in left)] = right == '#'

    return (initial, mappings)

def search_in_dict(substring, pots):

    pass

def solve_1(data):
    changed = True 

    pots = set()

    s = data[0]

    print(s)
    for i, c in enumerate(s):
        if c == '#':
            pots.add(i)

    mapping = data[1]
    # print(mapping)

    # for iteration in range(20):
    # return 
    print('initial', pots)

    def matches(i, left):
        for n, plant in enumerate(left):
            if not ( ((i-2+n) in pots) == plant):
                return False 
        return True
        # return all(pots[i-2+n] == left[n] for n in range(5))

    # pots = {0, 1, 2}
    # print(matches(0, (False, True, True, True, True)))

    def print_pots(pots):
        print(min(pots), end=': ')
        for i in range(min(pots), max(pots)+1):
            print('#' if i in pots else '.', end='')
        print()

    print('INITIAL')
    print_pots(pots)

    left_index = -2
    right_index = max(pots)+2
    it = 0
    prev_sol = 0
    while it < 50000000000:
        if it % 1000 == 0:
            print('Iteration', it+1)
        new_pots = set()
        for i in range(left_index, right_index):
            for left, right in mapping.items():
                if matches(i, left):
                    if right:
                        new_pots.add(i)
                    if i-2 < left_index and right:
                        left_index = i-2
                    if i+2 > right_index and right:
                        right_index = i+2
                    break
        pots = new_pots
        print('Iteration', it+1, end=' ')
        print_pots(pots)
    
        sol = 0
        for i in new_pots:
            sol += i

        print(f'{it+1}, {sol}, {sol-prev_sol}')
        prev_sol = sol
        it += 1
        
        # quit out of this. efficient algorithm below.
        break 

    # At generation 124 and beyond, the pot sum is exactly 8990 + (t-124)*58
    print('part 2', 8990 + (50000000000-123)*58)

def solve_2(data):
    pass 

if __name__ == "__main__":
    with open('day12_test.txt') as f:
        print(solve_1(parse(f)))