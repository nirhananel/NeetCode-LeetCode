class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] +=1
            
            key = tuple(count)

            if key not in anagram_groups:
                anagram_groups[key] = []
            anagram_groups[key].append(s)

        return list(anagram_groups.values())