class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        mini=max(weights)
        maxi=sum(weights)
        min_counts=float('inf')
        
        while(mini <= maxi):
            min_limits=(maxi+mini)//2    #min_limits=mid(less)->count(greater)
            sumo=0
            counts=1

            for i in weights:
                sumo +=i
                if sumo > min_limits:
                    counts +=1               #counts=day
                    sumo=i
            
            if counts > days :
                mini=min_limits+1
            else:
                min_counts=min(min_counts ,min_limits)
                maxi=min_limits-1

        return min_counts
            


        