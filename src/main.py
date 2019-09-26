from collections import deque

SYMBOL = '.'
CHECKED_SYMBOL = 'x'


def path_finder(maze: str) -> bool:
    table = list(map(list, maze.split("\n")))
    max_len = len(table[0]) - 1
    stack = deque()
    stack.append([0, 0])

    while stack:
        element = stack.pop()

        x = element[1]
        y = element[0]

        if element == [max_len, max_len]:
            return True

        if table[y][x] == CHECKED_SYMBOL:
            continue

        # Check right
        if max_len >= y and max_len >= x + 1 and table[y][x + 1] == SYMBOL and table[y][x + 1] != CHECKED_SYMBOL:
            stack.appendleft([y, x + 1])

        # Check down
        if max_len >= y + 1 and max_len >= x and table[y + 1][x] == SYMBOL and table[y + 1][x] != CHECKED_SYMBOL:
            stack.appendleft([y + 1, x])

        # Check up
        if y - 1 >= 0 and x >= 0 and table[y - 1][x] == SYMBOL and table[y - 1][x] != CHECKED_SYMBOL:
            stack.appendleft([y - 1, x])

        # Check left
        if y >= 0 and x - 1 >= 0 and table[y][x - 1] == SYMBOL and table[y][x - 1] != CHECKED_SYMBOL:
            stack.appendleft([y, x - 1])

        table[y][x] = CHECKED_SYMBOL

    return False
