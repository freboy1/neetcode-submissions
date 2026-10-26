class Solution:
    def isPalindrome(self, s: str) -> bool:
        true_string = ""
        for char in s:
            if ord(char) >= 65 and ord(char) <= 90:
                true_string += chr(ord(char) + 32)
            elif ord(char) >= 97 and ord(char) <= 122:
                true_string += char
            elif ord(char) >= 48 and ord(char) <= 57:
                true_string += char
        
        is_good = True

        for i in range(len(true_string)):
            if true_string[i] != true_string[len(true_string) - i - 1]:
                is_good = False
                break

        return is_good