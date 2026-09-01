class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dic = {}
        ans = []
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        for i in dic:
            if dic[i] > 1:
                ans.append(i)     
        return ans   