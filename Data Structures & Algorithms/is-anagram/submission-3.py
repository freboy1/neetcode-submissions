class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not(len(set(s)) == len(set(t))):
            return False

        set_s = set(s)

        for char in set_s:
            if s.count(char) != t.count(char):
                return False
        return True