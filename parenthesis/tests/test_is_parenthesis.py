from unittest import TestCase
from ..parenthesis import Solution

class TestSolution(TestCase):
    def setUp(self) -> None:
        self.subject = Solution()

    def test_simple(self):
        assert self.subject.isValid("()")

    def test_simple_not_valid(self):
        assert not self.subject.isValid("(]")


   
