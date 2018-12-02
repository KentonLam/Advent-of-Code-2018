from collections import defaultdict
from enum import Flag, auto

class ChecksumFlags(Flag):
    NONE = 0
    EXACTLY_2 = auto()
    EXACTLY_3 = auto()

def count_2_or_3(word: str) -> ChecksumFlags:
    counts = defaultdict(lambda: 0)
    for c in word:
        counts[c] += 1
    flags = ChecksumFlags.NONE
    for count in counts.values():
        if count == 2:
            flags |= ChecksumFlags.EXACTLY_2
        elif count == 3:
            flags |= ChecksumFlags.EXACTLY_3
    return flags

def solve_1(file_input: list) -> int:
    parts = [0, 0]
    for word in file_input:
        flags = count_2_or_3(word)
        parts[0] += bool(flags & ChecksumFlags.EXACTLY_2)
        parts[1] += bool(flags & ChecksumFlags.EXACTLY_3)
    return parts[0] * parts[1]

if __name__ == "__main__":
    with open('02_input.txt') as f:
        print(solve_1(f))