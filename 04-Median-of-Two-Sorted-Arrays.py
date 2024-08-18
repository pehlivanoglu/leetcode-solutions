class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_nums = []
        i1 = 0
        i2 = 0

        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] <= nums2[i2]:
                merged_nums.append(nums1[i1])
                i1 += 1
            else:
                merged_nums.append(nums2[i2])
                i2 += 1
        
        while i1 < len(nums1):
            merged_nums.append(nums1[i1])
            i1 += 1
        
        while i2 < len(nums2):
            merged_nums.append(nums2[i2])
            i2 += 1


        mid = len(merged_nums) // 2
        if len(merged_nums) % 2 != 0:
            return merged_nums[mid]
        else:
            return (merged_nums[mid-1] + merged_nums[mid]) / 2

# Runtime 77ms, beats %76.13
# Memory 16.87MB, beats %60.12
