from dataclasses import dataclass 

def parse(f):
    return [ tuple(map(int, l.strip().split(','))) for l in f]


def manhattan(a, b):
    diff = 0
    for ai, bi in zip(a, b):
        if ai-bi < 0:
            diff += bi-ai 
        else:
            diff += ai - bi
    return diff

def solve_2(data):
    data = set(data)
    seen = set()


    constellations = []
    remaining = data - seen
    while remaining:
        point = next(iter(remaining))
        #print()
        #print(point)
        seen.add(point)
        remaining = data - seen

        group = { point }


        added = [ point ]
        while added:
            point = added.pop()
            for p2 in remaining:
                if manhattan(point, p2) <= 3:
                    #print('    ', p2)
                    group.add(p2)
                    seen.add(p2)
                    added.append(p2)
            remaining = data - seen
        
        constellations.append(group)
    #print(constellations)
    print(len(constellations))
    pass

if __name__ == "__main__":
    with open('day25_input.txt') as f:
        solve_2(parse(f))