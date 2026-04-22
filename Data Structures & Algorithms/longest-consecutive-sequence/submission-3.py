class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = []
        counter = 1
        s_nums = sorted(nums)
        n = len(nums)-1
        print(s_nums)
        if n == -1:
          return 0
        for i in range(n):
          j=i+1
         # print(s_nums[j])
          if s_nums[j] - s_nums[i] == 1:
            counter+=1
          if s_nums[j] - s_nums[i] != 1 and s_nums[j] != s_nums[i]:
            output.append(counter)
            counter = 1
        output.append(counter)
        return max(output)
             
