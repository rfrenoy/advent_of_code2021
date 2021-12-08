from advent_of_code2021.day8 import count_occurences, decode_mapping, find_one, find_seven, _or, count_occurences, decode_output


def test_segments_from_signals_should_return_segment_mapping():
    # Given
    signals = [
        "be", "cfbegad", "cbdgef", "fgaecd", "cgeb", "fdcge", "agebfd",
        "fecdb", "fabcd", "edb"
    ]

    # When
    segment_map = decode_mapping(signals)

    # Then
    assert segment_map == {
        'a': 2**3,
        'b': 2**0,
        'c': 2**6,
        'd': 2**5,
        'e': 2**1,
        'f': 2**2,
        'g': 2**4,
    }


def test_find_one_should_return_signal_with_two_characters():
    # Given
    signals = [
        "be", "cfbegad", "cbdgef", "fgaecd", "cgeb", "fdcge", "agebfd",
        "fecdb", "fabcd", "edb"
    ]

    # When
    one = find_one(signals)

    # Then
    assert one == 'be'


def test_find_seven_should_return_signal_with_three_characters():
    # Given
    signals = [
        "be", "cfbegad", "cbdgef", "fgaecd", "cgeb", "fdcge", "agebfd",
        "fecdb", "fabcd", "edb"
    ]

    # When
    one = find_seven(signals)

    # Then
    assert one == 'edb'


def test_or_should_return_segments_in_one_or_other():
    # Given
    a = 'abc'
    b = 'ac'

    # When
    or_a_b = _or(a, b)

    # Then
    assert or_a_b == 'b'

def test_count_occurences_should_return_number_of_segment_where_char_appears():
    # Given
    char = 'a'
    segments = ['ab', 'bc', 'aa']

    # When
    count_char_occurences_in_segments = count_occurences(char, segments)

    # Then
    assert count_char_occurences_in_segments == 2

def test_decode_output_should_return_figure_represented_by_display():
    # Given
    codes = ["fdgacbe", "cefdb", "cefbgd", "gcbe"]
    segment_map = {
        'a': 2**3,
        'b': 2**0,
        'c': 2**6,
        'd': 2**5,
        'e': 2**1,
        'f': 2**2,
        'g': 2**4,
    }


    # When
    outputs = [decode_output(code, segment_map) for code in codes]

    assert outputs == [8, 3, 9, 4]