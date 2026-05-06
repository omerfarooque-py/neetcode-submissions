class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        stock = 0
        best_day = 0
        for i in range(len(prices)):
            print(profit, stock, best_day)
            if i == 0:
                stock = prices[i]
                #profit = prices[i]
                continue 
            if prices[i] < stock:
                profit = max(profit, best_day - stock)
                stock = prices[i]
                best_day = prices[i]
            else:
                best_day = max(prices[i], best_day)
       
        return max(profit, best_day - stock)
                

             
