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

    pots = defaultdict(lambda: False)

    s = data[0]

    for i, c in enumerate(s):
        pots[i] = c == '#'

    mapping = data[1]
    # print(mapping)

    # for iteration in range(20):
    # return 
    print('initial', pots)

    def matches(i, left):
        return all(pots[i-2+n] == left[n] for n in range(5))

    def print_pots(pots):
        s = list(pots.items())
        s.sort()
        print(s[0][0], end=': ')
        for n, p in s:
            print('#' if p else '.', end='')
        print()

    print('INITIAL')
    print_pots(pots)

    left_index = -2
    right_index = len(pots)+2
    it = 0
    while it < 20:
        if it % 1000 == 0:
            print('Iteration', it+1)
        new_pots = defaultdict(lambda: False)
        for i in range(left_index, right_index):
            for left, right in mapping.items():
                if matches(i, left):
                    new_pots[i] = right
                    if i-2 < left_index and right:
                        left_index = i-2
                    if i+2 > right_index and right:
                        right_index = i+2
                    break
        pots = new_pots
        # print_pots(pots)
        it += 1
    
    print(left_index)
    sol = 0
    for i, c in new_pots.items():
        if c:
            sol += i

    print('solution', sol)

def solve_2(data):
    pass 

if __name__ == "__main__":
    with open('day12_input.txt') as f:
        print(solve_1(parse(f)))