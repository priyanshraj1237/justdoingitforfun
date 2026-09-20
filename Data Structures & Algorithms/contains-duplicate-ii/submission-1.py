class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        j=0
        if k<=1 :
            return False
        while(j<len(nums)):
            if(j-i > k):
                i+=1
            if nums[i]==nums[j]:
                return True
            j+=1
        return False
            
        