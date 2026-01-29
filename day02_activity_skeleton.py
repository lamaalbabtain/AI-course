"""
Day 2 Activity: Build a utility library with reusable functions.
Required functions:
1) calculate_statistics(data)
2) normalize_data(data, method)
3) remove_outliers(data, threshold)
4) train_test_split(data, ratio)
5) encode_labels(labels)
"""
from typing import List, Dict, Tuple

# TODO: Implement each function below.

# def calculate_statistics(data: List[float]) -> Dict[str, float]:
def calculate_statistics(data: List[float]) -> Dict[str, float]:
    mean = sum(data) / len(data)
    return {
        "mean": mean,
        "min": min(data),
        "max": max(data)
    }


# def normalize_data(data: List[float], method: str = "minmax") -> List[float]:
def normalize_data(data: List[float], method: str = "minmax") -> List[float]:
    if method == "minmax":
        min_val = min(data)
        max_val = max(data)
        return [(x - min_val) / (max_val - min_val) for x in data]
    else:
        raise ValueError("Unsupported normalization method")


# def remove_outliers(data: List[float], threshold: float) -> List[float]:
def remove_outliers(data: List[float], threshold: float) -> List[float]:
    mean = sum(data) / len(data)
    return [x for x in data if abs(x - mean) <= threshold]


# def train_test_split(data: List[float], ratio: float = 0.8) -> Tuple[List[float], List[float]]:
def train_test_split(data: List[float], ratio: float = 0.8) -> Tuple[List[float], List[float]]:
    split = int(len(data) * ratio)
    return data[:split], data[split:]


# def encode_labels(labels: List[str]) -> Dict[str, int]:
def encode_labels(labels: List[str]) -> Dict[str, int]:
    return {label: index for index, label in enumerate(labels)}


# TODO: Add small tests for each function.
print(calculate_statistics([1, 2, 3, 4, 5]))
print(normalize_data([10, 20, 30]))
print(remove_outliers([10, 12, 14, 100], 20))
print(train_test_split([1, 2, 3, 4, 5]))
print(encode_labels(["cat", "dog", "bird"]))