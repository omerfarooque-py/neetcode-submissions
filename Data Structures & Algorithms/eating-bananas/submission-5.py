class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        res = R

        while L <= R:
            k = L + (R - L) // 2
            hours = 0
            for pile in piles:
                time = (pile + k - 1) // k
                hours += time
            if hours > h: #if taken time is greater than expected increae eating rate per hour #K
                L = k + 1
            elif hours <= h: #if time taken to finish bananas is lesser decreas k
                #print(f"found a min val {k} that takes lesser time than: {R} and is within bounds of: {h} ")
                #print(f"printing time taken... {hours}, expected time: {h} or less.")
                R = k - 1
                res = k
        return res


        


