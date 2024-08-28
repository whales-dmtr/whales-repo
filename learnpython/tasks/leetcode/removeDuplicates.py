# Easy
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        idx = 0
        stack = []
        for i in range(len(nums)):
            if nums[i] not in stack:
                stack.append(nums[i])
                nums[idx] = nums[i]
                idx += 1
        return idx
