class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        s_nums =sorted(nums)
        n = len(nums) -1
       # print(s_nums)
        for i in range(n):
            R = n
            L = i+1
            if i > 0 and s_nums[i] == s_nums[i-1]:
                continue
            while L < R:
                total = s_nums[i] + s_nums[L] + s_nums[R]
                if total > 0:
                    R-=1
                elif total == 0:
                    res.append([s_nums[i], s_nums[L], s_nums[R]])              
                    R-=1
                    L+=1
                    while L < R and  s_nums[L] == s_nums[L-1]:
                        L+=1
                    while L < R and s_nums[R] == s_nums[R+1]:
                        R-=1
                else:
                    L+=1
        return res