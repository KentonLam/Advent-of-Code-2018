from collections import defaultdict, deque

def parse(x):
    return deque(int(x) for x in x.read().split(' '))

counter = 0
metadata_sum = 0

def parse_one_node(numbers) -> (int, int):
    global counter
    global metadata_sum
    counter += 1 
    this_counter = counter
    c_left = numbers.popleft()
    m_left = numbers.popleft()
    print(c_left, m_left)

    # if a node has no children, its value is the sum of its 
    # metadata.
    child_values = []
    for i in range(c_left):
        c_id, c_val = parse_one_node(numbers)
        child_values.append(c_val)

    this_value = 0
    meta = []
    for i in range(m_left):
        m = numbers.popleft()
        meta.append(m)
        if 0 <= m-1 < len(child_values):
            this_value += child_values[m-1]

    if not child_values:
        assert this_value == 0
        this_value = sum(meta)
    
    metadata_sum += sum(meta)

    print(meta, this_value)

    return (this_counter, this_value)

# also solves 2.
def solve_1(numbers):
    # number of child/metadata nodes more we are expecting.

    parse_one_node(numbers)
    print(metadata_sum)
    # with open('08_graph.json', 'w') as g:
    #     from json import dump
    #     dump(networkx.node_link_data(graph), g)


if __name__ == "__main__":
    with open('08_input.txt') as f:
        solve_1(parse(f))