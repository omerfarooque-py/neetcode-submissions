import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+" : operator.add,
            "-" : operator.sub,
            "*" : operator.mul,
            "/" : lambda a, b: int(a / b)
            }
        
        stack = []
        for token in tokens:
            if token in operators:
                tmp_2, tmp_1 = stack.pop(),stack.pop()
                stack.append(operators[token](tmp_1, tmp_2))
            else:
                stack.append(int(token))
        return stack[0]