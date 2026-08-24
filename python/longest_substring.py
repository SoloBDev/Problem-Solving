class Solution:
  def length_of_longest_substring(self, s):
    ws, we, max = 0, 0, 0
    while( we < len(s) ):
      duplicate = 0
      for i in range(ws, we):
        if(s[i] == s[we]):
          duplicate = 1
          break

      if(duplicate):
        ws++
      else:
        current = we - ws + 1
        if(current > max):
          max = current
        we++

    return max
