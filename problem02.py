# Given the starting and ending times of n talks, use the appropriate greedy algorithm to schedule 
# the most talks possible in a single lecture hall

"""
Activity Selection Problem:
This program schedules the maximum number of non-overlapping activities in a single lecture hall.
We are provided with each activity's start time and end time.

Approach:
1. Sort all activities by their end times - greedy choice.
2. Select the first activity and skip to the next one that starts after the previous ends.
3. Repeat until all activities are considered.
"""

# Time complexity: O(nlogn) due to sorting
def activity_selection(activities):
  # Sort activities by end time - our greedy choice
  activities.sort(key=lambda x: x[1])
  
  selected_activities = []
  current_end_time = 0
  
  for start, end in activities:
    # check if current activity is compatible with the previous one
    # compare the start time of the current activity with the end time of the previous activity
    if start >= current_end_time:
      selected_activities.append((start, end))
      # update the end time of the previous activity
      current_end_time = end
  
  # return the selected activities
  return selected_activities

# Test cases
test_cases = [
    [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)],
    [(1, 3), (2, 5), (4, 7), (6, 8), (5, 9), (8, 10)],
    [(0, 1), (3, 5), (4, 6), (5, 7), (8, 9), (8, 11)],
    [(1, 3), (3, 5), (0, 6), (8, 9), (5, 7), (8, 10)],
    [(0, 2), (1, 4), (2, 5), (4, 6), (6, 8), (7, 9)],
]
print("Activity Selection Problem Test Cases:")
for i, test in enumerate(test_cases):
    print(f"Test Case {i + 1}: Activities: {test} -> Selected: {activity_selection(test)}")
