class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0
        for i in nums:
            tip = i
            while tip > 0:
                dum = tip % 10
                if digit == dum:
                    count += 1
                tip //= 10
        return count


        