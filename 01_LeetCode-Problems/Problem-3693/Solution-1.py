class Solution(object):
    def climbStairs(self, n, costs):
        INF = 9999999999999
        dp={}
        def helper(i):
            if i==0:
                return 0
            
            if i in dp:
                return dp[i]
            v1,v2,v3 =INF,INF,INF
            if i-1>=0:
                v1=1+helper(i-1)
            if i-2>=0:
                v2=4 + helper(i-2)
            if i-3>=0:
                v3=9 + helper(i-3)
            
            dp[i]=costs[i-1]+min(v1,v2,v3)
            return dp[i]
        
        helper(n)
        return dp[n]
                
                
        