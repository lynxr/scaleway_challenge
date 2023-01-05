import unittest
from collections import namedtuple

from challenge.second.no_duplicate import de_duplicate, de_duplicate_list_comprehension

TestData = namedtuple('TestData', ['data', 'expected'])


class TestSecondChallenge(unittest.TestCase):
    TEST_DATA_SUCCESS = [
        # base task
        TestData([0, 1, 3, 1, 3, 5, 7, 9, 0], [0, 1, 3, 5, 7, 9]),

        # empty collection edge case
        TestData([], []),

        # only duplicates
        TestData([0, 0, 0, 0], [0]),

        # mixed types
        TestData([0, '1', '2', 'a', 'b'], [0, '1', '2', 'a', 'b']),

        # duplicates with mixed types
        TestData([0, '1', '2', 'a', 'b', 0, 'b'], [0, '1', '2', 'a', 'b']),

        # non sorted
        TestData([9, 5, 10, 50, 1, -1, -1, 5], [9, 5, 10, 50, 1, -1]),
    ]

    def test_remove_duplicates(self):
        for test_data in self.TEST_DATA_SUCCESS:
            assert de_duplicate(test_data.data) == test_data.expected
            assert de_duplicate_list_comprehension(test_data.data) == test_data.expected
