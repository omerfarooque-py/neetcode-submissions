class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashset = {}
        for index, num in enumerate(numbers, 1):
            hashset[num] = index
        print(hashset)
        for index, num in enumerate(numbers, 1):
            if target - num in hashset:
                print(target, num)
                return[index, hashset[target - num]]
        

