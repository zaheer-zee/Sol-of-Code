class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        base = 3
        if n <= 0:
            return False
        while n % base == 0:
            n //= base 
        
        return 1 == n


        