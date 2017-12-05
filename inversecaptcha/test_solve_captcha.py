from unittest import TestCase

from inversecaptcha.InverseCaptcha import solve_captcha, solve_captcha_2


class TestSolveCaptcha(TestCase):

    def test_solve_captcha(self):
        input_to_expected = {"1122": 3, "1111": 4, "1234": 0, "91212129": 9}
        for test_input, expected_result in input_to_expected.items():
            self.assertEqual(expected_result, solve_captcha([int(x) for x in test_input]))  # List comprehension

    def test_solve_captcha_2(self):
        input_to_expected = {"1212": 6, "1221": 0, "123425": 4, "123123": 12, "12131415": 4}
        for test_input, expected_result in input_to_expected.items():
            self.assertEqual(expected_result, solve_captcha_2([int(x) for x in test_input]))