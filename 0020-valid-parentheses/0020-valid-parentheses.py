class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        stk = []

        for i in list(s):
            if i == '(' or i == '[' or i == '{':
                stk.append(i)
            else:
                if len(stk) == 0:
                    return False
                top = stk.pop()
                if i == "]" and top != "[":
                    return False
                elif i == ")" and top != "(":
                    return False
                elif i == "}" and top != "{":
                    return False
        if len(stk) == 0:
            return True
        else:
            return False
                
        