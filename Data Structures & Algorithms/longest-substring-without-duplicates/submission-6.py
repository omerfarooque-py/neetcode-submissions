class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       seen = set()
       L = 0
       res  = 0

       for R in range(len(s)):
          while s[R] in seen:
            res = max(len(seen), res)
            seen.remove(s[L])
            L += 1
          seen.add(s[R])
        #  print(seen)
       return  max(len(seen), res)