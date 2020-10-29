class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10: return []
        
        se = set()
        ans = set()
        for i in range(len(s)-10+1):
            if s[i: i+10] in se:
                ans.add(s[i: i+10])
            else:
                se.add(s[i: i+10])
        return ans