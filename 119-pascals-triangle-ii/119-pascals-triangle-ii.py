class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                result[i - j] += result[i - j - 1]
        return result


if __name__ == "__main__":
    assert Solution().getRow(3) == [1, 3, 3, 1]