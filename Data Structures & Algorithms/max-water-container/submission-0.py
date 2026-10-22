class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        water=0
        max_water=0
        while(j>=i):
            h=min(heights[i],heights[j])
            water=h*(j-i)
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
            max_water=max(max_water ,water)
        return max_water
        