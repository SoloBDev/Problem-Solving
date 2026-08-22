class Solution:
  def check_divisibility(n):
    sum, prod = 0, 1
    copy = n
    while(n>0):
      digit = n % 10;

      sum += digit
      prod *= digit

      n /= 10

    return copy % (sum + prod) == 0
