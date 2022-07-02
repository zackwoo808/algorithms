#Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or not len(s):
          return ''
        
        res = ''
        
        for i in range(len(s)):
          tmp = self.helper(s, i, i)
          if len(tmp) > len(res):
            res = tmp
          tmp = self.helper(s, i, i+1)
          if len(tmp) > len(res):
            res = tmp
        
        return res
      
    def helper(self, s, l, r):
      while (l>=0 and r<len(s) and s[l] == s[r]):
        l-=1
        r+=1
      
      return s[l+1:r]
          