class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        my_set = set()
        slow, fast = 0, 0

        while slow < len(s) and fast < len(s):
            if s[fast] in my_set:
                my_set.remove(s[slow])
                slow += 1

            else:
                my_set.add(s[fast])
                fast += 1

                if len(my_set) > length:
                    length = len(my_set)


        return length