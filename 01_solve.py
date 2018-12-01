
def solve_1(numbers):
    return sum(numbers)

def solve_2(numbers):
    pass

if __name__ == "__main__":
    with open('01_input.txt') as f:
        print(solve_1(map(int, f.readlines())))