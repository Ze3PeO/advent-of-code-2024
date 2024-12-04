import re


def p1(inp):
    # Determine grid dimensions
    height = len(inp)
    width = len(inp[0])

    # Horizontal lines
    searchable_lines = inp

    # Vertical lines
    searchable_lines = searchable_lines + [''.join(line[x] for line in inp) for x in range(width)]

    # Top-left to bottom-right diagonals
    for i in range(height + width - 1):
        line = ''.join(inp[y][i - y] for y in range(max(0, i - width + 1), min(i + 1, height)) if 0 <= i - y < width)
        searchable_lines.append(line)

    # Top-right to bottom-left diagonals
    for i in range(-height + 1, width):
        line = ''.join(inp[y][y - i] for y in range(max(0, i), min(height, width + i)) if 0 <= y - i < width)
        searchable_lines.append(line)

    return sum([len(re.findall(r"XMAS", line)) + len(re.findall(r"XMAS", line[::-1])) for line in searchable_lines])


def p2(inp):
    height = len(inp)
    width = len(inp[0])

    # Define valid MAS patterns
    patterns = ["MAS", "SAM"]

    # Initialize count
    count = 0

    # Traverse the grid for potential centers
    for y in range(1, height - 1):  # Avoid edges
        for x in range(1, width - 1):  # Avoid edges
            if inp[y][x] == "A":  # Center must be 'A'
                # Extract diagonal strings
                diagonal_1 = inp[y - 1][x - 1] + inp[y][x] + inp[y + 1][x + 1]
                diagonal_2 = inp[y - 1][x + 1] + inp[y][x] + inp[y + 1][x - 1]

                # Check if both diagonals are valid
                if diagonal_1 in patterns and diagonal_2 in patterns:
                    count += 1

    return count


with open("./input/week1/day4.txt") as file:
    lines = [line.strip() for line in file.readlines()]

    print("part 1: {}".format(p1(lines)))
    print("part 2: {}".format(p2(lines)))
