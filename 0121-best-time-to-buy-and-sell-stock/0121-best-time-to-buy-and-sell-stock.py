class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Max_Profit = 0
        Min_price = float('inf')
        for price in prices:
            if price < Min_price:
                Min_price = price
            else:
                profit = price - Min_price
                if profit > Max_Profit:
                    Max_Profit = profit
        return Max_Profit

        
        
        