class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merger(left,right):
            ans = []
            i = 0
            j = 0
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
            left = merge(arr[:mid])
            right = merge(arr[mid:])

            return merger(left,right)

        return merge(nums)
