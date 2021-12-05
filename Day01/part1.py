from Support import timing

import os.path
import time

DATA = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    numbers = [int(line) for line in s.splitlines()]
    prev = numbers[0]
    count = 0
    for n in numbers[1:]:
        if n > prev:
            count += 1
        prev = n
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


def main() -> int:
    assert compute(TESTDATA) == 7
    start = time.time()

    with open(DATA) as f:
        print(compute(f.read()))
    timing.timing(start, time.time())

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
