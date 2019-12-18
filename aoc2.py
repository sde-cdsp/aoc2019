import os

from configs import INPUTS_DIR


def parse_input():
    with open(os.path.join(INPUTS_DIR, '2.txt')) as f:
        l = f.readline().split(',')
        return [int(e) for e in l]

def add(l, position):
    l[l[position + 3]] = l[l[position + 1]] + l[l[position + 2]]
    return l, position + 4

def mul(l, position):
    l[l[position + 3]] = l[l[position + 1]] * l[l[position + 2]]
    return l, position + 4

def init_l(l):
    l[1] = 12
    l[2] = 2
    return l


# part 1
# if __name__ == '__main__':
#     l = parse_input()
#     l = init_l(l)
#     print(l)
#     pos = 0
#     while l[pos] != 99:
#         if l[pos] == 1:
#             l, pos = add(l, pos)
#         elif l[pos] == 2:
#             l, pos = mul(l, pos)
#         else:
#             print("Something went wrong: list", l)
#             print("Encountered opcode %d at pos %d" % (l[pos], pos))
#     print("HALT", l)

def init_l2(l, noun, verb):
    l[1] = noun
    l[2] = verb
    return l, 0

# part 2
if __name__ == '__main__':
    default_l = parse_input()
    pos = 0
    for i in range(100):
        for j  in range(100):
            l = default_l.copy()
            l, pos = init_l2(l, i, j)
            # print(i, j)
            while l[pos] != 99:
                if l[pos] == 1:
                    l, pos = add(l, pos)
                elif l[pos] == 2:
                    l, pos = mul(l, pos)
                # else:
                #     continue
            if l[0] == 19690720:
                print("RESULT", 100 * i + j)
                exit()
