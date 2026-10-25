class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i=0
        result=[]
        while(i< len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            j=i+1
            k=len(nums)-1
            
            while(j<k):
                sumo=nums[i]+nums[j]+nums[k]
                if sumo == 0:
                    result.append([nums[i] ,nums[j] ,nums[k]])
                    j+=1
                    k-=1
                elif(sumo>0):
                    k-=1
                else:
                    j+=1
            i+=1
        return result
        
        