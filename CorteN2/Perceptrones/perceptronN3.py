inputs = [1, 2, 3, 4]
targets = [2, 4, 6, 8]
w = 0.1
b = 0.3
epochs = 300
learning_rate = 0.1

def predict(x):
    return w * x + b

for epoch in range(epochs):
    # Paso 1: Predicciones
    predictions = [predict(i) for i in inputs]
    
    # Paso 2: Error cuadrático medio (MSE)
    errors = [(p - t) ** 2 for p, t in zip(predictions, targets)]
    cost = sum(errors) / len(errors)
    
    # Paso 3: Derivadas (gradientes)
    errors_d = [2 * (p - t) for p, t in zip(predictions, targets)]
    weight_d = [e * i for e, i in zip(errors_d, inputs)]
    bias_d = errors_d  # derivada respecto a b es simplemente 1, por eso se multiplica por 1

    # Paso 4: Actualización de parámetros
    w -= learning_rate * sum(weight_d) / len(weight_d)
    b -= learning_rate * sum(bias_d) / len(bias_d)

    # Paso 5: Mostrar resultados
    if epoch % 10 == 0 or epoch == epochs - 1:
        print(f"Epoch {epoch+1:03d} | Weight: {w:.4f}, Bias: {b:.4f}, Cost: {cost:.4f}")
