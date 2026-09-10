class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums) - 1
        def merger(left,right):
            i = j = 0
            ans = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    ans.append(left[i])
                    i += 1
                elif left[i] > right[j]:
                    ans.append(right[j])
                    j += 1

                elif left[i] == right[j]:
                    ans.append(left[i])
                    ans.append(right[j])
                    i += 1
                    j += 1
            ans.extend(left[i:])
            ans.extend(right[j:])

            return ans

        def merge(arr):
            if len(arr) == 0:
                return []
            if len(arr) == 1:
                return arr 
            mid = len(arr) // 2

            left  = merge(arr[:mid])
            right = merge(arr[mid:])

            return merger(left,right)
        nums = merge(nums)
        
        return nums[len(nums) - k]

        
        
        





        # n = len(nums)
        # def partition(arr,l,r):
        #     key = arr[r]
        #     start = l

        #     for i in range(l,r+1):
        #         if arr[i] <= key:
        #             arr[i],arr[start] = arr[start],arr[i]

        #             start += 1
        #     return start - 1

        # def quickSort(arr,l,r):

        #     if l >= r:
        #         return 

        #     p = partition(arr,l,r)

        #     quickSort(arr,l,p - 1)
        #     quickSort(arr,p+1,r)

        # quickSort(nums,0,n - 1)

        # return nums[n - k]
        