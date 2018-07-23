class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        lastLine = [1]
        nwline = []
        if(rowIndex == 0):
            return lastLine
        for i in range(1,rowIndex+1):
            for j in range(i+1):
                if(j == 0):
                    nwline.append(1)
                elif(j < i):
                    nwline.append(lastLine[j-1] + lastLine[j])
   
                    print(str(lastLine[j-1]))
                    print(str(lastLine[j]))
                if(j == i):
                    nwline.append(1)
            lastLine = nwline
            

            nwline = []
        return lastLine
                