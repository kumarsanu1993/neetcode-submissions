class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        if len(s) == len(t) and sorted_s == sorted_t:
            return True
        else:
            return False
    
