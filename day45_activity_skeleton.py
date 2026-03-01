import numpy as np


np.random.seed(42)
X = np.random.randn(100, 3)
y_true = np.random.randint(0, 3, 100)


W = np.random.randn(3, 3)
b = np.random.randn(3)
logits = X @ W + b
probs = np.exp(logits) / np.sum(np.exp(logits), axis=1, keepdims=True)


y_pred = np.argmax(probs, axis=1)
accuracy = np.mean(y_pred == y_true)

print("Predictions:", y_pred[:10])
print("True labels:", y_true[:10])
print("Accuracy:", accuracy)