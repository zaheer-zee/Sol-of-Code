class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        summ = 0
        ss = str(n)
        lis = {}

        for i in ss:
            if i in lis:
                lis[i] += 1
            else:
                lis[i] = 1
        
        
        for i in lis:
            summ += int(i)*int(lis[i])
        return summ
        
        