# CPE 602-A Final Project

## Overview

This repo contains programming exercises as a part of the Final Project for a Discrete Mathematics course taken in Fall 2024. The project topic is: Greedy Algorithms.

### Files and Algorithms

There are three

## 01 - Cashier's Algorithm

**Description:** This program calculates the optimal way to provide change for a given amount in cents using quarters, dimes, nickels, and pennies. It includes two implementations: one using a direct pseudo-code approach and another using the modulo operator for faster computation.

**Functions:**

- `cashiers_algorithm_psuedo(amount, coins)`: Direct pseudo-code implementation.
- `cashiers_algorithm(amount, coins)`: Optimized implementation using the modulo operator.

**How to Run:**

```sh
python problem01.py
```

## 02 - Activity Selection Problem

**Description:** This program selects the maximum number of activities that don't overlap, given their start and end times. It uses a greedy approach to always pick the next activity that finishes the earliest.

**Functions:**

- `activity_selection(activities)`: Returns the maximum set of non-overlapping activities.

**How to Run:**

```sh
python problem02.py
```

## 03 - Fractional Knapsack Problem

**Description:** This program solves the fractional knapsack problem, where you can take fractions of items to maximize the total value in the knapsack. It uses a greedy approach to always take the item with the highest value-to-weight ratio first.

**Functions:**

- `fractional_knapsack(capacity, items)`: Returns the maximum value that fits in the knapsack.

**How to Run:**

```sh
python problem03.py
```
