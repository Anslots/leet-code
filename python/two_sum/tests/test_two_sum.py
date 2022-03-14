from unittest import TestCase
from ..two_sum import Solution

class TestSolution(TestCase):
    def setUp(self) -> None:
        self.subject = Solution()

    def test_example_one(self):
        assert self.subject.twoSum([2, 7, 11, 15], 9) == [0, 1]


