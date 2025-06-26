inputs = [1, 2, 3, 4]
targets = [2, 4, 6, 8]
w = 0.1
learning_rate = 0.1

def predict(i):
    return w * i

for epoch in range(100):
    pred = [predict(i) for i in inputs]
    errors = [t - p for t, p in zip(targets, pred)]
    cost = sum(errors) / len(targets)
    print(f"Epoch {epoch+1}")
    print(f"Targets:      {targets}")
    print(f"Predictions:  {[round(p, 2) for p in pred]}")
    print(f"Errors:       {[round(e, 2) for e in errors]}")
    print(f"Weight: {w:.6f}  | Cost: {cost:.6f}")
    print("-" * 40)
    w += learning_rate * cost
