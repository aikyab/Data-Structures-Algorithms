
#Python version
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

#Java Version
class Solution {
    public int longestPalindromeSubseq(String s) {
        int L[][] = new int[s.length()][s.length()];
        // for(int i=0;i<s.length();i++){
        //     L[i][i]=1;
        // }
        
        for(int cl=1;cl<=s.length();cl++){
            for(int i=0;i<(s.length()-cl)+1;i++){
                int j = (i+cl)-1;
                if(i==j){
                    L[i][j]=1;
                    continue;
                }
                if((s.charAt(i)==s.charAt(j)) && cl==2)
                    L[i][j] = 2;
                else if(s.charAt(i)==s.charAt(j))
                    L[i][j] = 2+L[i+1][j-1];
                else
                    L[i][j] = Math.max(L[i+1][j],L[i][j-1]);
                    
            }
        }
        return L[0][s.length()-1];
    }
}
