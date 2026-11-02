import lab2.Lab2 as lab2 


def test_find_min_max():
    input_list = [10, 23, 31, 42, 25]
    expected = [10, 42]
    result = lab2.find_min_max(input_list)
    assert (result == expected)

def test_calc_average():
    input_list = [10, 23, 31, 42, 25]
    expected = 26.2
    result = lab2.calc_average(input_list)
    assert (result == expected)

def test_find_median_odd_number():
    input_list = [10, 23, 31, 42, 25]
    expected = 25
    result = lab2.calc_median_temperature(input_list)
    assert (result == expected)

def test_find_median_even_number():
    input_list = [10, 23, 32, 42]
    expected = 27.5
    result = lab2.calc_median_temperature(input_list)
    assert (result == expected)


def test_calc_average_round():
    input_list = [33, 24, 27, 25, 29, 31, 21]
    expected = 27.14285714
    result = lab2.calc_average(input_list)
    assert (round(result, 3) == round(expected, 3))