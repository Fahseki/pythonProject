class Solution(object):
    def removeElement(self, nums, val):
        L = len(nums)
        left = right = 0
        while right < L:
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left
