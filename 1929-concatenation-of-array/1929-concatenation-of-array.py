class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        t = nums
        nums.extend(t)
        return nums
        