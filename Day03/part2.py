from __future__ import annotations
from Support.timing import timing
from copy import deepcopy

import os.path
import pytest
import time

DATA = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    o2 = list(lines)
    co2 = list(lines)
    for i in range(len(lines[0])):
        if len(o2) > 1:
            ones = len([item for item in o2 if item[i] == '1'])
            zeros = len([item for item in o2 if item[i] == '0'])
            if ones >= zeros:
                o2 = [item for item in o2 if item[i] == '1']
            else:
                o2 = [item for item in o2 if item[i] == '0']
        if len(co2) > 1:
            ones = len([item for item in co2 if item[i] == '1'])
            zeros = len([item for item in co2 if item[i] == '0'])
            if ones >= zeros:
                co2 = [item for item in co2 if item[i] == '0']
            else:
                co2 = [item for item in co2 if item[i] == '1']

    return int(o2[0], 2) * int(co2[0], 2)


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



@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
            (TESTDATA, 230),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    start = time.time()

    with open(DATA) as f:
        print(compute(f.read()))
    timing(start, time.time())

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
