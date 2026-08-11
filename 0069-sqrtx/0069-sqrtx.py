
class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        low = 1
        high = x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
        # ans = math.sqrt(x)
        # return floor(ans)
        # # ans = x**0.5
        # # return math.sqrt(x)