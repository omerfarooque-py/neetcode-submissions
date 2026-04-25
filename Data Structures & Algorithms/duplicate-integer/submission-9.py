class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       if sorted(nums) != sorted(set(nums)):
        print(sorted(nums), list(set(nums)))
        return True
       else:
        return False