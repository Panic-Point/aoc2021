from Support.timing import timing
from collections import Counter

import os.path
import time

DATA = os.path.join(os.path.dirname(__file__), 'input.txt')


def parse(s: str):
    start, end = s.split(' -> ')
    first = tuple(start.split(','))
    second = tuple(end.split(','))
    return first, second

def compute(s: str) -> int:
    lines = s.splitlines()
    vents = list()
    coor = Counter()
    for line in lines:
        vents.append(parse(line))

    for vent in vents:
        start_x = int(vent[0][0])
        start_y = int(vent[0][1])
        end_x = int(vent[1][0])
        end_y = int(vent[1][1])

        if start_y == end_y:
            for i in range(min(start_x, end_x), max(start_x, end_x) + 1):
                coor.update([(i, start_y)])
        if start_x == end_x:
            for j in range(min(start_y, end_y), max(start_y, end_y) + 1):
                coor.update([(start_x, j)])
        if start_y != end_y and start_x != end_x:
            if start_x > end_x:
                x_dir = -1
            else:
                x_dir = 1
            if start_y > end_y:
                y_dir = -1
            else:
                y_dir = 1
            for t in range(0, max(start_y, end_y) - min(start_y, end_y) + 1):
                coor.update([(start_x + t * x_dir, start_y + t * y_dir)])
    return len([c for c in coor if coor[c] > 1])


TESTDATA = '''\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''


def main() -> int:
    assert compute(TESTDATA) == 12
    start = time.time()

    with open(DATA) as f:
        print(compute(f.read()))
    timing(start, time.time())

    return 0


if __name__ == '__main__':
    raise SystemExit(main())