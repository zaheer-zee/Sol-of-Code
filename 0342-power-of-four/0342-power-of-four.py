class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        base = 4
        while n % base == 0:
            n //= base
        
        return n == 1
        