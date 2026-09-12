class Solution:
    def isPalindrome(self, x: int) -> bool:
        t = str(x)
        u = t[::-1]
        if t == u:
            return True
        else:
            return False




        