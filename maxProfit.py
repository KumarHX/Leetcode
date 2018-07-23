class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = 99999
        maxprofit = 0
        for i in range(0,len(prices)):
            if (prices[i] < minprice):
                minprice = prices[i]
            elif (prices[i] - minprice > maxprofit):
                maxprofit = prices[i] - minprice;
        return maxprofit;
        
        
        
