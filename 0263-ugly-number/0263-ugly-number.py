class Solution:
    def isUgly(self, n: int) -> bool:
        check = [2,3,5]
        if n <= 0:
            return False
        # if n == 1:
        #     return True
        for p in check:
            while n % p == 0:
                n //= p
        return n == 1

        # for i in range([2,3,5])
        # def isPrime(n):
        #         if n < 2:
        #             return False
        #         for i in range(2,int(n**0.5) + 1):
        #             if n % i == 0:
        #                 return False
        #         return True
        # def check(n):
        #     if n < 2:
        #         return False
        #     return isPrime(n)
        # ans = []
        # if n == 1:
        #     return True 
        # if n < 1:
        #     return False
        # else:
        #     for i in range(2,n+1):
        #         if n % i == 0 and check(i):
        #             ans.append(i)
        # flag = True
        # for i in ans:
        #     if i != 2 and i != 3 and i != 5:
        #         flag = False
        #         break
        # return flag






        


        