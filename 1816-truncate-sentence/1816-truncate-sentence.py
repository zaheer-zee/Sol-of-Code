class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        tt = s.split(" ")
        pp = ''
        for i in range(k):
            pp += tt[i] + ' '
        return pp.strip()
        

        