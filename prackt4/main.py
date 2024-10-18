from time import time
from math import pi, sin, cos
from dsmltf import gradient_descent, minimize_stochastic
import matplotlib.pyplot as plt

# параметры
k=2
dt = 2*pi/1000
x = [0,(-1)**k * dt]
base = [2*pi*(i/500) for i in range(500)]
omega=1000/k
L=k/100

def furie(k,a):
    return a[0]+a[1]*cos(base[k]) + a[2]*sin(base[k])+a[3]*cos(2*base[k])+a[4]*sin(2*base[k])

# функция ошибки для обычного градиентного спуска
def F(a):
    return sum([(x[j]-furie(j,a))**2 for j in range(500)])

# функция ошибки для стохатического градиентного спуска
def f(i,a):
    global x
    return (x[i]-furie(i,a))**2



for i in range(2,500):
    x.append(x[i-1]*(2+dt*L*(1-x[i-2]**2))- x[i-2]*(1+dt**2+dt*L*(1-x[i-2]**2))+dt**2*sin(omega*dt))  

# вычисляем коэфициенты
s_t_0 = time()
a0 = gradient_descent(F,[0]*5)
s_t_1 = time()
a1 = minimize_stochastic(f,[i for i in range(500)],[0]*500,[0]*5)
print(a0[0],a0[1])
print(a1[0],a1[1])
print(f"{s_t_1-s_t_0} секунд",f"{time()-s_t_1} секунд")

# рисуем графики
plt.plot(base, x, label='Изначальная функция', linestyle='-', color='green')
plt.plot(base, [furie(i,a0[0]) for i in range(500)], label=f'Градиентный спуск', linestyle='-.', color='red')
plt.plot(base, [furie(i,a1[0]) for i in range(500)], label=f'Стохатичный градиентный спуск', linestyle='-.', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
