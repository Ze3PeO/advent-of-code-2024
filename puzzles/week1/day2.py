def p1(inp):
    reports = [list(map(int, line.strip().split(" "))) for line in inp]

    return sum(
        (all(b > a for a, b in zip(rep, rep[1:])) or all(b < a for a, b in zip(rep, rep[1:])))
        and all(0 <= abs(b - a) <= 3 for a, b in zip(rep, rep[1:]))
        for rep in reports
    )


def p2(inp):
    reports = [list(map(int, line.split())) for line in inp]

    return sum(
        any(
            (all(b > a for a, b in zip(mod_rep, mod_rep[1:])) or all(b < a for a, b in zip(mod_rep, mod_rep[1:])))
            and all(0 <= abs(b - a) <= 3 for a, b in zip(mod_rep, mod_rep[1:]))
            for mod_rep in (rep[:i] + rep[i + 1 :] for i in range(len(rep)))
        )
        for rep in reports
    )


with open('./input/week1/day2.txt') as file:
    lines = file.readlines()

    print('part 1: {}'.format(p1(lines)))
    print('part 2: {}'.format(p2(lines)))
