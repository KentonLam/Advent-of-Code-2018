from collections import defaultdict

def get_time(line):
    return int(line.split(':')[1].split(']')[0])

def parse_guard_sleeps(chrono):
    # mapping from guard number to sleep mapping
    # sleep mapping is minute to times asleep.
    guard_hours_asleep = defaultdict(lambda: [0]*60)
    chrono = list(sorted(chrono))

    time_asleep = None

    for line in chrono:
        line = line.rstrip()
        if ' begins shift' in line:
            code = line.split(' Guard #')[1].replace(' begins shift', '')
        elif ' falls asleep' in line:
            time_asleep = get_time(line)
        elif ' wakes up' in line:
            for i in range(time_asleep, get_time(line)):
                guard_hours_asleep[code][i] += 1

    return guard_hours_asleep

def solve_1(chrono):
    guard_hours_asleep = parse_guard_sleeps(chrono)

    sol = max(guard_hours_asleep.items(), key=lambda x: sum(x[1]))
    print(f'part 1: guard {sol[0]}, minute {sol[1].index(max(sol[1]))}')

def solve_2(chrono):
    guard_hours_asleep = parse_guard_sleeps(chrono)

    sol = max(guard_hours_asleep.items(), key=lambda x: max(x[1]))
    print(f'part 2: guard {sol[0]}, minute {sol[1].index(max(sol[1]))}')

if __name__ == "__main__":
    with open('04_input.txt') as f:
        input_list = list(f)
        solve_1(input_list)
        solve_2(input_list)