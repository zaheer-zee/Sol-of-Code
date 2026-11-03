class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxx = max(nums)

        summ = 0
        for i in nums:
            summ += (maxx - i)

        return summ
        