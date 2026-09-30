class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)

        lis = []
        sol = []

        def check():
            if len(sol) == n:
                lis.append(sol[:])
                return 

            for i in nums:
                if i not in sol:
                    sol.append(i)
                    check()
                    sol.pop()


        check()

        return lis

            


        