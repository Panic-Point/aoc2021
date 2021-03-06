from Support.timing import timing

import os.path
import time

DATA = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.split('\n\n')
    numbers = [int(x) for x in lines[0].split(',')]
    boards = [[int(y) for y in lines[i].split()] for i in range(1, len(lines))]
    marked = [[False for _ in board] for board in boards]
    boards_left = set(range(len(boards)))
    used = list()

    for n in numbers:
        used.append(n)
        for board in boards:
            if n in board:
                pos = board.index(n)
                b_pos = boards.index(board)
                marked[b_pos][pos] = True
                rows = [sum(marked[b_pos][j:j+5]) for j in range(0, len(marked[b_pos]), 5)]
                cols = [sum(marked[b_pos][j::5]) for j in range(5)]
                if 5 in rows or 5 in cols:
                    boards_left.discard(b_pos)
        if len(boards_left) == 1:
            loser = list(boards_left)[0]
        if len(boards_left) == 0:
            break
        else:
            continue

    unmarked = sum([x for x in boards[loser] if x not in used])
    return unmarked*used[-1]


TESTDATA = '''\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''


def main() -> int:
    assert compute(TESTDATA) == 1924
    start = time.time()

    with open(DATA) as f:
        print(compute(f.read()))
    timing(start, time.time())

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
