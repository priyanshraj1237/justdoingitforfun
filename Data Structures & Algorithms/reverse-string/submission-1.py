class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse(i,j):
            if i>j :
                return 
            else :
                s[i],s[j]=s[j],s[i]
                i +=1
                j-=1
                reverse(i,j)
        i=0
        j=len(s)-1
        reverse(i,j)
        
        
