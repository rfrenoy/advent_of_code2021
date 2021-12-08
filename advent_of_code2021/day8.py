from typing import Dict, Generator, List, Tuple

MAPPING = {
    'a': 2**0,
    'b': 2**1,
    'c': 2**2,
    'd': 2**3,
    'e': 2**4,
    'f': 2**5,
    'g': 2**6,
}

NUMBERS = {
    sum([2**x for x in [0, 1, 2, 3, 4, 5]]): 0,
    sum([2**x for x in [0, 1]]): 1,
    sum([2**x for x in [0, 2, 3, 5, 6]]): 2,
    sum([2**x for x in [0, 1, 2, 5, 6]]): 3,
    sum([2**x for x in [0, 1, 4, 6]]): 4,
    sum([2**x for x in [1, 2, 4, 5, 6]]): 5,
    sum([2**x for x in [1, 2, 3, 4, 5, 6]]): 6,
    sum([2**x for x in [0, 1, 5]]): 7,
    sum([2**x for x in [0, 1, 2, 3, 4, 5, 6]]): 8,
    sum([2**x for x in [0, 1, 2, 4, 5, 6]]): 9,
}


def find_word_of_length(segments: List[str], length: int) -> str:
    for segment in segments:
        if len(segment) == length:
            return segment
    raise Exception(f'A segment should have a word of size {length}')


def find_one(segments: List[str]) -> str:
    return find_word_of_length(segments, 2)


def find_seven(segments: List[str]) -> str:
    return find_word_of_length(segments, 3)


def find_four(segments: List[str]) -> str:
    return find_word_of_length(segments, 4)


def find_eight(segments: List[str]) -> str:
    return find_word_of_length(segments, 7)


def count_occurences(char: str, segments: List[str]) -> int:
    return sum([1 if char in x else 0 for x in segments])


def decode_mapping(segments: List[str]) -> Dict[str, int]:
    decoded_mapping = {}
    one = find_one(segments)
    seven = find_seven(segments)
    upper = _or(one, seven)
    decoded_mapping[upper] = 2**5
    four = find_four(segments)
    segments_in_four_not_seven = list(set(four).difference(set(seven)))
    eight = find_eight(segments)
    other_segments = [
        s for s in segments if s not in [one, four, seven, eight]
    ]
    for s in segments_in_four_not_seven:
        occurences = count_occurences(s, other_segments)
        if occurences == 5:
            decoded_mapping[s] = 2**6
        else:
            decoded_mapping[s] = 2**4
    remaining_chars = [
        s for s in list(set(''.join(segments)))
        if s not in decoded_mapping.keys()
    ]
    for s in remaining_chars:
        occurences = count_occurences(s, other_segments)
        if occurences == 3:
            decoded_mapping[s] = 2**3
        elif occurences == 4:
            decoded_mapping[s] = 2**0
        elif occurences == 5:
            decoded_mapping[s] = 2**1
        else:
            decoded_mapping[s] = 2**2
    return decoded_mapping


def decode_output(code: str, segment_mapping: Dict[str, int]):
    return NUMBERS[sum([segment_mapping[segment] for segment in code])]


def _or(a: str, b: str) -> str:
    return list(set(a).difference(set(b)).union(set(b).difference(set(a))))[0]


def clean_word(word: str) -> str:
    if word != '' and word[-1] == '\n':
        return word[:-1]
    return word


def clean_list(lst: List[str]) -> List[str]:
    cleaned_words = [clean_word(word) for word in lst]
    return [word for word in cleaned_words if word != '']


def read_puzzle(
        filepath: str) -> Generator[Tuple[List[str], List[str]], None, None]:
    with open(filepath, 'r', encoding='utf-8') as in_f:
        for line in in_f.readlines():
            signals, digits = line.split('|')

            yield (clean_list(signals.split(' ')),
                   clean_list(digits.split(' ')))


if __name__ == '__main__':
    puzzle = list(read_puzzle('./inputs/day8.txt'))
    res = []
    for signals, digits in puzzle:
        res.append(
            sum([1 if len(word) in [2, 3, 4, 7] else 0 for word in digits]))

    print(sum(res))

    res = []
    for signals, digits in puzzle:
        mapping = decode_mapping(signals)
        res.append(
            int(''.join([str(decode_output(x, mapping)) for x in digits])))
    print(sum(res))
