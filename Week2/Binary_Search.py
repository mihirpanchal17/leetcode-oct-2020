class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(start,end):
            if start>end:
                return -1
            m=(start+end)//2
            if target==nums[m]:
                return m
            elif target<nums[m]:
                return binary(start,m-1)
            else:
                return binary(m+1,end)
        return binary(0,len(nums)-1)