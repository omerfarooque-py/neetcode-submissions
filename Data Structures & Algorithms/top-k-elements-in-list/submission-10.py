class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      count = {}
      freq = [[] for _ in range(len(nums)+1)]
      for n in nums:
        count[n] = count.get(n, 0) + 1
      res = []
      for c, n in count.items():
        print(c, n)
        freq[n].append(c)
      print(freq)
      for i in range(len(nums), 0, -1):
        for n in freq[i]:
          res.append(n)
          if len(res) == k:
           return res