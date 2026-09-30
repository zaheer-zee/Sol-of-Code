class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []
        sol = []
        n = len(nums)
        initial = {}
        for i in nums:
            if i in initial:
                initial[i] += 1
            else:
                initial[i] = 1
        def check():
            if len(sol) == n:
                result.append(sol[:])
                return 
            for i in initial:
                if initial[i] > 0:

                    sol.append(i)
                    initial[i] -= 1

                    check()

                    initial[i] += 1
                    sol.pop()


        check()
        return result

        