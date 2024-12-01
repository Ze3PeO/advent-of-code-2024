def p1(inp):
    loc_ids = [list(map(int, line.strip().split("   "))) for line in inp]
    left_list, right_list = sorted([int(loc_id[0]) for loc_id in loc_ids]), sorted([int(loc_id[1]) for loc_id in loc_ids])
    return sum(abs(left - right) for left, right in zip(left_list, right_list))


def p2(inp):
    loc_ids = [list(map(int, line.strip().split("   "))) for line in inp]
    id_count = {}
    for _, loc_id in loc_ids:
        id_count[loc_id] = id_count.get(loc_id, 0) + 1
    return sum(left * id_count.get(left, 0) for left, _ in loc_ids)


with open('./input/week1/day1.txt') as file:
    lines = file.readlines()

    print('part 1: {}'.format(p1(lines)))
    print('part 2: {}'.format(p2(lines)))
