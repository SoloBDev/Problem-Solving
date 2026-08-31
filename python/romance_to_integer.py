class Solution:
  def romance_to_integer(self, s):
    total, previous = 0, 0
    for i in range(len(s) - 1, -1, -1):
      match s[i]:
        case 'I':
          value 1
        case 'V':
          value 5
        case 'X':
          value 10
        case 'L':
          value 50
        case 'C':
          value 100
        case 'D':
          value 500
        case 'M':
          value 1000
      if value < previous:
        total -= value
      else:
        total += value
      previous = value

      return total
      
          
