from collections import defaultdict

def go(line):
    queue = []
    for c in line:
        # if there is a previous letter and it is case-insensitive equal to c
        # but not c, then we react.
        if queue and queue[-1].upper() == c.upper() and queue[-1] != c:
            del queue[-1]
        else:
            queue.append(c)
    return ''.join(queue)

def solve_1(input_lines):
    for line in input_lines:
        output = go(line.strip())
        print(output)
        print(len(output))
        break

def solve_2(input_lines):
    lengths = {}
    for line in input_lines:
        line = line.rstrip() 
        from string import ascii_lowercase
        for char_to_delete in ascii_lowercase:
            new_line = line.replace(char_to_delete, '').replace(char_to_delete.upper(), '')
            lengths[char_to_delete] = len(go(new_line))
            print(char_to_delete, lengths[char_to_delete])
        break

    print(min(lengths.items(), key=lambda x: x[1]))


if __name__ == "__main__":
    # print(go("dBaAbc"))
    with open('05_input.txt') as f:
        lines = list(f)
        print(solve_1(lines))
        print(solve_2(lines))