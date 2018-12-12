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
        mappings[left] = right

    return (initial, mappings)

def search_in_dict(substring, pots):

    pass

def solve_1(data):
    changed = True 

    # pots = defaultdict(lambda: False)

    s = data[0]

    # for i, c in enumerate(s):
    #     pots[i] = c == 
    mapping = data[1]

    # for iteration in range(20):
    # return 
    print('initial', s)

    left_index = 0
    i = 0
    while i < 20:
        print()
        print('Iteration', i)
        changed = False 
        if s.find('#') <= 2:
            x = 4-s.find('#')
            s = '.'*x + s 
            left_index -= x
            continue
        if len(s)-1-s.rfind('#') <= 2:
            x = (len(s)-s.rfind('#'))
            s = s + '.'*x
            continue
        for left, right in mapping.items():
            
            # print(s)
            match = s.find(left)
            if match == -1: continue
            print(left, right)
            print(s)
            s = s[:match+2] + right + s[match+3:]
            # print(s)
            # print()
            changed = True
        i += 1
        print()
    
    print(left_index)
    sol = 0
    for i, c in enumerate(s):
        if c == '#':
            sol += left_index+i

    print(s, sol)

def solve_2(data):
    pass 

if __name__ == "__main__":
    with open('day12_test.txt') as f:
        print(solve_1(parse(f)))