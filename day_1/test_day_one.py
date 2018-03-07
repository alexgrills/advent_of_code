import day_1


def test_can_add_adjacent_digits():
    captcha = '1122'

    result = day_1.solve_captcha(captcha)

    assert result == 3


def test_can_handle_wrapping_match():
    captcha = '1111'

    result = day_1.solve_captcha(captcha)

    assert result == 4


def test_can_handle_no_match():
    captcha = '1234'

    result = day_1.solve_captcha(captcha)

    assert result == 0


def test_can_handle_only_one_wrapping_digit():
    captcha = '91212129'

    result = day_1.solve_captcha(captcha)

    assert result == 9


def test_can_solve_captcha_with_length():
    captcha = '1212'

    result = day_1.solve_captcha(captcha, int(len(captcha) / 2))

    assert result == 6


def test_can_solve_captcha_with_no_matches_with_length():
    captcha = '1221'

    result = day_1.solve_captcha(captcha, int(len(captcha) / 2))

    assert result == 0