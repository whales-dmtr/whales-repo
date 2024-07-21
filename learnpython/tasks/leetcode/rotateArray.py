# Medium
class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k >= len(nums):
            for i in range(k):
                nums[:] = [nums[-1]] + nums[:-1]
        else:
            nums[:] = nums[-k:] + nums[:-k]