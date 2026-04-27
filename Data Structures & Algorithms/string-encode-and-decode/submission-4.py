class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
          res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
       #  print(s)
         res = []
         i = 0
         while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length =  int(s[i:j])
         #   print(length)
            i =  j + 1
          #  print(i)
            res.append(s[i: length + i])
          #  print(length+i)
            i+= length 

         return res    
          
             



