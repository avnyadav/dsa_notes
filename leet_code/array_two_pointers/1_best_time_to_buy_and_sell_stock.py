
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days: int = len(prices)

        profit: int = 0

        d_buy, d_sell = 0, 1

        while d_sell<days:

            if prices[d_buy]<prices[d_sell]:
                profit = max(profit, prices[d_sell]-prices[d_buy])
            else:
                d_buy=d_sell
            d_sell+=1
        return profit
    
    

if __name__=="__main__":
    arr = [7,6,4,3,1]

    print(max_profit(arr))
