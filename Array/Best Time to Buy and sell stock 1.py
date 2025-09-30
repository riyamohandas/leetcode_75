class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=float('inf')
        profit=0
        for price in prices:

            if price<minprice:
                minprice=price
            else:
                profit=max(profit, price-minprice)
        return profit
