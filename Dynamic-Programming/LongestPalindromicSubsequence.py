class Solution:
    def longestPalindromeSubseq(self, str: str) -> int:
        
#         dp[0][4] = 2 maxlen = 2
#         dp[0][3] = 2
#         dp[0][2] = 2
#         dp[0][1] = 2
#         dp[0][0] = 1
#         dp[1][4] = 2
#         dp[1][3] = 2
#         dp[1][2] = 2
#         dp[1][1] = 3
#         dp[2][4] = 2
#         dp[2][3] = 2
#         dp[2][2] = 1
#         dp[3][4] = 2
#         dp[3][3] = 1
#         dp[4][4] = 1
    # BBABB
#   0 1 2 3 4
#0  1 2 2 3
#1    1 1 1 
#2      1 1
#3        1 1
#4          1
        
        
        
      n = len(str)
 
      L = [[0 for x in range(n)] for x in range(n)]

      # Strings of length 1 are palindrome of length 1
      for i in range(n):
          L[i][i] = 1

      # Build the table. Note that the lower
      # diagonal values of table are
      # useless and not filled in the process.
      # The values are filled in a
      # manner similar to Matrix Chain
      # Multiplication DP solution (See
      # https://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
      # cl is length of substring
      for cl in range(2, n+1):
          for i in range(n-cl+1):
              j = i+cl-1
              if str[i] == str[j] and cl == 2:
                  L[i][j] = 2
              elif str[i] == str[j]:
                  L[i][j] = L[i+1][j-1] + 2
              else:
                  L[i][j] = max(L[i][j-1], L[i+1][j]);

      return L[0][n-1]
