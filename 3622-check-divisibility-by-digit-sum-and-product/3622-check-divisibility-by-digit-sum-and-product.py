class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ = 0
        product = 1

        temp = n
        while temp > 0:
            digit = temp % 10
            summ += digit
            temp //= 10
        
        multemp = n
        while multemp > 0:
            digit = multemp % 10
            product *= digit
            multemp //= 10

        return n % (summ + product) == 0
        