# Easy
class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) != 0 and len(nums2) != 0:
            for idx, val in enumerate(nums1):
                if idx == len(nums1) - len(nums2):
                    break

            nums1[idx:] = nums2
            nums1.sort()
        nums1.sort()
