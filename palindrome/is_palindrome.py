class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        revers = str_x[::-1]
        print(revers)
        if revers == str_x:
            return True
        else:
            return False
