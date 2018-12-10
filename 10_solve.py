from collections import defaultdict, deque

def parse(f):
    l = [] 
    for line in f:
        left, right = line.strip().replace('position=<', '').rstrip('>').split('> velocity=<')
        left = [int(x) for x in left.split(', ')]
        right = [int(x) for x in right.split(', ')]
        l.append((left, right))
    return l

def pos_at_t(start, velocity, time):
    return (start[0] + velocity[0]*time, start[1] + velocity[1]*time)

shifts = ( (0, 1), (1, 0), (0, -1), (-1, 0) )
def get_adjacents(pos):
    for shift in shifts:
        yield (pos[0]+shift[0], pos[1]+shift[1])

def compute_closeness(sky):
    closeness = 0
    for pos in sky:
        for adj in get_adjacents(pos):
            if adj in sky:
                closeness += 1
    return closeness

def solve_1(data):
    sky = dict()
    for t in range(10630, 10650):
        sky.clear()
        for pos, vel in data:
            sky[pos_at_t(pos, vel, t)] = 1
        
        if True or compute_closeness(sky) == 328:
            print()
            print()
            print('TIME', t)
            min_l = min(sky.keys(), key=lambda x: x[0])[0]
            min_u = min(sky.keys(), key=lambda x: x[1])[1]
            max_r = max(sky.keys(), key=lambda x: x[0])[0]
            max_d = max(sky.keys(), key=lambda x: x[1])[1]

            for y in range(min_u, max_d + 1):
                for x in range(min_l, max_r + 1):
                    if (x, y) in sky:
                        print('#', end='')
                    else:
                        print(' ', end='')
                print()
            print()
            print(t)
            print(compute_closeness(sky))






def solve_2(data):
    pass 

if __name__ == "__main__":
    with open('10_input.txt') as f:
        solve_1(parse(f))