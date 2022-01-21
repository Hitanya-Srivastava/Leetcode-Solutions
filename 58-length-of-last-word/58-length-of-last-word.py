class Solution:
   
    def lengthOfLastWord(self, A):
        l=0
        A=A[::-1]
        index=-1
        for c in A:
            index+=1
            if(c!=" "): #first non space character
                break
        
        if(index==-1):
            return 0
        else:
            for i in range(index,len(A)):
                if(A[i]!=" "):
                    l+=1
                else:
                    break
            return l