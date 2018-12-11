from functools import lru_cache
import pandas as pd


@lru_cache(maxsize=None)
def power_level(x, y, serial=9424):
    assert 1 <= x <= 300 and 1 <= y <= 300
    # print(x, y)
    power = (x + 10)*y
    power += serial
    power = power * (x + 10)
    power = (power // 100) % 10
    power -= 5
    return power

def solve_1(serial=9424):
    powers = {}

    for size in (range(17, 300+1)):
        print()
        print('size', size)
        for x in range(1, 300+1):
            # print('x', x)
            for y in range(1, 300+1):
                if max(x, y) >= 300-size:
                    continue
                # from math import inf
                # prev_power = -inf
                total_power = 0
                for dx in range(size):
                    for dy in range(size):
                        total_power += power_level(x+dx, y+dy, serial)
                powers[(x, y, size)] = total_power
                # if total_power < prev_power:
                #     break 
                # prev_power = total_power
        print(max(powers.items(), key=lambda x: x[1]))

    # for y in range(1, 301):
    #     for x in range(1, 301):
    #         print(powers[(x, y)], end=', ')
    #     print() 

    for partition in (2, 3, 5, 10, 30, 50):
        parts = {}

        for x in range(1, (300-partition)//partition + 1):
            for y in range(1, (300-partition)//partition + 1 ):
                x_ = x*partition
                y_ = y*partition
                
                part = 0
                for dx in range(partition):
                    for dy in range(partition):
                        part += powers[(x_+dx, y_+dy)]
                parts[(x_, y_)] = part

        for x in range(1, (300-partition)//partition + 1):
            for y in range(1, (300-partition)//partition + 1 ):
                x_ = x*partition
                y_ = y*partition
                print(parts[(x_, y_)], end=', ')
            print() 
        

        print()
        print()

def prefixSum2D(a) : 
    C = len(a[0])
    R = len(a)
    psa = [[0 for x in range(C)]  
              for y in range(R)]  
    psa[0][0] = a[0][0] 
  
    # Filling first row  
    # and first column 
    for i in range(1, C) : 
        psa[0][i] = (psa[0][i - 1] + 
                       a[0][i]) 
    for i in range(0, R) : 
        psa[i][0] = (psa[i - 1][0] + 
                       a[i][0]) 
  
    # updating the values in  
    # the cells as per the  
    # general formula 
    for i in range(1, R) : 
        for j in range(1, C) : 
  
            # values in the cells of  
            # new array are updated 
            psa[i][j] = (psa[i - 1][j] + 
                         psa[i][j - 1] - 
                         psa[i - 1][j - 1] + 
                           a[i][j]) 
    return psa

def solve_2(serial=9424):
    import numpy as np 
    array = np.ndarray((300, 300))
    for y in range(300):
        for x in range(300):
            array[y][x] = power_level(x+1, y+1, serial)

    prefixes = np.array(prefixSum2D(array.tolist()))

    powers = {}
    for size in range(1, 301):
        print('size', size)
        for x in range(1, 301-size-1):
            for y in range(1, 301-size-1):
                this_power = prefixes[y+size-2][x+size-2]
                # conditional inclusion/exclusion using prefix sums
                if x > 1:
                    this_power -= prefixes[y+size-2][x-2]
                if y > 1:
                    this_power -= prefixes[y-2][x+size-2]
                if x > 1 and y > 1:
                    this_power += prefixes[y-2][x-2]
                    
                powers[(x, y, size)] = this_power

        # print(max(powers.items(), key=lambda x: x[1]))
    print(max(powers.items(), key=lambda x: x[1]))

    print(array)


if __name__ == "__main__":
    print(solve_2())
