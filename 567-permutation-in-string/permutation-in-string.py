class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = [0] * 26
        for c in s1:
            need[ord(c) - ord('a')] += 1
        window = [0] * 26
        for c in s2[:len(s1)]:
            window[ord(c) - ord('a')] += 1

        if window == need:
            return True

        for i in range(len(s1), len(s2)):
            in_char = s2[i]
            out_char = s2[i - len(s1)]
            window[ord(in_char) - ord('a')] += 1
            window[ord(out_char) - ord('a')] -= 1
            
            if window == need:
                return True 
        return False
