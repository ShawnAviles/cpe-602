# Problem Statement: Given an integer n, use the cashier's algorithm to find the change for n cents using 
# quarters, dimes, nickel, and pennies,

"""
Cashier's Algorithm:
This program calculates the optimal way to provide change for a given amount in cents.
The algorithm uses quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent)
to minimize the number of coins.

Approach:
1. Start with the highest denomination (quarters) and work downward (to penny).
2. For each denomination, calculate the maximum number of coins that fit into the remaining amount.
3. Subtract the value of the coins from the total amount and repeat for the next denomination.
"""
 
# Function based off of the cashier's algorithm - direct psuedo code implementation
# Time complexity: O(n)
def cashiers_algorithm_psuedo(amount, coins):  
  result = {}
  currentCoinIndex = 0
  
  while amount != 0:
    coin = coins[currentCoinIndex]
    
    # calculate the number of coins of the current denomination
    if amount >= coin:
      amount -= coin
      result[str(coin)] = result.get(str(coin), 0) + 1
    # move to the next coin denomination
    else:
      currentCoinIndex += 1
      
  # return the output result
  return result

# Function slightly modified to use modulo operator for faster computation
# Time complexity: O(1)
def cashiers_algorithm(amount, coins):  
  result = {}
  # iterate over each coin denomination from highest to lowest
  for coin in coins:
    # be 'greedy' determine how many of the current highest denomination coin can be used
    result[str(coin)] = amount // coin
    # decrease the remaining amount by the value of the coins used
    # - we can use modulo of the coin denomination as the remainder amount is less than the coin value
    #   hence we can't use the current coin denomination anymore
    amount %= coin
  
  # return the output result
  return result



# Cashier's Algorithm Test cases
cashiers_algo_coins = [25, 10, 5, 1]
test_cases = [41, 99, 56, 78, 32]
print("Cashier's Algorithm Test Cases - Base:")
for test in test_cases:
  print(f"1. Amount: {test} cents -> Change: {cashiers_algorithm(test, cashiers_algo_coins)}")
  print(f"2. Amount: {test} cents -> Change: {cashiers_algorithm_psuedo(test, cashiers_algo_coins)}\n")

# Cashier's Algorithm Test cases with different coin denominations
different_coins_1 = [5, 4, 3, 1] # different denominations
different_coins_2 = [25, 10, 1] # different denominations
different_test_cases_1 = [7, 16]
different_test_cases_2 = [30, 35]

print("Cashier's Algorithm Test Cases - Different Denominations:")
print("1. Different Denominations: [5, 4, 3, 1]")
for test in different_test_cases_1:
  print(f"Amount: {test} cents -> Change: {cashiers_algorithm_psuedo(test, different_coins_1)}")
print("2. Different Denominations: [25, 10, 1]")
for test in different_test_cases_2:
  print(f"Amount: {test} cents -> Change: {cashiers_algorithm_psuedo(test, different_coins_2)}")
