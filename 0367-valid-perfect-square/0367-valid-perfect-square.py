class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 0
        high = num - 1
        ans = 0
        while low <= high:
            mid = (low+high) // 2
            if mid * mid <= num:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        if num == 1:
            return True
        elif ans*ans == num:
            return True
        else:
            return False 
        # for i in range(2,num):

        # tip = num**(0.5)
        # l = int(tip)

        # if l*l == num:
        #     return True
        # else:
        #     return False

        