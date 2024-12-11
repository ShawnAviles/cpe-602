"""
Fractional Knapsack Problem:
This program solves the fractional knapsack problem using a greedy algorithm.

Approach:
1. Calculate the value-to-weight ratio for each item.
2. Sort items in descending order based on the value-to-weight ratio.
3. Add items to the knapsack in this order, taking full items when possible and fractions when necessary.
4. Stop when the knapsack reaches its weight limit.

Input:
- List of items with their values and weights.
- Maximum weight capacity of the knapsack.

Output:
- Maximum total value that can be obtained.
- Breakdown of items (full or fractional) added to the knapsack.
"""

def fractional_knapsack(items, capacity):
  """
  Solve the fractional knapsack problem.

  :param items: List of tuples [(value, weight), ...]
  :param capacity: Maximum weight capacity of the knapsack
  :return: Maximum value and list of items added to the knapsack
  """
  # Calculate value-to-weight ratio and sort items by this ratio in descending order
  items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)

  total_value = 0
  knapsack_contents = []

  # Add items to the knapsack
  for value, weight in items:
    if capacity == 0:
      break
    # Check if the whole item can be taken
    if weight <= capacity:
      # Take the whole item
      knapsack_contents.append((value, weight, 1))  # 1 indicates fully taken
      total_value += value
      capacity -= weight
    else:
      # Take a fraction of the item
      fraction = capacity / weight
      knapsack_contents.append((value, weight, fraction))
      total_value += value * fraction
      capacity = 0  # Knapsack is full

  return total_value, knapsack_contents

# Example test cases
items = [(60, 10), (100, 20), (120, 30)]  # Each tuple is (value, weight)
capacity = 50

max_value, knapsack = fractional_knapsack(items, capacity)

print("Maximum value obtainable:", max_value)
print("Knapsack contents:")
for value, weight, fraction in knapsack:
  print(f"Value: {value}, Weight: {weight}, Fraction taken: {fraction}")
