class Solution:
    def isValid(self, s: str) -> bool:
        isValid = True if s[0] != s[-1] else False
        return isValid

