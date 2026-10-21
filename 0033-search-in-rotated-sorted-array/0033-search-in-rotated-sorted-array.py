
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        # Find the minimum element (rotation pivot)
        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        tip = low

        # Decide which sorted half contains target
        if nums[tip] <= target <= nums[-1]:
            low = tip
            high = len(nums) - 1
        else:
            low = 0
            high = tip - 1

        # Binary search
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         ans = - 1

#         # minn = min(nums)
#         # maxx = max(nums)
#         def peak(nums):
            
#             low = 0
#             high = len(nums) - 1

#             while low < high:
#                 mid = (low + high) // 2

#                 if nums[mid] > nums[mid + 1]:
#                     high = mid
#                 else:
#                     low = mid + 1

#             return low

#         tip = peak(nums)
#         # if len(nums) == 1:
#         #     if nums[0] == target:
#         #         ans = 0
#         #     else:
#         #         ans = -1
#         #     return ans
#         # elif len(nums) == 2:
#         #     if nums[0] == target:
#         #         ans = 0
#         #     elif nums[1] == target:
#         #         ans = 1
#         #     else:
#         #         ans = -1
#         #     return ans
        
        
#         if nums[tip] == target:
#                 return tip
#         else:
#                 low1 = 0
#                 high1 = tip - 1

#                 while low1 <= high1:
#                     mid1 = (low1 + high1) // 2

#                     if nums[mid1] == target:
#                         return mid1
#                     elif nums[mid1] < target:
#                         low1 = mid1 + 1

#                     else:
#                         high1 = mid1 - 1

#                 low2 = tip + 1
#                 high2 = len(nums) - 1

#                 while low2 <= high2:
#                     mid2 = (low2 + high2) // 2

#                     if nums[mid2] == target:
#                         return mid2
                        

#                     elif nums[mid2] < target:
#                         low2 = mid2 + 1
#                     else:
#                         high2 = mid2 - 1

#                 return -1


            

        # return peak(nums)

        
        