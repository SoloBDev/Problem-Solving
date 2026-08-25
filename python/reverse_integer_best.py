class Solution:
  def reverse_integer(self, x):
    isNegative = False\
    
    if(x < 0):
      isNegative = True
      x = -x
      
    res = 0  
    
    while( x > 0 ):
      res = (res * 10) + x % 10
      x = x // 10

    if res > 2**31 - 1 or res < -2**31:
      return 0
      
    if(isNegative) return -res
    else return res
