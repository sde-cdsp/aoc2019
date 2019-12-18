
import sys, os
import math
from configs import INPUTS_DIR

def parse_input():
    with open(os.path.join(INPUTS_DIR, '1.txt')) as f:
        return [int(l) for l in f.readlines()]

def get_fuels():
    masses = parse_input()
    fuels = [math.trunc(mass/3) - 2 for mass in masses]
    return sum(fuels)

def get_all_fuels(masses):
    if any(masses):
        new_masses = [max(0, math.trunc(mass/3) - 2) for mass in masses]
        return sum(new_masses) + get_all_fuels(new_masses)
    return 0


if __name__ == '__main__':
    # print(get_fuels())
    print(get_all_fuels(parse_input()))
    # print(get_all_fuels([100756, 1969]))
