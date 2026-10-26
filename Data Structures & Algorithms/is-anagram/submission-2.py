class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not(len(set(s)) == len(set(t))):
            return False

        for char in s:
            if s.count(char) != t.count(char):
                return False
        return True