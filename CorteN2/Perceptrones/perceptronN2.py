inputs = [1, 2, 3, 4]
targets = [2, 4, 6, 8]
w = 0.1
epochs = 30
learning_rate = 0.1

def predict(x):
    return w * x

for epoch in range(epochs):
    # Paso 1: Hacer predicciones
    predictions = [predict(i) for i in inputs]
    
    # Paso 2: Calcular el error cuadrático (MSE)
    errors = [(p - t) ** 2 for p, t in zip(predictions, targets)]
    cost = sum(errors) / len(targets)
    
    # Paso 3: Derivada del error con respecto a w (gradiente)
    errors_d = [2 * (p - t) for p, t in zip(predictions, targets)]
    gradients = [e * i for e, i in zip(errors_d, inputs)]
    avg_gradient = sum(gradients) / len(gradients)
    
    # Paso 4: Actualizar el peso
    w -= learning_rate * avg_gradient

    # Mostrar resultados por época
    print(f"Epoch {epoch+1:02d} | Weight: {w:.4f} | Cost: {cost:.4f}")
