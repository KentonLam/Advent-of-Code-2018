from util import * 
from collections import defaultdict, deque, namedtuple
import math
# from statistics import mean

from dataclasses import dataclass

# import numpy as np 
# import scipy as sp

def Ref(theta):
    return np.array([
        [np.cos(2*theta), np.sin(2*theta)],
        [np.sin(2*theta), -np.cos(2*theta)]
    ])

def Rot(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])

# left, straight, right
plus_directions = [-np.pi/2, 0, np.pi/2]

turns = {
    '\\': np.pi/4,
    '/': -np.pi/4
}

velocities = {
    '^': (0, -1),
    '<': (-1, 0),
    '>': (1, 0),
    'v': (0, 1)
}

velocity_names = {
    (0, -1): '^',
    (-1, 0): '<',
    (1, 0): '>',
    (0, 1): 'v'
}

def int_array(array):
    return [int(x) for x in np.round(array)]

def print_state(rails, carts):
    blank_rails = lambda: [''.join(line) for line in rails]
    rails = blank_rails()
    for cart in carts:
        x, y = int_array(cart[0])
        vel = tuple(int_array(cart[1]))
        rails[y] = rails[y][:x] + velocity_names[vel] + rails[y][x+1:]
    print('\n'.join(rails))


def parse(file):
    rails = []
    carts = []
    for y, line in enumerate(file):
        rails.append([])
        for x, c in enumerate(line.rstrip('\n')):
            rails[-1].append(c.replace('^', '|').replace('v', '|').replace('<', '-').replace('>', '-'))
            if c in velocities:
                carts.append([np.array([x, y]), np.array(velocities[c]), 0])
    # print(rails)
    # print(carts)

    for text_dir, vel in velocities.items():
        for text_turn, turn in turns.items():
            print(text_dir, text_turn, np.round(Ref(turn) @ np.array(vel)))
    print()
    print_state(rails, carts)
    print()
    return rails, carts

def solve_1(data):
    rails, carts = data
    cart_positions = set()
    for i in range(10000):
        carts.sort(key=lambda c: (c[0][1], c[0][0]))
        cart_positions.clear()
        for cart in carts:
            x, y = int_array(cart[0])
            track = rails[y][x]
            assert track != ' '
            vel = cart[1]
            if track in turns:
                vel = Ref(turns[track]) @ vel
            elif track == '+':
                vel = Rot(plus_directions[cart[2]]) @ vel
                cart[2] = (cart[2]+1) % 3
            
            cart[0] = cart[0] + vel
            cart[1] = vel

            new_pos = tuple(int_array((cart[0])))
            if new_pos in cart_positions:
                print('crash', new_pos)
                return
                
            cart_positions.add(new_pos)
        print()
        print('After', i+1, 'iterations.')
        # print_state(rails, carts)
        

    

def solve_2(data):
    rails, carts = data
    cart_positions = {}
    for i in range(10000):
        carts.sort(key=lambda c: (c[0][1], c[0][0]))
        to_remove = set()
        for n, cart in enumerate(carts):
            x, y = int_array(cart[0])
            track = rails[y][x]
            assert track != ' '
            vel = cart[1]
            if track in turns:
                vel = Ref(turns[track]) @ vel
            elif track == '+':
                vel = Rot(plus_directions[cart[2]]) @ vel
                cart[2] = (cart[2]+1) % 3
            
            cart[0] = cart[0] + vel
            cart[1] = vel

            new_pos = tuple(int_array((cart[0])))
            for other in carts:
                pass
            if any((cart[0]==c).all() for c in carts): 
                pass
            if new_pos in cart_positions:
                print('crash', new_pos)
                to_remove.update((n, cart_positions[new_pos]))
                del cart_positions[new_pos]
            else:
                cart_positions[new_pos] = n
        carts = [x for n, x in enumerate(carts) if n not in to_remove]
        print()
        print('After', i+1, 'iterations.')
        # print_state(rails, carts)
        if len(carts) == 1:
            print(carts)
            break
        if i+1 >= 8246:
            return
        

if __name__ == "__main__":
    with open('day13_input.txt') as f:
        solve_2(parse(f))