from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lettsS = [char for char in s]
        lettsT = [char for char in t]

        return Counter(lettsS) == Counter(lettsT)



        