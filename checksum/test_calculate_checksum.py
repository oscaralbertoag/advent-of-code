from unittest import TestCase

from checksum.Checksum import calculate_checksum


class TestCalculateChecksum(TestCase):

    def test_calculate_checksum(self):
        input_matrix = [[5, 1, 9, 5],
                        [7, 5, 3],
                        [2, 4, 6, 8]]
        checksum = calculate_checksum(input_matrix)
        self.assertEqual(18, checksum)
