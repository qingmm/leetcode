# my stupid solution
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = []
        outputS = ''
        i = 0
        if numRows == 1:
            return s
        while i < len(s):
            if i % (numRows - 1) == 0:
                l = [''] * numRows
                for j in range(numRows):
                    if i + j < len(s):
                        l[j] = s[i + j]
                rows.append(l)
                i += numRows
            else:
                l = [''] * numRows
                l[numRows - i % (numRows - 1) - 1] = s[i]
                rows.append(l)
                i += 1
        for i in range(numRows):
            for j in range(len(rows)):
                outputS += rows[j][i]
        return outputS
  
# a very beautiful solution by @pharrellyhy from LeetCode, and I just did a little adjustment
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2 or len(s) < numRows:
            return s
        step, index = - 1, 0
        r = [''] * numRows
        for ch in s:
            r[index] += ch
            if index == 0 or index % (numRows - 1) == 0:
                step = - step
            index += step
        return ''.join(r)
