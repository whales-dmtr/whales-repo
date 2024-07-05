# easy
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for key, main in enumerate(nums):
            for k, sub in enumerate(nums[(key+1):], start=(key+1)):
                if main + sub == target:
                    result = [key, k]
                    return result
