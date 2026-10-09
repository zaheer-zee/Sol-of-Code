class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        sol = []

        def check(x):
            if len(sol) == k:
                result.append(sol[:])
                return

            left = x
            inNeed = k - len(sol)

            if inNeed < left:
                check(x-1)

            sol.append(x)
            check(x-1)
            sol.pop()

        check(n)
        return result