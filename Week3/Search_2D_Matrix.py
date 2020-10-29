
class Solution:
    def binary(nums,start,end,key):
        
        while start<=end:
            mid = (start+end)//2
            
            if nums[mid] == key:
                return True
            
            elif key<nums[mid]:
                end = mid-1
                
            elif key>nums[mid]:
                start = mid+1
                
            else:
                return False
            
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if (n:=len(matrix))==0 or (m:=len(matrix[0]))==0:
            return False

        for i in range(n):
            if target<= matrix[i][m-1]:
                if Solution.binary(matrix[i],0,m-1,target):
                    return True
                else:
                    return False
                
            
            elif matrix[i][0]>target:
                return
