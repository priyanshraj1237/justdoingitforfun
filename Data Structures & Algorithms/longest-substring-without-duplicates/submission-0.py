class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        count=0
        result=0
        track=set()
        while(j<len(s)):
            if s[j] in track:
                track.remove(s[j])
                count=0
                i+=1
            track.add(s[j])
            count +=1
            result=max(count,result)
            j+=1
        return result

        