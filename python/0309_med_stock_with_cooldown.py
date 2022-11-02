''''''''''''
NOT COMPLETE
''''''''''''
from functools import reduce 

class Solution:
    def priceReducer():
        return None
    def maxProfit(self, prices) -> int:
        prof = 0
        currBuy = 0
        coolDown = False
        '''
        for ind, price in enumerate(prices):
        if prices[ind + 1] > currBuy 
            currBuy = price
        '''
        return prof
            

print(new Solution.maxProfit([1]))
'''
var maxProfit = function(prices) {
    return prices.reduce((acc, price) => ({
        prof: Math.max(price - acc.lastLow, acc.prof, 0),
        lastLow: Math.min(price,acc.lastLow), 
        }), {lastLow: 10 ** 4, prof: 0}).prof
};
'''
