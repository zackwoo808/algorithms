# We're also interested in understanding what the maximum number of appointments in a K day period was.
# Implement a method that can take a K day input and return the maximum number of appointments within a K day period.
# 
# appointments = [4, 24, 23, 24, 22, 5, 5, 4, 4, 3] 
# k = 3
#
#
# find_most_appointment_day_k_period(appointments, k) == 6
#
# Day 24 -> 2 Appointments
# Day 23 -> 1 Appointment
# Day 22 -> 1 Appointment
# ...
# Day 6 -> 0 Appointments
# Day 5 -> 2 Appointments
# Day 4 -> 3 Appointments
# Day 3 -> 1 Appointment
# Day 2 -> 0 Appointments

def maxApptWindow(appts, k):
  if not appts or len(appts) < 1 or k < 1:
    return 0
  
  # make calendar
  table = {}
  for date in appts:
    table[date] = 1 if not table.get(date) else table[date] + 1
  apptsPerDate = [table.get(x+1) or 0 for x in range(31)]

  left = 0
  right = 0
  max = 0

  # establish initial window size
  while (right - left < k):
    max += apptsPerDate[right]
    right += 1

  temp = max
  # print(left, right, temp)
  while (right < len(apptsPerDate)):
    temp = temp + apptsPerDate[right] - apptsPerDate[left]
    if temp > max:
      max = temp
    
    # slide window
    right += 1
    left += 1
  return max

print(maxApptWindow([4, 24, 23, 24, 22, 5, 5, 4, 4, 3], 3))