class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> float:
        i=0
        j=0
        min_len=float('inf')
        sumo=0
        while(j<len(nums)):
            sumo+=nums[j]
            while sumo >= target :
                min_len=min(min_len ,j-i+1)
                sumo -=nums[i]
                i+=1

            j+=1
        if min_len ==float('inf') :
            return 0
        else :
            return min_len     