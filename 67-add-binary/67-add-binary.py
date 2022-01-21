class Solution(object):
    def addBinary(self, a, b):

        _len = max(len(a), len(b))
        if len(a) < _len:
            a = (_len - len(a)) * '0' + a
        if len(b) < _len:
            b = (_len - len(b)) * '0' + b

        plus = 0
        result = ""

       
        for i in range(len(a))[::-1]:
            tmp = int(a[i]) + int(b[i]) + plus
            if tmp > 1:
                tmp -= 2
                plus = 1
            else:
                plus = 0

            result += str(tmp)

        if plus == 1:
            return '1' + result[::-1] 
        else: 
            return result[::-1]