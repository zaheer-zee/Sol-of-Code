class Solution:
    def reverseDegree(self, s: str) -> int:
        # pos = 'abcdefghijklmnopqrstuvwxyz'
        pos = 'zyxwvutsrqponmlkjihgfedcba'
        pr = 0
        tt = []
        for i in s:
            count = 1
            for j in pos:
                if i == j:
                    break
                else:
                    count += 1

            tt.append(count)
        for i in range(len(tt)):
            pr += tt[i]*(i+1)
        return pr
        
        


        