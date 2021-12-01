from advent_of_code2021.day1 import nb_increased_values


def test_nb_increase_should_return_the_number_of_times_values_have_increased():
    # given
    inputs = [1, 2, 3]
    sequence_length = 1

    # when
    nb_increased = nb_increased_values(inputs, sequence_length)

    # then
    assert nb_increased == 2
    
def test_nb_increase_should_return_the_number_of_times_values_have_increased_taking_sequence_length_into_account():
    # given
    inputs = [1, 2, 3]
    sequence_length = 2

    # when
    nb_increased = nb_increased_values(inputs, sequence_length)

    # then
    assert nb_increased == 1

def test_nb_increase_should_return_zero_on_decreasing_list():
    # given
    inputs = [3, 2, 1]
    sequence_length = 1

    # when
    nb_increased = nb_increased_values(inputs, sequence_length)

    # then
    assert nb_increased == 0
    
