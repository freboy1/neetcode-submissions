class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        min_temp = None

        for i in range(len(temperatures)):
            if len(stack) == 0:
                min_temp = temperatures[i]
                stack.append([temperatures[i], i])
                # print(stack)
                # print()
                continue
            
            if min_temp is None or temperatures[i] > min_temp:
                j = 0

                while len(stack) > 0:
                    poped = stack.pop()

                    if temperatures[i] > poped[0]:
                        answer[poped[1]] = i - poped[1]
                        min_temp = poped[0]
                    else:
                        min_temp = temperatures[i]
                        stack.append(poped)
                        break
            else:
                min_temp = temperatures[i] 
            stack.append([temperatures[i], i])

        # print(stack)

        return answer