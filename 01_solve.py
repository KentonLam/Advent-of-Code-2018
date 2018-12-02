
def solve_1(numbers):
    return sum(numbers)

def solve_2(numbers):
    seen = {0}
    freq = 0
    while True:
        for change in numbers:
            freq += change
            if freq in seen:
                return freq
            seen.add(freq)

if __name__ == "__main__":
    with open('01_input.txt') as f:
        numbers = list(map(int, f.readlines()))
        print(solve_2(numbers))