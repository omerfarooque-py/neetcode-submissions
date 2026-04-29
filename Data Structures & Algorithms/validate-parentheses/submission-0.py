class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", "}": "{", "]": "["}
        #if 3 in hashmap: return True
        stack = []
        for char in s:
            if char in hashmap:
                top_element = stack.pop() if stack else "#"
                if hashmap[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack