class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for char in s:
            if char in bracket:
                if len(stack) == 0:
                    return False
                poped = stack.pop()
                if poped != bracket[char]:
                    return False
            else:
                stack.append(char)
        # print(stack)
        return len(stack) == 0
        