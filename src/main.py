from collections import deque

SYMBOL = '.'


def path_finder(maze: str) -> bool:
    table = maze.split("\n")
    max_len = len(table[0]) - 1
    stack = deque()
    stack.append([0, 0])
    checked = []

    while stack:
        element = stack.popleft()

        if element == [max_len, max_len]:
            return True

        if element in checked:
            continue

        # Check right
        if max_len >= element[0] and max_len >= element[1] + 1:
            if table[element[0]][element[1] + 1] == SYMBOL and [element[0], element[1] + 1] not in checked:
                stack.appendleft([element[0], element[1] + 1])

        # Check down
        if max_len >= element[0] + 1 and max_len >= element[1]:
            if table[element[0] + 1][element[1]] == SYMBOL and [element[0] + 1, element[1]] not in checked:
                stack.appendleft([element[0] + 1, element[1]])

        # Check up
        if element[0] - 1 >= 0 and element[1] >= 0:
            if table[element[0] - 1][element[1]] == SYMBOL and [element[0] - 1, element[1]] not in checked:
                stack.appendleft([element[0] - 1, element[1]])

        # Check left
        if element[0] >= 0 and element[1] - 1 >= 0:
            if table[element[0]][element[1] - 1] == SYMBOL and [element[0], element[1] - 1] not in checked:
                stack.appendleft([element[0], element[1] - 1])

        checked.append(element)

    return False
