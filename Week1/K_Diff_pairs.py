class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        if k == 0:
            return len([n for n, count in collections.Counter(nums).items() if count > 1])
        
        snums = set(nums)
        pairs = len([n for n in snums if n - k in snums])
            
        return pairs