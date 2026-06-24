class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0
        result = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                result.append(nums2[j])
                j += 1
            elif nums1[i] == nums2[j]:
                result.append(nums1[i])
                result.append(nums2[j])
                i += 1
                j += 1
        while i < m:
            result.append(nums1[i])
            i += 1
        while j < n:
            result.append(nums2[j])
            j += 1
        nums1[:] = result










        # result = []
        # def tip(nums1,nums2,i,j):
        #     if i == len(nums1) or j == len(nums2):
        #         return 
        #     if nums1[i] < nums2[j]:
        #         result.append(nums1[i])
        #         return tip(nums1,nums2,i+1,j)
        #     if nums2[j] < nums1[i]:
        #         result.append(nums2[j])
        #         return tip(nums1,nums2,i,j+1)
        #     return result
        # tip(nums1,nums2,0,0)
        


        