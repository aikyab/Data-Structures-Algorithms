class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount+1)
        dp[0] = 0
        # 20 30 40 A = 60
        # dp[0] = 0
        # dp[1] = 1
        # dp[2] = 2
        # 
        
        for c in coins:
            for a in range(1,amount+1):
                if a>=c:
                    dp[a] = min(dp[a],1+dp[a-c])
        return dp[amount] if dp[amount]!=amount+1 else -1
