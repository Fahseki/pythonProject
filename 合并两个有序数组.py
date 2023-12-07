class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        a = b = 0
        nums = []
        while a < m or b < n:
            if a == m:
                nums.append(nums2[b])
                b += 1
            elif b == n:
                nums.append(nums1[a])
                a += 1
            elif nums1[a] < nums2[b]:
                nums.append(nums1[a])
                a += 1
            else:
                nums.append(nums2[b])
                b += 1
        nums1[:] = nums

