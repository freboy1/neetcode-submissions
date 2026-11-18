class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        value = None
        for char in tokens:
            if char in "+-*/":
                first = None
                if value is None:
                    value = stack.pop()
                first = int(value)
                second = int(stack.pop())

                if char == "+":
                    value = first + second
                elif char == "-":
                    value = second - first
                elif char == "*":
                    value = first * second
                elif second * first >= 0:
                    value = int(second / first)
                else:
                    value = math.trunc(second / first)
                    
                stack.append(value)
                value = None
            else:
                stack.append(char)
        # print(stack)
        return int(stack[-1])