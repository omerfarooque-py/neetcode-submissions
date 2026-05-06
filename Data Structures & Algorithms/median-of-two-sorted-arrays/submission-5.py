class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merged_nums = nums1 + nums2

        merged_nums.sort()
        n = len(merged_nums)
        print(merged_nums[(n + 1) // 2 - 1])
        print((n + 1) // 2)
        if n % 2  != 0:
            return merged_nums[(n + 1) // 2 - 1]
        else:
            mid = (n + 1) // 2
            return (merged_nums[mid - 1] + merged_nums[mid]) / 2


        
