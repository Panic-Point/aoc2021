from __future__ import annotations
from Support.timing import timing

import os.path
import time

DATA = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    h = 0
    v = 0
    for line in lines:
        dir_s, val_s = line.split()
        val = int(val_s)
        if dir_s == 'forward':
            h += val
        if dir_s == 'down':
            v += val
        if dir_s == 'up':
            v -= val

    return h*v


TESTDATA = '''\
forward 5
down 5
forward 8
up 3
down 8
forward 2
'''


def main() -> int:
    assert compute(TESTDATA) == 150
    start = time.time()

    with open(DATA) as f:
        print(compute(f.read()))
    timing(start, time.time())

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
