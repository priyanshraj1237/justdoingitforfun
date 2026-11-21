class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini=1
        maxi=max(piles)
        min_avg=float('inf')

        while(mini<=maxi):
            
            mid=(mini+maxi)//2
            hours=0
            for i in piles:
                q=i//mid
                r=i%mid
                if r!=0:
                    hours +=q+1
                else:
                    hours +=q
            if hours > h:
                mini=mid+1
            else:
                min_avg=min(min_avg,mid)
                maxi=mid-1
        
        return min_avg
        