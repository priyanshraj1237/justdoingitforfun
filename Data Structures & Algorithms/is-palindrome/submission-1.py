class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for i in s:
            if (i.isalpha() or i.isdigit()):
                if(i.isalpha()):
                    i=i.lower()
                res += i

        i=0
        j=len(res)-1
        def check(i,j):
            if i > j:
                return True
            if(res[i]!=res[j]):
                return False
            else :
                i +=1
                j-=1
                return check(i ,j)
        return check(i ,j)
        
        
        

        