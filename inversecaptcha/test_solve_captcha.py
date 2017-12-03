from unittest import TestCase

from inversecaptcha.InverseCaptcha import solve_captcha


class TestSolveCaptcha(TestCase):

    def test_solve_captcha(self):
        input_to_expected = {"1122": 3, "1111": 4, "1234": 0, "91212129": 9}
        for test_input, expected_result in input_to_expected.items():
            self.assertEqual(expected_result, solve_captcha([int(x) for x in test_input]))  # List comprehension
