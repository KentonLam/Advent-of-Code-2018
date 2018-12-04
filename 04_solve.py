from collections import defaultdict

def get_time(line):
    return int(line.split(':')[1].split(']')[0])

def solve_1(chrono):
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

    #sol = list(sorted(guard_hours_asleep.items(), key=lambda x: sum(x[1]), reverse=True))[0]
    sol = list(sorted(guard_hours_asleep.items(), key=lambda x: max(x[1]), reverse=True))[0]
    print(sol)
    guard = sol[0]

    max_hours = max(guard_hours_asleep[guard])
    print(max_hours)
    print(guard_hours_asleep[guard].index(max_hours))





if __name__ == "__main__":
    with open('04_input.txt') as f:
        print(solve_1(list(f)))