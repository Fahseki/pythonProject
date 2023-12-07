class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        L = len(nums)
        fast = slow = 1
        while fast < L:
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
