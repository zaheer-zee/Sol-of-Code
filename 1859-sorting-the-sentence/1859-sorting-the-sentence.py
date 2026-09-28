class Solution:
    def sortSentence(self, s: str) -> str:
        dic = {}
        lis = s.split(" ")
        ans = ''
        for i in lis:
            n = len(i)    
            dic[i[-1]] = i[:n-1]

        for i in range(1,len(dic) + 1):
            ans += dic[str(i)] + " "

        return ans.strip()