from __future__ import annotations
from Support import timing

import os.path
import pytest
import time

DATA = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    numbers = [int(line) for line in s.splitlines()]
    prev = numbers[0]
    count = 0
    for i in range(3, len(numbers)):
        if numbers[i] > prev:
            count += 1
        prev = numbers[i-2]
    return count


TESTDATA = '''\
199
200
208
210
200
207
240
269
260
263
'''

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
            (TESTDATA, 5),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    start = time.time()

    with open(DATA) as f:
        print(compute(f.read()))
    timing.timing(start, time.time())

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
