class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        exp = sorted(heights)
        count = 0
        for i in range(len(exp)):
            if exp[i] != heights[i]:
                count += 1
        return count

        