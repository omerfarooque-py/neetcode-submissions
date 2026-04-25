class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            if target - num in hashmap:
                print(target - num)
                print("OK")
                print([num])
                return [hashmap[target-num], index]
            print(hashmap)
            hashmap[num] = index
            print([num])