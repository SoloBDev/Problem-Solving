class Solution:
  def reverse_integer(self, x):
    digit, reverse, count = 0, 0. 0
    copy = x
    if(x == 0 and copy == 0) return 0
    while( x != 0):
      digit = x % 10
      x = x//10
      count++
    while( copy != 0):
      digit = copy % 10
      reverse = reverse + digit * 10**(count-1)
      copy = copy // 10
      count--
    return reverse
