from dataclasses import dataclass 

@dataclass 
class Cart:
    symbol: str
    count: str # 

TURNS = {
    '^/': '>',
    '^\\': '<',
    '</': 'v',
    '<\\': '^',
    'v/': '<',
    'v\\': '>',
    '>/': '^',
    '>\\': 'v'
}

MOVES = {
    '^': (0, -1),
    '<': (-1, 0),
    'v': (0, 1),
    '>': (1, 0)
}

# cardinal directions, such that +1 index corresponds to 90 degree CCW rotation.
DIRECTIONS = ['>', '^', '<', 'v']


def parse(f):
    # coordinate system is (0,0) in top left corner.
    turns = {} # turns are keyed by (x,y) and the symbol.
    carts = {} # keyed by (x,y) in order of iteration.
    intersections = {}

    for y, line in enumerate(f):
        for x, c in enumerate(line):
            if c in '<^>v':
                carts[(x,y)] = Cart(c, 0)
            elif c in '/\\':
                turns[(x,y)] = c
            elif c == '+':
                intersections[(x,y)] = c
    
    return (carts, turns, intersections)


def solve_2(data):
    carts, turns, intersections = data

    while True:
        iter_carts = list(carts.items())
        iter_carts.sort(key=lambda x: x[0][::-1]) # sort by y, then x.

        #print(carts)
        for pos, cart in iter_carts:
            #print(pos, cart)

            # only change direction of carts which start the turn on a turn tile.
            if pos in turns:
                #print(pos, turns[pos])
                #print(turns[pos])
                turn = turns[pos]
                #print(turns)
                #print('hit turn at', pos, turn)
                cart.symbol = TURNS[cart.symbol + turn] # cart turns into new direction
            elif pos in intersections:
                # index of cart's current direction.
                cur_dir = DIRECTIONS.index(cart.symbol)
                # left, straight, right.
                dir_rot = [1, 0, -1][cart.count % 3]
                cart.count += 1
                cart.symbol = DIRECTIONS[(cur_dir + dir_rot) % 4]
            
            new_pos = (pos[0] + MOVES[cart.symbol][0], pos[1] + MOVES[cart.symbol][1])
            #print(new_pos)

            if new_pos in carts:
                print('imminent crash at:', new_pos)
                return

            print(pos, new_pos, cart)
            # move cart
            del carts[pos]
            carts[new_pos] = cart
        print()
        #input()
        
    pass

if __name__ == "__main__":
    with open('day13_input.txt') as f:
        solve_2(parse(f))