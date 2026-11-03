class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        def find(left ,right):
            if left > right :
                return -1
            mid= (left +right)//2
            if nums[mid]==target :
                return mid
            elif nums[mid] > target :
                return find(left ,mid-1)
            else :
                return find(mid+1 ,right)
        return find(left ,right)
        