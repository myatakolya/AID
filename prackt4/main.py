import numpy as np
import matplotlib.pyplot as plt
import time

def f(x, a1, a2, w1, w2, b):
    return a1 * np.sin(w1 * x) + a2 * np.sin(w2 * x) + b

def loss(params, x):
    a1, a2, w1, w2, b = params
    return np.sum((x - f(np.arange(len(x)), a1, a2, w1, w2, b))**2)

def gradient(params, x):
    # Частные производные по параметрам
    a1, a2, w1, w2, b = params
    grad = np.zeros(5)
    
    # Вычисление градиентов
    predictions = f(np.arange(len(x)), a1, a2, w1, w2, b)
    error = predictions - x
    
    grad[0] = -2 * np.sum(error * np.sin(w1 * np.arange(len(x))))  # dL/da1
    grad[1] = -2 * np.sum(error * np.sin(w2 * np.arange(len(x))))  # dL/da2
    grad[2] = -2 * np.sum(error * a1 * np.arange(len(x)) * np.cos(w1 * np.arange(len(x))))  # dL/dw1
    grad[3] = -2 * np.sum(error * a2 * np.arange(len(x)) * np.cos(w2 * np.arange(len(x))))  # dL/dw2
    grad[4] = -2 * np.sum(error)  # dL/db
    
    return grad

def gradient_descent(x, params_init, learning_rate=0.001, iterations=1000):
    params = params_init
    for _ in range(iterations):
        params -= learning_rate * gradient(params, x)
    return params


def stochastic_gradient_descent(x, params_init, learning_rate=0.001, iterations=1000):
    params = params_init
    for _ in range(iterations):
        idx = np.random.randint(len(x))
        gradient_idx = gradient(params, x[idx:idx+1])
        params -= learning_rate * gradient_idx
    return params

# Задание номера в журнале
k = 13  # Замените на ваш номер
L = k / 100
omega = 1000 / k
dt = 2 * np.pi / 1000

# Генерация
N = 500
x = np.zeros(N)
x[0] = 0
x[1] = (-1) ** k * dt

for i in range(2, N):
    x[i] = (x[i-1] * (2 + dt * L * (1 - x[i-2]**2)) 
            - x[i-2] * (1 + dt**2 + dt * L * (1 - x[i-2]**2))
            + dt**2 * np.sin(omega * i * dt))
    
# Начальные параметры
params_init = np.random.rand(5)

# Градиентный спуск
start_time = time.time()
result_gd = gradient_descent(x, params_init)
gd_time = time.time() - start_time

# Стохастический градиентный спуск
start_time = time.time()
result_sgd = stochastic_gradient_descent(x, params_init)
sgd_time = time.time() - start_time

print(f"Время градиентного спуска: {gd_time:.4f} секунд")
print(f"Время стохастического градиентного спуска: {sgd_time:.4f} секунд")
