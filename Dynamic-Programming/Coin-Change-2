class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not amount:
            return 1
        dp = [0]*(amount+1)
        for coin in coins:
            counter = 0
            while counter<=amount:
                if counter>=coin:
                    if counter==coin:
                        dp[counter]+=1
                    else:
                        if dp[counter-coin]:
                            dp[counter]+=dp[counter-coin]
                counter+=1
        return dp[amount]
        
