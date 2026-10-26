class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        score = 0
        ans = 0
        i , j = 0, n-1
        while i <= j:
            if tokens[i] <= power:
                score += 1
                power -= tokens[i]
                ans = max(ans,score)
                i += 1


            else:
                if score > 0:
                    power += tokens[j]
                    score -= 1
                    j -= 1
                else:
                    break
        return ans

            