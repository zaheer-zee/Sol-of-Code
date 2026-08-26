class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        t = x
        summ = 0
        while t > 0:
            digit = t % 10
            summ += digit
            t //= 10
        # return summ
        if x % summ == 0:
            return summ
        else:
            return -1

        