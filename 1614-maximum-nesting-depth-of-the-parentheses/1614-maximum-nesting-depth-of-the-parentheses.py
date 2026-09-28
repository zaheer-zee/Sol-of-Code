class Solution:
    def maxDepth(self, s: str) -> int:
        bal = 0
        ans = []
        for i in s:
            if i == '(':
                bal += 1
            elif i == ')':
                bal -= 1
            
            ans.append(bal)
    
        return max(ans)


                

        