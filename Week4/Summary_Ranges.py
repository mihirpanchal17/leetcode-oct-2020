class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
          return []
        
        first = nums[0]
        last = nums[0]
        r=[]
        
        for num in nums:
          if num > last+1:
            r.append(f"{first}->{last}" if first != last else f"{first}")
            first = num
          last = num
          
        r.append(f"{first}->{last}" if first != last else f"{first}")
          
        return r