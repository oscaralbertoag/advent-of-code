from unittest import TestCase

from checksum.Checksum import calculate_checksum, calculate_checksum_2


class TestCalculateChecksum(TestCase):

    def test_calculate_checksum(self):
        input_matrix = [[5, 1, 9, 5],
                        [7, 5, 3],
                        [2, 4, 6, 8]]
        checksum = calculate_checksum(input_matrix)
        self.assertEqual(18, checksum)

    def test_calculate_checksum_2(self):
        input_matrix = [[5, 9, 2, 8],
                        [9, 4, 7, 3],
                        [3, 8, 6, 5]]
        checksum = calculate_checksum_2(input_matrix)
        self.assertEqual(9, checksum)
