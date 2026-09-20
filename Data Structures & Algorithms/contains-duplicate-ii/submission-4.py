class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #[1,0,1,1]        k=1
        i=0
        j=0
        track=set()
        if k<1:
            return False
        while(j<len(nums)):
            if(j-i > k):
                track.remove(nums[i])
                i+=1
            if nums[j] in track:
                return True
            track.add(nums[j])
            j+=1
        return False
            
        