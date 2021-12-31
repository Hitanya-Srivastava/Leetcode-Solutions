
class Solution:
   
    def searchInsert(self, A, target):
        if len(A)==0: return 0
        for i in range(len(A)):
            if A[i]>=target:
               return i
        return len(A)