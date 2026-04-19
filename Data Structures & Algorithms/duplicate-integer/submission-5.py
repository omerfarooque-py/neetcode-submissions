class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if sorted((set(nums))) == sorted(nums):
            return False 
        else: 
            return True
