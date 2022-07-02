sum = 0

firstNum = 1
secondNum = 2

while (True):
  localSum = firstNum + secondNum

  if localSum > 4000000:
    print(sum + 2)
    break
  
  if localSum % 2 == 0:
    sum += localSum
  
  firstNum = secondNum
  secondNum = localSum
