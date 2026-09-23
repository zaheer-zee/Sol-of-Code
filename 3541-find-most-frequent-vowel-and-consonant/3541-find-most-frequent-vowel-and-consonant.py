class Solution:
    def maxFreqSum(self, s: str) -> int:
        vo = {}
        co = {}
        for i in s:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                if i in vo:
                    vo[i] += 1
                else:
                    vo[i] = 1
            else:
                if i in co:
                    co[i] += 1
                else:
                    co[i] = 1
        vol = []
        col = []

        for i in vo:
            vol.append(vo[i])
        for i in co:
            col.append(co[i])
        if len(vol) == 0:
            return max(col)
        elif len(col) == 0:
            return max(vol)
        else:
            return max(vol) + max(col)

        