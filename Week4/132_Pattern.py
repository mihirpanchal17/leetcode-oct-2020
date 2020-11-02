class Solution:
    def find132pattern(self, nums: [int]) -> bool:
        if len(nums) <= 2: return False
        st = [nums.pop()] # define a stack st and treat the input nums as another stack
        threshold = -float('inf') # function will return if found something smaller that threshold
        while st and nums:
            while nums and nums[-1] <= st[-1]: # first while loop push decreasing value from nums to st
                if nums[-1] < threshold:
                    return True
                st.append(nums.pop())
            if not nums:
                return False # nums empty indicated a monotonic decreasing pattern of nums
            while st and nums[-1] > st[-1]: # second while loop ensure st only contain decreasing value for the next round push
                threshold = max(st.pop(), threshold)
            st.append(nums.pop())
        return False