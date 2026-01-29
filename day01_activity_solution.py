"""
Day 1 Activity Solution: Refactoring repeated code into functions.
"""

from typing import List, Dict

# Sample data
cat_a = [1, 2, 3, 4, 5]
cat_b = [10, 20, 30]


def calculate_stats(data: List[float]) -> Dict[str, float]:
    """Return basic stats for a numeric list."""
    if not data:
        return {"mean": 0.0, "max": float("-inf")}
    return {
        "mean": sum(data) / len(data),
        "max": max(data),
    }


stats_a = calculate_stats(cat_a)
stats_b = calculate_stats(cat_b)

print("A:", stats_a)
print("B:", stats_b)
