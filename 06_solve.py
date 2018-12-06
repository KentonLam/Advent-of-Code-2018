from collections import defaultdict, deque
import string 
import itertools
from typing import DefaultDict
import math
import sys

adjacents = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def get_adj(coord):
    adj = set()
    for dx, dy in adjacents:
        adj.add((coord[0] + dx, coord[1] + dy))
    return adj

def max_angle_difference(array):
    array.sort()
    return max((array[(i+1)%len(array)]-array[i])%(2*math.pi) for i in range(len(array)))

def compute_unbounded(coords):
    unbounded = []
    for coord in coords:
        angles = []
        for coord2 in coords:
            if coord == coord2:
                continue 
            angles.append(math.atan2(coord2[1]-coord[1], coord2[0]-coord[0]))
        if max_angle_difference(angles) >= math.pi:
            log(coord)
            unbounded.append(coord)
    return unbounded

def log(*args, **kwargs):
    # print(*args, **kwargs)
    pass

def solve_1(input_lines):
    coords = []
    for line in input_lines:
        if 'break' in line:
            break
        x, y = map(int, line.split(', '))
        coords.append((x, y))


    # a point is from the input list. coordinates are all across the map.
    points = coords
    unbounded = set(compute_unbounded(points))
    print('unbounded:')
    for x, y in unbounded:
        print(f'{x}, {y}')
    
    # mapping of coordinates to the point which has claimed it.
    claimed = dict()

    # mapping of points to its queue of coordinates to check.
    queue = dict()

    # initialise queue.
    for pt in points:
        queue[pt] = [pt]

    i = 0
    # perform a BFS across all the points.
    while queue:
        print('Iteration', i)
        moved = set()
        claim_changes = dict() # dict of changes to 'claimed' in this iteration.
        queue_changes = defaultdict(lambda: defaultdict(set))

        for point, to_check in queue.items():
            for a_coord in to_check:
                log('considering point', point, 'to', a_coord, end=' -- ')
                if a_coord in claimed:
                    log('  already claimed by', claimed[a_coord])
                elif a_coord in claim_changes:
                    log('  equidistant with', claim_changes[a_coord])
                    # a_coord is equally close to two points. 
                    # blacklist with None value.
                    if claim_changes[a_coord] != point:
                        claim_changes[a_coord] = None
                        queue_changes[claim_changes[a_coord]][a_coord].clear()
                else:
                    log('  is closest to this point, distance', i)
                    claim_changes[a_coord] = point
                    to_add = set(x for x in get_adj(a_coord) if x not in claimed)
                    if to_add:
                        queue_changes[point][a_coord].update(to_add)
                        moved.add(point)
            to_check.clear()
            
        assert len(set(claimed.keys()) & set(claim_changes.keys())) == 0
        claimed.update(claim_changes)
        for pt, coords_map in queue_changes.items():
            if pt is None: continue
            log('updating queue of', pt, 'with', coords_map)
            for coords in coords_map.values():
                queue[pt].extend(coords)

        residual = moved - unbounded

        if len(residual) <= 8: # HACK. potentially, compute_unbounded is incorrect.
            print('only unbounded points were moved. finished.')
            break
        print('changed minus unbounded', residual)
        if len(residual) <= 2:
            print('pause')
        i += 1
    
    print('computing')
    areas = defaultdict(lambda: 0)
    for claimer in claimed.values():
        if claimer not in (unbounded | residual):
            areas[claimer] += 1

    print('all areas')
    print('\n'.join(str(x) for x in areas.items()))
    print() 
    print('solution')
    sol = (max(areas.items(), key=lambda x: x[1]))
    print(sol)
    #print([x for x in claimed if claimed[x] == sol[0]])
    #print([x for x in claimed if claimed[x] == (1, 6)])


def solve_2(input_lines):
    points = []
    for line in input_lines:
        if 'break' in line:
            break
        x, y = map(int, line.split(', '))
        points.append((x, y))

    def manhattan(pos):
        distance = 0
        for pt in points:
            distance += abs(pt[0] - pos[0]) + abs(pt[1] - pos[1])
        return distance

    queue = deque()
    queue.append((150, 150))

    seen = set()
    area = 0

    while queue:
        pos = queue.popleft()
        if pos in seen:
            continue
        seen.add(pos)
        if manhattan(pos) <= 10000:
            area += 1
            queue.extend(get_adj(pos))
        
    print(area)




if __name__ == "__main__":
    import sys
    file = sys.argv[1] if len(sys.argv) > 1 else '06_input.txt'
    with open(file) as f:
        input_lines = [x.rstrip() for x in f]
        log(solve_2(input_lines))