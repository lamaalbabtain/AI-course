"""
Day 41 Activity Solution: Probability Basics
"""

import numpy as np

np.random.seed(41)

# Coin flips
n = 20000
flips = np.random.choice(["H", "T"], size=n)
print("P(H):", (flips == "H").mean())
print("P(T):", (flips == "T").mean())

# Dice rolls
rolls = np.random.randint(1, 7, size=n)
print("P(even):", (rolls % 2 == 0).mean())
print("P(>=4):", (rolls >= 4).mean())
