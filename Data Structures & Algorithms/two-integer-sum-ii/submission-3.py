class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, number in enumerate(numbers):
          
          if hashmap and target - number in hashmap:
            return [hashmap[target - number] + 1, index + 1]
          hashmap[number] = index
