class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #[1,0,1,1]        k=1
        i=0
        j=1
        while(j<len(nums)):
            if(j-i > k):
                i+=1
            if nums[i]==nums[j]:
                return True
            j+=1
        return False
            
        