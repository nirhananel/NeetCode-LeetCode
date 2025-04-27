class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = 0
        sub = set()
        max_len = 0


        for r in range(len(s)):
            while s[r] in sub:
               sub.remove(s[l])
               l += 1
            sub.add(s[r])
            max_len = max(r - l +1, max_len)
            
        return max_len