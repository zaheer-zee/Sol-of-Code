class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        ans = 0
        for i in range(1,len(requests)):
            tip = abs(requests[i] - requests[i - 1])
            ans += tip
        return ans + requests[0]
        