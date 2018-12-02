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

# unused
def almost_equal(str1, str2):
    assert len(str1) == len(str2)
    differences = 0
    str2_iter = iter(str2)
    for c1 in str1:
        if c1 != next(str2_iter):
            differences += 1
    return differences == 1

# i'd say this is O(nm) in number of box IDs and length of each ID.
def solve_2(file_input: iter) -> str:
    seen = set() 
    for word in file_input:
        for i in range(len(word)):
            word_part = word[:i] + word[i+1:] # delete char at i-th index
            if word_part in seen:
                return word_part
            seen.add(word_part)


if __name__ == "__main__":
    with open('02_input.txt') as f:
        print(solve_2(f))