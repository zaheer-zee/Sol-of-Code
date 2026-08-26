class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxVal = max(candies)
        nextcandy = []
        for i in candies:
            tip = i + extraCandies
            nextcandy.append(tip)
        ans = []
        for i in nextcandy:
            if i >= maxVal:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        