i = 999
j = 999

table = {}

def isPalindrome(num):
  if table.get(num) == True:
    return True
  
  if table.get(num) == False:
    return False

  s = str(num)
  l = 0
  r = len(s) - 1

  while (l <= r):
    if (s[l] != s[r]):
      table[s] = False
      return False
    
    l += 1
    r -= 1
  
  table[num] = True
  return True

max = 0
while i > 0:
  while j > 0:
    prod = i * j
    if isPalindrome(prod) and prod > max:
      max = prod
    j -= 1

  i -= 1
  j = 999

print(max)