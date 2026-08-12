class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(left,right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                elif left[i] > right[j]:
                    result.append(right[j])
                    j += 1
                elif left[i] == right[j]:
                    result.append(left[i])
                    result.append(right[j])
                    i += 1
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        low = 0
        
        lis = merge(nums1,nums2)
        mid = (low + len(lis)-1) // 2
        if len(lis) % 2 == 1:
            return lis[mid]
        else:
            result = (lis[mid] + lis[mid+1])/2
            return result


        