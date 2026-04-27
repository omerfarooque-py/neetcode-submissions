class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] 
        n = len(nums)
        for i in range(n-1):
          prefix.append(nums[i] * prefix[i])
        #return prefix
        output = [0] * n 
        postfix = 1
        for i in range(n-1, -1, -1):
          output[i] = prefix[i] * postfix
          postfix = postfix * nums[i]
        return output


