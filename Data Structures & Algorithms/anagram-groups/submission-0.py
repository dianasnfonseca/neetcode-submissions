class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {} 
        for word in strs:
            key = "".join(sorted(word))
            if key in s:
                s[key].append(word)
            else:
                s[key] = [word]
        return list(s.values())
