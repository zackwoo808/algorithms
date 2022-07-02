# We are interested in understanding what day we see the highest traffic of doctor appointments within our network.
# Given an unsorted list containing appointment dates (represented as an integer), determine the date at which we had the highest amount of visits in a single day.
  
# test_case_one = [14, 14, 1, 2] 
# test_case_two = [2, 1]
  
# find_most_appointment_day(test_case_one) == 14
# find_most_appointment_day(test_case_two) == either 1 or 2

testCase1 = [14, 14, 1, 2, 8, 8, 8]
testCase2 = [2, 1]

def maxApptDays(dates):
  if not dates or not len(dates):
    return 0
  
  table = {}
  maxDate = 0

  for date in dates:
    if not table.get(date):
      table[date] = 1
      maxDate = date if not table.get(maxDate) or 1 > table.get(maxDate) else maxDate
    else:
      table[date] += 1
      maxDate = date if table.get(date) > table.get(maxDate) else maxDate
  
  return maxDate

print(maxApptDays(testCase1))
print(maxApptDays(testCase2))