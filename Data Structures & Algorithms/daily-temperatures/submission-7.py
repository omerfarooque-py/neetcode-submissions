class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures) 
        res = [0] * n   
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]] :
               res[stack.pop()] = i - stack[-1]
            stack.append((i))
        return res