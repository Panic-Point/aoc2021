from __future__ import annotations

import argparse
import os.path

import pytest

import time

DATA = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    numbers = [int(line) for line in s.splitlines()]
    for n in numbers:
        pass

    lines = s.splitlines()
    for line in lines:
        pass
    # TODO: implement solution here!
    return 0


TESTDATA = '''\
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
            (TESTDATA, 1),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    start = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=DATA)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))
    print('Time taken {} seconds'.format(round(time.time() - start, 2)))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())