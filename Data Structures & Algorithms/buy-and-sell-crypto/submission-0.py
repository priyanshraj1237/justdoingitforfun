class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=0
        mini=float('inf')
        maxi=0
        while(i<len(prices)):
            mini=min(mini,prices[i])
            diff=prices[i]-mini
            maxi=max(maxi,diff)
            i+=1
        return maxi
        