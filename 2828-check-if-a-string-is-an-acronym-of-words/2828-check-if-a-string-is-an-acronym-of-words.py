class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        tip = ''
        for i in words:
            tip += i[0]
        
        if tip == s:
            return True
        else:
            return False
        