class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        i =0
        j = matrix[i][-1]
        retarray=[]
        for i in range(len(matrix[0])):  
            retarray.append(matrix[i])
        for j in range(len(matrix[-1])):
            retarray.append(matrix[j])
