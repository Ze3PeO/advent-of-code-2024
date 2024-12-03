import re


def p1(inp):
    return sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", inp))


def p2(inp):
    return p1(re.sub(r"don't\(\).*?do\(\)", "", inp))


with open("./input/week1/day3.txt") as file:
    lines = file.readlines()
    instructions = "".join(lines).replace("\n", "")

    print("part 1: {}".format(p1(instructions)))
    print("part 2: {}".format(p2(instructions)))
