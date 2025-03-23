class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mvalue = 0
        lowestValueIndex = 0
        markIndex = 1
        
        if len(prices) <= 1:
         return mvalue
        
        while True:
            value = prices[lowestValueIndex]-prices[markIndex]

            if value < mvalue:
                mvalue = value

            if markIndex >= len(prices)-1:
               return -mvalue

            if prices[lowestValueIndex] > prices[markIndex]:
               lowestValueIndex = markIndex

            markIndex+=1      
              