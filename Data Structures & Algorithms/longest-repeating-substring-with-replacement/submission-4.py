class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        L = 0
        res = 0
        most_freq = 0
        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0 ) + 1
            most_freq = max(count[s[R]], most_freq)

            while (R - L + 1) - most_freq > k:
                count[s[L]] = count.get(s[L], 0) - 1
                L+=1
                res = max(res, R - L + 1)
            res = max(res, R - L + 1) 

        return res






         
