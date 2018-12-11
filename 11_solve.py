from functools import lru_cache

@lru_cache(maxsize=None)
def power_level(x, y, serial=9424):
    power = (x + 10)*y
    power += 9424
    power = power * (x + 10)
    power = (power // 100) % 10
    power -= 5
    return power

def solve_1(serial=9424):

    powers = {}

    for x in range(1, 300+1-3):
        for y in range(1, 300+1-3):

            total_power = 0
            for dx in range(3):
                for dy in range(3):
                    total_power += power_level(x+dx, y+dy, serial)

            powers[(x, y)] = total_power

    print(max(powers.items(), key=lambda x: x[1]))

if __name__ == "__main__":
    print(solve_1())
