class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        l1=(len(word1)-1)+(len(word2)-1)
        i=0
        j=0
        k=0
        while(i<=l1):
            if(j>len(word1)-1):
                res.join(word2[i])
                j+=1
                i+=1
            elif(k>len(word2)-1):
                res.join(word1[i])
                k+=1
                i+=1
            else:   
                res.join(word1[i])
                res.join(word2[i])
                i +=1
                j+=1
                k+=1
        return res
        

        