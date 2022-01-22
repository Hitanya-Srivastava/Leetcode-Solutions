class Solution:
   
    def singleNumber(self, A):
        result = 0
        for i in A:
            result ^= i
        return result