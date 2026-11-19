class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums.sort()
        s = nums[::-1]
        lis = []
        for i in s:
            if i in lis:
                continue
            else:
                lis.append(i)
        if len(lis) >= 3:
            return lis[2]
        else:
            return lis[0]