class Solution:
  def merge(self, nums1, m, nums2, n):
    if(m == 0):
      for i in range(n):
        nums1[i] = nums2[i]
      return
    j = 0
    for i in range(m, m+n):
      nums1[i] = nums2[j]
      j += 1
    for i in range(m+n):
      min = i
      for j in range(i+1, m+n):
        if(nums1[j] < nums1[min]):
          min = j
      temp = nums1[i]
      nums1[i] = nums1[min]
      nums1[min] = temp

    return nums1
