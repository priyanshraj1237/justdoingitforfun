class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        window=set()
        maxi=0
        count=0
        while(j<len(s)):
            if s[j] not in window:
                window.add(s[j])
                count=j-i+1
                j+=1
            else:
                window.remove(s[i])
                count -=1
                i+=1
            maxi=max(maxi,count)
        return maxi

        