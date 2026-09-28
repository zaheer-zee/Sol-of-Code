class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        lo = 0
        # hi = len(nums) - 1
        # pos = lo 

        # for i in range(lo,hi+1):
        #     if nums[i] <= pivot:
        #         nums[i],nums[pos] = nums[pos],nums[i]
        #         pos += 1

        # nums[lo],nums[pos] = nums[pos], nums[lo]

        # return nums
        lo = []
        hi = []
        fihi = []
        for i in nums:
            if i < pivot:
                lo.append(i)
            else:
                hi.append(i)
        for i in hi:
            if i == pivot:
                lo.append(i)
        for i in hi:
            if i != pivot:
                fihi.append(i)

        lo.extend(fihi)
        nums[:] = lo
        return lo
        # return lo
        # hi.remove(10)
        # lo.extend(hi)

        # nums[:] = lo
        # return nums

        # p = 0
        # for i in nums:
        #     p += 1
        #     if i == pivot:
        #         break
        # def check(arr,lo,hi):
        #     nonlocal pivot
        #     start = lo
    
        #     for i in range(lo,hi+1):
        #         if arr[i] <= pivot:
        #             arr[i],arr[start] = arr[start],arr[i]
        #             start += 1
        #     arr[lo],arr[i] = arr[i],arr[lo]
            
        # check(nums,0,len(nums) - 1)
        # return nums      
                


        