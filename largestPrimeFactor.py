import math

num = 600851475143
res = 0

while (num % 2 == 0):
  num /= 2

# # n must be odd at this point
for i in range(3, int(math.sqrt(num))+1, 2):
  while num % i == 0:
    res = i
    num = num / i

if num > 2:
  res = num

print(res)
