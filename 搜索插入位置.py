class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        if nums[l-1] < target:
            return len(nums)
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] >= target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        return left
