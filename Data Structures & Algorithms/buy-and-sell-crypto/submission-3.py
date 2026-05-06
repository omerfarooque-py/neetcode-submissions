class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        stock = prices[0]

        for price in prices:
            profit = max(profit, price - stock)
            stock = min(stock, price)
        return profit 
        

                

             
