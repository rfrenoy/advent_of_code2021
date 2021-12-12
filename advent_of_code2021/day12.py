from typing import Dict, Generator, List

PATHS = []


def read_puzzle(filepath: str) -> Generator[List[str], None, None]:
    with open(filepath, 'r', encoding='utf-8') as in_f:
        for line in in_f.readlines():
            yield [
                char if char[-1] != '\n' else char[:-1]
                for char in line.split('-')
            ]


def init_dictionaries(connections):
    connect_dict = {}
    visit_dict = {}
    for start, end in connections:
        if start not in connect_dict:
            connect_dict[start] = []
            visit_dict[start] = 0
        if end not in connect_dict:
            connect_dict[end] = []
            visit_dict[end] = 0
        connect_dict[start].append(end)
        connect_dict[end].append(start)
    return connect_dict, visit_dict


def has_twice_visited_small_cave(visits_count_dict: Dict[str, int]) -> bool:
    for k in visits_count_dict:
        if str.lower(k) == k:
            if visits_count_dict[k] == 2:
                return True
    return False


def possible_paths(connections_mapping: Dict[str, List[str]],
                   visits_record: Dict[str, int], position: str,
                   can_visit_twice: bool) -> List[str]:
    c_mappings = connections_mapping[position]
    res = []
    if can_visit_twice:
        has_been_twice_in_a_small_cave = has_twice_visited_small_cave(
            visits_record)
    else:
        has_been_twice_in_a_small_cave = True
    for connection in c_mappings:
        if has_been_twice_in_a_small_cave:
            if visits_record[connection] == 0 or str.upper(
                    connection) == connection or connection == 'end':
                res.append(connection)
        else:
            if connection != 'start':
                res.append(connection)
    return res


def paths(connection_mappings,
          visits_records,
          position,
          past=None,
          can_visit_twice=False):
    past = past or []
    past.append(position)
    visits_records[position] += 1
    if position == 'end':
        PATHS.append(past)
        return
    next_paths = possible_paths(connection_mappings, visits_records, position,
                                can_visit_twice)
    if len(next_paths) == 0:
        return
    for next_path in next_paths:
        paths(connection_mappings, visits_records.copy(), next_path,
              list(past), can_visit_twice)


if __name__ == '__main__':
    puzzle = list(read_puzzle('./inputs/day12.txt'))

    # First star
    mapping, visits = init_dictionaries(puzzle)
    paths(mapping, visits, 'start', None, False)
    print(len(PATHS))

    # Second star
    PATHS = []
    mapping, visits = init_dictionaries(puzzle)
    paths(mapping, visits, 'start', None, True)
    print(len(PATHS))
