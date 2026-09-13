class Solution:
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        def ispallindrom(i , j):
            if(i>j):
                return True
            if(s[i]!=s[j]):
                return False
            else :
                i +=1
                j-=1
                return ispallindrom(i ,j)
        while(i<=j):
            if(s[j]==s[i]):
                i +=1
                j -=1
            else :
                return ispallindrom(i+1,j) or ispallindrom(i,j-1)
        return True
        