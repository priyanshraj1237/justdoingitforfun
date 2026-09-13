class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans={}
        for i in ans:
            if i in ans:
                ans[i] +=1
            else:
                ans[i]=1
        count=0
        for i in ans:
            if ans[i]>1:
                return True
        return False
        
        