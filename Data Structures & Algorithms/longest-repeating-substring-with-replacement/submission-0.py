class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s=sorted(s)
        hashmap={}
        greater=float('-inf')
        for i in s:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
            greater=max(greater,hashmap[i])
        return greater+k
        