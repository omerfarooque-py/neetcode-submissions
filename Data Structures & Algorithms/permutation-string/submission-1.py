class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = sorted(s1)
        permutation = []
        #L = 0
        n = len(s1)
        for R in s2:
            permutation.append(R)
            #print(sorted("".join(permutation)), sorted_s1)
            if sorted("".join(permutation)) == sorted_s1:
                return True
            if n == len(permutation):
                permutation.pop(0)
        return False


        