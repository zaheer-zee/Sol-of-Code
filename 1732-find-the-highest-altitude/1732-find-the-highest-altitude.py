class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = []
        ans.append(gain[0])
        for i in range(1,len(gain)):
            tip = ans[i-1] + gain[i]
            ans.append(tip)
        if max(ans) <= 0:
            return 0
        else:
            return max(ans)

        # for i in range(1,len(gain) - 1):
        #     tip = ans[i-1] - gain[i]
        #     ans.append(tip)
        # return ans


        # lis = []
        # lis.append(0)
        # # if 0 in gain:
        # #     gain.remove(0)
        # lis.extend(gain)

        # ans = []
        # ans.append(0)
        # return lis
        # for i in range(1,len(lis) - 1):
        #     tip = lis[i] - gain[i+1]
        #     ans.append(tip)
        # return ans
        


        # return lis
        # for i in range(1,len(gain) - 1):
        #     gain[i] = gain[i] - gain[i + 1]


        # return gain
        # gain.sort()
        # ans = 0
        # for i in range(len(gain)):
        #     if gain[i] == 0:
        #         ans = i
        #         break
        
        # if gain[ans] == gain[-1]:
        #     return 0
        # elif 0 not in gain:
        #     return 0
        # else:
        #     return gain[ans+1]
        