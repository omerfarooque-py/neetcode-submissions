class Solution:
    def isPalindrome(self, s: str) -> bool:
      if s != "":
        L = 0
        R = len(s)-1
        while R > L:
          if not s[R].isalnum():
            R-=1
            continue
          if not s[L].isalnum():
            L+=1
            continue
          if s[R].lower() != s[L].lower():
            return False
          R-=1
          L+=1
        return True
      return False

        
