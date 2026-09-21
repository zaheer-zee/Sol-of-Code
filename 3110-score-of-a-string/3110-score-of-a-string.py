class Solution:
    def scoreOfString(self, s: str) -> int:
        pp = 0
        for i in range(len(s) - 1):
            pp += abs(ord(s[i]) - ord(s[i+1]))
        return pp
        