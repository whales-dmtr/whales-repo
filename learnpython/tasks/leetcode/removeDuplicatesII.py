# Medium
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        idx = 0
        stack = []
        for i in range(len(nums)):
            if stack.count(nums[i]) < 2:
                stack.append(nums[i])
                nums[idx] = nums[i]
                idx += 1
        return idx
