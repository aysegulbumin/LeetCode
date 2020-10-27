class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        
        if obstacleGrid == []:
            return 0
        if obstacleGrid[0] == []:
            return 0
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        
        #Initialize a matrix : Matrix
        Matrix=[]
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(0)
            Matrix.append(row)
        
        def calculate(obstacleGrid, m, n):
            a = 0
            b = 0
            # edge cases
            if(m==rows-1 and n==cols-1):
                if obstacleGrid[m][n]==1:
                    return 0
                else:
                    return 1
            if(m==rows-1):
                if obstacleGrid[m][n+1]==1:
                    return 0
                else:
                    return Matrix[m][n+1]
            if (n==cols-1):
                if obstacleGrid[m+1][n]==1:
                    return 0
                else:
                    return Matrix[m+1][n]
            if(obstacleGrid[m+1][n]!=1):
                a=Matrix[m+1][n]
            if(obstacleGrid[m][n+1]!=1):
                b=Matrix[m][n+1]
            return a+b
        
        index_m=rows-1
        index_n=cols-1
        
        if(obstacleGrid[index_m][index_n]==1):
            return 0
        if(obstacleGrid[0][0]==1):
            return 0
        
        while index_m >=0:
            while index_n>=0:
                Matrix[index_m][index_n]=calculate(obstacleGrid,index_m,index_n)
                index_n -=1
            index_n = cols-1
            index_m -= 1
        
            
        return Matrix[0][0]
        
