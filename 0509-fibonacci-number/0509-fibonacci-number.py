class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        return self.fib(n-1) + self.fib(n-2)

        # num1 = 0
        # num2 = 1
        # for i in range(n):
        #     sum = num1+ num2
        #     return sum
        #     num1 = num2
        #     num2 = sum
    # n = int(input())
    # print(fib(n))

    

        