class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        new = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            new[i] = prefix
            prefix *= nums[i]

        suffix = 1

        for i in range(len(nums) - 1, -1, -1):
            new[i] *= suffix
            suffix *= nums[i]

        return new