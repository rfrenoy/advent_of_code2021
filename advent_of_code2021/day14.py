from typing import Optional
import math
import itertools

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def read_puzzle(filepath: str) -> tuple[str, dict[str, str]]:
    with open(filepath, 'r', encoding='utf-8') as in_f:
        lines = in_f.readlines()
    polymer_template = lines[0]
    if polymer_template[-1] == '\n':
        polymer_template = polymer_template[:-1]
    mapping_pair_letter = {}
    for line in lines[2:]:
        pair, to_insert = line.split(' -> ')
        if to_insert[-1] == '\n':
            to_insert = to_insert[:-1]
        mapping_pair_letter[pair] = to_insert
    return polymer_template, mapping_pair_letter


def step_on_polymer(polymer: str,
                    pair_insertion_dict: dict[str, str],
                    saved_pairs: Optional[dict[str, int]] = None) -> dict[str, int]:
    saved_pairs = saved_pairs or {}
    if len(saved_pairs.keys()) == 0:
        saved_pairs = {
            k: 0
            for k in
            [''.join(x) for x in list(itertools.product(ALPHABET, repeat=2))]
        }
        for i in range(len(polymer) - 1):
            pair = polymer[i:i + 2]
            saved_pairs[pair] += 1
    old_saved_pairs = saved_pairs.copy()
    for key_pair in old_saved_pairs:
        nb_pair_occurences = old_saved_pairs[key_pair]
        if nb_pair_occurences > 0:
            to_insert = pair_insertion_dict[key_pair]
            new_pairs = [
                f'{key_pair[0]}{to_insert}', f'{to_insert}{key_pair[1]}'
            ]
            for p in new_pairs:
                saved_pairs[p] += nb_pair_occurences
            saved_pairs[key_pair] -= nb_pair_occurences
    return saved_pairs


def max_minus_min_letter_occurences_in_pairs(pairs_count_dict: dict[str, int]) -> int:
    letter_count_dict = {x: 0 for x in ALPHABET}
    for pair_count in pairs_count_dict:
        for letter in pair_count:
            letter_count_dict[letter] += pairs_count_dict[pair_count]
    for pair_count in letter_count_dict:
        letter_count_dict[pair_count] = math.ceil(float(letter_count_dict[pair_count]) / 2)
    non_zero_values = [x for x in letter_count_dict.values() if x != 0]
    return max(non_zero_values) - min(non_zero_values)


if __name__ == '__main__':
    polymer, pair_mapping = read_puzzle('./inputs/day14.txt')
    saved_pairs = None
    for step in range(40):
        saved_pairs = step_on_polymer(polymer, pair_mapping, saved_pairs)
        if step == 9:
            print(max_minus_min_letter_occurences_in_pairs(saved_pairs))
    if saved_pairs:
        print(max_minus_min_letter_occurences_in_pairs(saved_pairs))