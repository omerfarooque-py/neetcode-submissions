class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hashmap = {}
        for num in nums:
          hashmap[num] = hashmap.get(num, 0) + 1
       # print(f"hashmap = {hashmap}, maximum val = {max(hashmap)}")
        for i in range(k):
            res.append(max(hashmap ,key=hashmap.get))
            del hashmap[max(hashmap ,key=hashmap.get)]
        return res
