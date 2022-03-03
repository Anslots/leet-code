from unittest import TestCase
from ..is_palindrome import Solution

class TestSolution(TestCase):
    def setUp(self) -> None:
        self.subject = Solution()

    def test_example_11(self):
        assert self.subject.isPalindrome(11)

    def test_example_12(self):
        assert not self.subject.isPalindrome(12)

    def test_example_121(self):
        assert self.subject.isPalindrome(121)

