class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #0->1, 1->2, 2->3, 3->4
        n = len(nums)
        prefix = [0] * n
        prefix[0] = 1
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
        postfix = 1
        for i in range(n-1, -1, -1):
            #prefix[i] = prefix *
            prefix[i] = postfix * prefix[i]
            postfix = nums[i] * postfix
        return prefix



            

            





            