class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
          return 0
        s_nums = sorted(nums)
        res = 1
        count = 1
        #print(s_nums)
        for i in range(len(nums)-1):
          if s_nums[i] == s_nums[i+1]:
            continue
          if s_nums[i] + 1 == s_nums[i+1]:
            count+=1
          else:
            res = max(count, res)
            count = 1
        res = max(count, res)
        return res
