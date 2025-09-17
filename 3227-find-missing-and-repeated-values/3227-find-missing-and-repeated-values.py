class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        d=[grid[i][j] for i in range(0,len(grid)) for j in range(0,len(grid[i]))]
        result=[0,0]
        for items in range(1,len(d)+1):
            count=0
            for i in range(0,len(d)):
                if(items==d[i]):
                    count=count+1
            if count==0:
                result[1]=items
            if count==2:
                result[0]=items
        return result
        
