class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        lis = []
        sol = []
        n = len(nums)
        def check(i):
            if i == n:
                lis.append(sol[:])
                return 

            check(i+1)

            sol.append(nums[i])
            check(i+1)
            sol.pop()

        check(0)
        return lis

        #     lis = []
        #     sol = []
        #     l = 0
        # def check(l,nums):

        #     if len(sol) == len(lis):
        #         return 

        #     for i in lis:
        #         lis.append(sol)
        #         l += 1
        #         sol.append(i)

        #         check(nums)

