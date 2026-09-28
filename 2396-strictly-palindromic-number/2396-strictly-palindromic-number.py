class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        flag = True
        for i in range(2,n-1):
            s = ''
            while i > 0:
                digit = i % 2
                s += str(digit)

                i //= 2
            ans = s[::-1]
            if ans != s:
                flag = False
                break
        if flag == False:
            return False
        else:
            return flag
                
            


        