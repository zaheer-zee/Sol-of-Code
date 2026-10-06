class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stk = []
        count = 0
        flag = True
        for i in s:
            if i == '(':
                stk.append(i)
            elif i == ")":
                if len(stk) != 0 and stk[-1] == '(':
                    stk.pop()
                else:
                    stk.append(i)
                

        return len(stk)
        