class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        left_max=[]
        left_maxi=0
        while(i < len(height)):
            left_maxi=max(left_maxi , height[i])
            left_max.append(left_maxi)
            i+=1

        # find the max right element for each indexes..
        right_max=[]
        right_maxi=0
        for j in range(len(height)-1 ,-1 ,-1):
            right_maxi=max(right_maxi,height[j])
            right_max.append(right_maxi)

        # we store element in opposite order
        right_max.reverse()

        #finding total_water
        water=0
        k=0
        while(k <len(height)):
            water += min(left_max[k] ,right_max[k])-height[k]
            k+=1

        return water


        