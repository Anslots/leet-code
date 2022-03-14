class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        is_palindrome = True if str_x[::-1] == str_x else False
        return is_palindrome
