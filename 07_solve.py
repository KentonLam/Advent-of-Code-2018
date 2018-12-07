from string import ascii_uppercase
from collections import deque
import networkx

def solve_1(input_lines):

    # list of (from, to) pairs
    edges = set()

    for line in input_lines:
        edges.add((line[5], line[36]))

    alphabet = set(x[0] for x in edges)
    alphabet.update(x[1] for x in edges)

    order = [] 

    while edges:
        successors = set(x[1] for x in edges)
        possible = alphabet - successors
        possible -= set(order)
        print('possible', possible)
        
        next_step = min(possible)
        order.append(next_step)
        print(next_step)

        to_remove = set()
        for x in edges:
            if x[0] == next_step:
                to_remove.add(x)
        print(to_remove)
        edges -= to_remove

    
    print('remaining', alphabet - set(order))
    print(''.join(order + list(alphabet - set(order))))
    pass 

def time_needed(letter):
    return ord(letter.upper()) - ord('A') + 60 + 1

def solve_2(input_lines):
    graph = networkx.DiGraph()
    for line in input_lines:
        graph.add_edge(line[5], line[36])

    alphabet = set('SCLPAMQVUWNHODRTGYKBJEFXZI')
    done = set()
    in_progress = set()

    # list of 5x [letter, time remaining].
    workers = [[None, None] for x in range(5)]

    get_possible = lambda: deque(sorted(set(node for node, deg in graph.in_degree if deg == 0) - in_progress))

    print('starting')
    i = 0
    while graph.number_of_edges() or (alphabet - done):
        print(i, 'seconds have passed.')
        possible = get_possible()
        print('available', possible)

        for n, worker in enumerate(workers):
            if worker[0] is not None:
                worker[1] -= 1
                if worker[1] == 0:
                    print('worker', n, 'done with', worker)
                    done.add(worker[0])
                    to_remove = (list(graph.out_edges(worker[0])))
                    print(to_remove)
                    graph.remove_edges_from(to_remove)
                    worker[0] = None

                    possible = get_possible()

            if worker[0] is None and possible: # worker is idle
                worker[0] = possible.popleft()
                worker[1] = time_needed(worker[0])
                print('worker', n, 'assigned', worker)
                in_progress.add(worker[0])
        i += 1

        # input('pause')

    print(i)



if __name__ == "__main__":
    with open('07_input.txt') as f:
        in_ = list(f)
        solve_2(in_)