"""
Day 44 Activity: Log, Exp, Softmax
"""

import numpy as np

def softmax_stable(scores):
    shifted = scores - np.max(scores)
    exp_vals = np.exp(shifted)
    return exp_vals / np.sum(exp_vals)

score_vector = np.array([2.5, 0.3, -1.2, 4.0])

probabilities = softmax_stable(score_vector)

print("Probabilities:", probabilities)
print("Sum of probabilities:", np.sum(probabilities))