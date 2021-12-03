from __future__ import annotations
from Support.timing import timing

import os.path
import time

DATA = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    cols = list(zip(*lines))
    gamma = ''
    epsilon = ''
    for c in cols:
        ones = sum([i == '1' for i in c])
        zeros = len(c) - ones
        if ones >= zeros:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return int(gamma, 2) * int(epsilon, 2)

TESTDATA = '''\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
'''


def main() -> int:
    assert compute(TESTDATA) == 198
    start = time.time()

    with open(DATA) as f:
        print(compute(f.read()))
    timing(start, time.time())

    return 0


if __name__ == '__main__':
    raise SystemExit(main())