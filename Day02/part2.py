from __future__ import annotations
from Support.timing import timing

import os.path
import pytest
import time

DATA = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    h = 0
    v = 0
    aim = 0
    for line in lines:
        dir_s, val_s = line.split()
        val = int(val_s)
        if dir_s == 'forward':
            h += val
            v += val*aim
        if dir_s == 'down':
            aim += val
        if dir_s == 'up':
            aim -= val

    return h*v


TESTDATA = '''\
forward 5
down 5
forward 8
up 3
down 8
forward 2
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
            (TESTDATA, 900),
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
