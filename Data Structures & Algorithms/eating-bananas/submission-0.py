class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i=1
        j=max(piles)
        min_avg=float('inf')

        while(i<=j):
            hours=0
            mid=(i+j)//2
            for i in piles:
                q=i//mid
                r=i%mid
                if r!=0:
                    hours +=q+1
                else:
                    hours +=q
            if hours > h:
                i=mid+1
            else:
                min_avg=min(min_avg,mid)
                j=mid-1
        
        return min_avg
        