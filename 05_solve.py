from collections import defaultdict

# this is horrendously inefficient. part 2 took almost 20 minutes to compute
def go(line):
    changed = True
    while changed:
        changed = False 
        for i in range(len(line)-1):
            if line[i].lower() == line[i+1].lower() and line[i] != line[i+1]:
                line = line[:i] + line[i+2:]
                changed = True
                break
    return line

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
        print(solve_2(list(f)))