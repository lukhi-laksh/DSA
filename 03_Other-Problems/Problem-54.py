class Solution:
    def minDominoRotations(self, tops, bottoms):
        
        for x in [tops[0] , bottoms[0]]:  
            top_swap , bottom_swap = 0,0
            
            for i in range(len(tops)):
            
                if tops[i] != x and bottoms[i] != x:
                    break
                if tops[i] != x:
                    top_swap +=1  
                if bottoms[i] != x:
                    bottom_swap +=1  
            else:
                return min(top_swap , bottom_swap) 
        
        return -1