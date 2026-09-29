class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        lis = []
        def check(n):
            temp = n
            flag = True
            while temp > 0:
                digit = temp % 10
                if digit == 0 or n % digit != 0:
                    flag = False
                    break
                temp //= 10
            return flag

        for i in range(left,right+1):
            if check(i):
                lis.append(i)
        return lis

        