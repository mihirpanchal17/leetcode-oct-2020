class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4: return max(nums)
        
        temp1 = [nums[0],nums[1],nums[0]+nums[2]]
        temp2= [0,nums[1],nums[2]]
        
        for i in range(3,len(nums)):
            temp1.append(max(temp1.pop(0)+nums[i],temp1[0]+nums[i]))
            temp2.append(max(temp2.pop(0)+nums[i],temp2[0]+nums[i]))
            
        return max(temp1[0],temp1[1],temp2[2])