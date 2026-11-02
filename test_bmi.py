import lab2.bmi as bmi 

def test_calc_bmi_function_normal_weight():
    expected = 0
    result = bmi.calculate_bmi(height=1.85, weight=65)
    assert (result == expected)


def test_calc_bmi_function_over_weight():
    expected = 1
    result = bmi.calculate_bmi(height=1.85, weight=95)
    assert (result == expected)


def test_calc_bmi_function_under_weight():
    expected = -1
    result = bmi.calculate_bmi(height=1.85, weight=35)
    assert (result == expected)

